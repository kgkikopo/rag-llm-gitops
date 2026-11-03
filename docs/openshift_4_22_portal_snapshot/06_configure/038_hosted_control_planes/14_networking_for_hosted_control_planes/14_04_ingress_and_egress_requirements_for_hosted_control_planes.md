# 14.4. Ingress and egress requirements for hosted control planes

Open network ports to enable communication between the management cluster, hosted control planes components, and compute nodes. Categorize them into ingress ports for incoming traffic to hosted control planes and egress ports for outgoing traffic from hosted control planes. 

## 14.4.1. Ingress requirements for hosted control planes

Ingress ports involve incoming traffic to hosted control planes. Ensure the correct ports are open for communication between the management cluster, the hosted control planes components, and the compute nodes. 

The following table details the ports for incoming traffic to hosted control planes across all platforms: 

Table 14.1. Common ingress portsPort| Protocol| Service| Description| Code reference  
---|---|---|---|---  
`6443` |  TCP  |  Kubernetes API server  |  Primary API server port for `kubectl` and cluster communication  |  `support/config/constants.go:35` \- `KASSVCPort = 6443`  
`9090` |  TCP  |  Ignition server  |  Port from compute nodes during the bootstrap process, `NodePort` or `Route` service publishing strategy  |  \-   
Show more

The service publishing strategy determines additional ports. The `Ignition Proxy` and `Konnectivity` services are exposed through one of the following service publishing strategies: 

`Route`
     This setting is the default on OpenShift Container Platform. Traffic flows through the OpenShift router on port 443. No additional firewall rules are needed beyond standard HTTPS. 
`NodePort`
     Direct access is required to port 8091 (Konnectivity) and port 8443 (Ignition Proxy). 
`LoadBalancer`
     Direct access is required to port 8091 (Konnectivity) through the cloud load balancer. 

The following table details the ingress port configurations that are specific to each platform: 

Table 14.2. Platform-specific ingress port configurationsPlatform| Port| Service| Description| Code reference  
---|---|---|---|---  
Agent  |  `8443` |  Ignition Proxy  |  HTTPS proxy for ignition content delivery (`NodePort` publishing)  |  `hypershift-operator/controllers/hostedcluster/network_policies.go:390`  
Agent  |  `8081` |  Agent CAPI health probe  |  Health check endpoint for Agent platform CAPI provider  |  `hypershift-operator/controllers/hostedcluster/internal/platform/agent.go:96,105,115`  
Agent  |  `8080` |  Agent CAPI metrics  |  Metrics endpoint for Agent platform CAPI provider (binds to localhost only)  |  `hypershift-operator/controllers/hostedcluster/internal/platform/agent/agent.go:97`  
AWS  |  `9440` |  CAPI health check  |  Health and readiness probe endpoint for AWS CAPI provider  |  `hypershift-operator/controllers/hostedcluster/internal/platform/aws/aws.go:222-223`  
Bare metal without the Agent platform  |  `8443` |  Ignition Proxy  |  HTTPS proxy for ignition content delivery (`NodePort` publishing)  |  \-   
KubeVirt  |  `9440` |  CAPI health check  |  Health and readiness probe endpoint  |  `hypershift-operator/controllers/hostedcluster/internal/platform/kubevirt/kubevirt.go:140`  
RHOSP (Technology Preview)  |  `9440` |  CAPI health check  |  Health and readiness probe endpoint  |  `hypershift-operator/controllers/hostedcluster/internal/platform/openstack/openstack.go:238`  
RHOSP (Technology Preview)  |  `8081` |  ORC health check  |  Health and readiness probe endpoint for OpenStack Resource Controller  |  `hypershift-operator/controllers/hostedcluster/internal/platform/openstack/openstack.go:294,311`  
Show more

The following table details the ingress port configurations for private clusters, such as those on AWS: 

Table 14.3. Ingress port configurations for private clustersPort| Service| Description| Code reference  
---|---|---|---  
`8080` |  Private router HTTP  |  HTTP traffic through the private router  |  `hypershift-operator/controllers/hostedcluster/network_policies.go:244`  
`8443` |  Private router HTTPS  |  HTTPS traffic through the private router  |  `hypershift-operator/controllers/hostedcluster/network_policies.go:245`  
Show more

## 14.4.2. Egress requirements for hosted control planes

Egress ports involve outgoing traffic from hosted control planes. Ensure the correct ports are open for communication between the management cluster, the hosted control planes components, and the compute nodes. 

The following table details the ports that must be accessible for outgoing traffic from hosted control planes, across all platforms. 

Table 14.4. Common egress portsPort| Protocol| Service| Purpose  
---|---|---|---  
`443` |  TCP  |  HTTPS  |  OLM images, `Ignition` content, external HTTPS services   
`6443` |  TCP  |  Kubernetes API server  |  Communication with management cluster API   
`53` |  TCP and UDP  |  DNS  |  Standard DNS queries   
Show more

Compute nodes require outbound network access to several hosted control planes services. The following table details the egress requirements for compute nodes. 

