# 10.2. Deploy an egress service

You can deploy an egress service to manage egress traffic for pods behind a `LoadBalancer` service. 

The following example configures the egress traffic to have the same source IP address as the ingress IP address of the `LoadBalancer` service. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in as a user with `cluster-admin` privileges. 
  * You configured MetalLB `BGPPeer` resources. 



**Procedure**

  1. Create an `IPAddressPool` CR with the desired IP for the service: 

     1. Create a file, such as `ip-addr-pool.yaml`, with content like the following example: 

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: example-pool
  namespace: metallb-system
spec:
  addresses:
  - 172.19.0.100/32
```


     2. Apply the configuration for the IP address pool by running the following command: 

```shell-session
$ oc apply -f ip-addr-pool.yaml
```


  2. Create `Service` and `EgressService` CRs: 

     1. Create a file, such as `service-egress-service.yaml`, with content like the following example: 

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
  namespace: example-namespace
  annotations:
    metallb.io/address-pool: example-pool
spec:
  selector:
    app: example
  ports:
    - name: http
      protocol: TCP
      port: 8080
      targetPort: 8080
  type: LoadBalancer
---
apiVersion: k8s.ovn.org/v1
kind: EgressService
metadata:
  name: example-service
  namespace: example-namespace
spec:
  sourceIPBy: "LoadBalancerIP"
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker: ""
```


where: 

`metadata.annotations.metallb.io/address-pool`
     Specifies the `LoadBalancer` service uses the IP address assigned by MetalLB from the `example-pool` IP address pool. 
`spec.sourceIPBy`
     This example uses the `LoadBalancerIP` value to assign the ingress IP address of the `LoadBalancer` service as the source IP address of egress traffic. 
`spec.nodeSelector`
    

When you specify the `LoadBalancerIP` value, a single node handles the `LoadBalancer` service’s traffic. In this example, only nodes with the `worker` label can be selected to handle the traffic. When a node is selected, OVN-Kubernetes labels the node in the following format `egress-service.k8s.ovn.org/<svc-namespace>-<svc-name>: ""`. 

Note

If you use the `sourceIPBy: "LoadBalancerIP"` setting, you must specify the load-balancer node in the `BGPAdvertisement` custom resource (CR). 

     2. Apply the configuration for the service and egress service by running the following command: 

```shell-session
$ oc apply -f service-egress-service.yaml
```


  3. Create a `BGPAdvertisement` CR to advertise the service: 

     1. Create a file, such as `service-bgp-advertisement.yaml`, with content like the following example: 

```yaml
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: example-bgp-adv
  namespace: metallb-system
spec:
  ipAddressPools:
  - example-pool
  nodeSelectors:
  - matchLabels:
      egress-service.k8s.ovn.org/example-namespace-example-service: ""
```


where: 

`spec.nodeSelectors.matchLabels`
     In the example, the `EgressService` CR configures the source IP address for egress traffic to use the load-balancer service IP address. Therefore, you must specify the load-balancer node for return traffic to use the same return path for the traffic originating from the pod. 




**Verification**

  1. Verify that you can access the application endpoint of the pods running behind the MetalLB service by running the following command: 

```shell-session
$ curl <external_ip_address>:<port_number>
```


`<external_ip_address>:<port_number`
     Update the external IP address and port number to suit your application endpoint. 

  2. If you assigned the `LoadBalancer` service’s ingress IP address as the source IP address for egress traffic, verify this configuration by using tools such as `tcpdump` to analyze packets received at the external client. 



**Additional resources**

  * [Exposing a service through a network VRF](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-metallb-bgp-peer-vrf_configure-metallb-bgp-peers)
  * [Example: Network interface with a VRF instance node network configuration policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/kubernetes_nmstate/#virt-example-host-vrf_k8s-nmstate-updating-node-network-config)
  * [Managing symmetric routing with MetalLB](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#metallb-configure-return-traffic)
  * [About virtual routing and forwarding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#cnf-about-virtual-routing-and-forwarding_about-virtual-routing-and-forwarding)
