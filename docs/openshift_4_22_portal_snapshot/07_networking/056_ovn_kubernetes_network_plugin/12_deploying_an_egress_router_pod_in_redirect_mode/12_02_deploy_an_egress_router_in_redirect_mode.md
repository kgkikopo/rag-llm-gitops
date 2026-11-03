# 12.2. Deploy an egress router in redirect mode

You can deploy an egress router to redirect traffic from its own reserved source IP address to one or more destination IP addresses. 

After you add an egress router, the client pods that need to use the reserved source IP address must be modified to connect to the egress router rather than connecting directly to the destination IP. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create an egress router definition. 
  2. To ensure that other pods can find the IP address of the egress router pod, create a service that uses the egress router, as in the following example: 

```yaml
apiVersion: v1
kind: Service
metadata:
  name: egress-1
spec:
  ports:
  - name: web-app
    protocol: TCP
    port: 8080
  type: ClusterIP
  selector:
    app: egress-router-cni
```


`spec.selector`: Specifies the label for the egress router. The value shown is added by the Cluster Network Operator and is not configurable. 

After you create the service, your pods can connect to the service. The egress router pod redirects traffic to the corresponding port on the destination IP address. The connections originate from the reserved source IP address. 




**Verification**

  1. View the network attachment definition that the Operator created for the egress router: 

```shell-session
$ oc get network-attachment-definition egress-router-cni-nad
```


The name of the network attachment definition is not configurable. 

**Example output**

```shell-session
NAME                    AGE
egress-router-cni-nad   18m
```


  2. View the deployment for the egress router pod: 

```shell-session
$ oc get deployment egress-router-cni-deployment
```


The name of the deployment is not configurable. 

**Example output**

```shell-session
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
egress-router-cni-deployment   1/1     1            1           18m
```


  3. View the status of the egress router pod: 

```shell-session
$ oc get pods -l app=egress-router-cni
```


**Example output**

```shell-session
NAME                                            READY   STATUS    RESTARTS   AGE
egress-router-cni-deployment-575465c75c-qkq6m   1/1     Running   0          18m
```


  4. View the logs and the routing table for the egress router pod. 

     1. Get the node name for the egress router pod: 

```shell-session
$ POD_NODENAME=$(oc get pod -l app=egress-router-cni -o jsonpath="{.items[0].spec.nodeName}")
```


     2. Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`: 

```shell-session
$ oc debug node/$POD_NODENAME
```


     3. Set `/host` as the root directory within the debug shell. The debug pod mounts the root file system of the host in `/host` within the pod. By changing the root directory to `/host`, you can run binaries from the executable paths of the host: 

```shell-session
# chroot /host
```


     4. From within the `chroot` environment console, display the egress router logs: 

```shell-session
# cat /tmp/egress-router-log
```


**Example output**

```shell-session
2021-04-26T12:27:20Z [debug] Called CNI ADD
2021-04-26T12:27:20Z [debug] Gateway: 192.168.12.1
2021-04-26T12:27:20Z [debug] IP Source Addresses: [192.168.12.99/24]
2021-04-26T12:27:20Z [debug] IP Destinations: [80 UDP 10.0.0.99/30 8080 TCP 203.0.113.26/30 80 8443 TCP 203.0.113.27/30 443]
2021-04-26T12:27:20Z [debug] Created macvlan interface
2021-04-26T12:27:20Z [debug] Renamed macvlan to "net1"
2021-04-26T12:27:20Z [debug] Adding route to gateway 192.168.12.1 on macvlan interface
2021-04-26T12:27:20Z [debug] deleted default route {Ifindex: 3 Dst: <nil> Src: <nil> Gw: 10.128.10.1 Flags: [] Table: 254}
2021-04-26T12:27:20Z [debug] Added new default route with gateway 192.168.12.1
2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat PREROUTING -i eth0 -p UDP --dport 80 -j DNAT --to-destination 10.0.0.99
2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat PREROUTING -i eth0 -p TCP --dport 8080 -j DNAT --to-destination 203.0.113.26:80
2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat PREROUTING -i eth0 -p TCP --dport 8443 -j DNAT --to-destination 203.0.113.27:443
2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat -o net1 -j SNAT --to-source 192.168.12.99
```


The logging file location and logging level are not configurable when you start the egress router by creating an `EgressRouter` object as described in this procedure. 

     5. From within the `chroot` environment console, get the container ID: 

```shell-session
# crictl ps --name egress-router-cni-pod | awk '{print $1}'
```


**Example output**

```shell-session
CONTAINER
bac9fae69ddb6
```


     6. Determine the process ID of the container. In this example, the container ID is `bac9fae69ddb6`: 

```shell-session
# crictl inspect -o yaml bac9fae69ddb6 | grep 'pid:' | awk '{print $2}'
```


**Example output**

```shell-session
68857
```


     7. Enter the network namespace of the container: 

```shell-session
# nsenter -n -t 68857
```


     8. Display the routing table: 

```shell-session
# ip route
```


In the following example output, the `net1` network interface is the default route. Traffic for the cluster network uses the `eth0` network interface. Traffic for the `192.168.12.0/24` network uses the `net1` network interface and originates from the reserved source IP address `192.168.12.99`. The pod routes all other traffic to the gateway at IP address `192.168.12.1`. Routing for the service network is not shown. 

**Example output**

```shell-session
default via 192.168.12.1 dev net1
10.128.10.0/23 dev eth0 proto kernel scope link src 10.128.10.18
192.168.12.0/24 dev net1 proto kernel scope link src 192.168.12.99
192.168.12.1 dev net1
```