Table 14.5. Compute node egress requirementsPort| Protocol| Service| Purpose| When required  
---|---|---|---|---  
`443` |  TCP  |  HTTPS  |  Container registries, `Ignition` or `Konnectivity` service via `Route` service publishing strategy, external HTTPS services  |  Always   
`6443` |  TCP  |  Kubernetes API server  |  Cluster management and kubelet communication  |  Always   
`8091` |  TCP  |  Konnectivity server  |  Establishes a reverse tunnel for control plane access  |  `NodePort` or `LoadBalancer` publishing only   
`8443` |  TCP  |  Ignition Proxy  |  Retrieves bootstrap configuration  |  `NodePort` publishing only for Agent platform or bare metal   
`53` |  TCP and UDP  |  DNS  |  Name resolution  |  Always   
Show more

## 14.4.3. Handling ingress in a hosted cluster on bare metal

Every OpenShift Container Platform cluster has a default application Ingress Controller that typically has an external DNS record associated with it. 

For example, if you create a hosted cluster named `example` with the base domain `krnl.es`, you can expect the wildcard domain `*.apps.example.krnl.es` to be routable. 

To set up a load balancer and wildcard DNS record for the `*.apps` domain, perform the following actions on your hosted cluster. 

**Procedure**

  1. Deploy MetalLB by creating a YAML file that has the configuration for the MetalLB Operator: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: metallb
  labels:
    openshift.io/cluster-monitoring: "true"
  annotations:
    workload.openshift.io/allowed: management
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: metallb-operator-operatorgroup
  namespace: metallb
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: metallb-operator
  namespace: metallb
spec:
  channel: "stable"
  name: metallb-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


  2. Save the file as `metallb-operator-config.yaml`. 
  3. Enter the following command to apply the configuration: 

```shell-session
$ oc apply -f metallb-operator-config.yaml
```


  4. After the Operator is running, create the MetalLB instance: 

     1. Create a YAML file that has the configuration for the MetalLB instance: 

```yaml
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb
```


     2. Save the file as `metallb-instance-config.yaml`. 
     3. Create the MetalLB instance by entering this command: 

```shell-session
$ oc apply -f metallb-instance-config.yaml
```


  5. Create an `IPAddressPool` resource with a single IP address. This IP address must be on the same subnet as the network that the cluster nodes use. 

     1. Create a file, such as `ipaddresspool.yaml`, with content similar to the following example: 

```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb
  name: <ip_address_pool_name>
spec:
  addresses:
    - <ingress_ip>-<ingress_ip>
  autoAssign: false
```


        * `metadata.name` specifies the `IPAddressPool` resource name. 
        * `spec.addresses` specifies the IP address for your environment. For example, `192.168.122.23`. 

     2. Apply the configuration for the IP address pool by entering the following command: 

```shell-session
$ oc apply -f ipaddresspool.yaml
```


  6. Create a L2 advertisement. 

     1. Create a file, such as `l2advertisement.yaml`, with content similar to the following example: 

```yaml
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: <l2_advertisement_name>
  namespace: metallb
spec:
  ipAddressPools:
   - <ip_address_pool_name>
```


        * `metadata.name` specifies the `L2Advertisement` resource name. 
        * `spec.ipAddressPools` specifies the `IPAddressPool` resource name. 

     2. Apply the configuration by entering the following command: 

```shell-session
$ oc apply -f l2advertisement.yaml
```


  7. After creating a service of the `LoadBalancer` type, MetalLB adds an external IP address for the service. 

     1. Configure a new load balancer service that routes ingress traffic to the ingress deployment by creating a YAML file named `metallb-loadbalancer-service.yaml`: 

```yaml
kind: Service
apiVersion: v1
metadata:
  annotations:
   metallb.io/address-pool: ingress-public-ip
  name: metallb-ingress
  namespace: openshift-ingress
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 80
    - name: https
      protocol: TCP
      port: 443
      targetPort: 443
  selector:
    ingresscontroller.operator.openshift.io/deployment-ingresscontroller: default
  type: LoadBalancer
```


     2. Save the `metallb-loadbalancer-service.yaml` file. 
     3. Enter the following command to apply the YAML configuration: 

```shell-session
$ oc apply -f metallb-loadbalancer-service.yaml
```


     4. Enter the following command to reach the OpenShift Container Platform console: 

```bash
$ curl -kI https://console-openshift-console.apps.example.krnl.es
```


**Example output**

```shell-session
HTTP/1.1 200 OK
```


     5. Check the `clusterversion` and `clusteroperator` values to verify that everything is running. Enter the following command: 

```shell-session
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get clusterversion,co
```


**Example output**

```shell-session
NAME                                         VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
clusterversion.config.openshift.io/version   4.x.y      True        False        3m32s   Cluster version is 4.x.y

NAME                                                                             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
clusteroperator.config.openshift.io/console                                      4.x.y     True        False         False      3m50s
clusteroperator.config.openshift.io/ingress                                      4.x.y     True        False         False      53m
```


Replace `<4.x.y>` with the supported OpenShift Container Platform version that you want to use, for example, `4.22.0-multi`.
