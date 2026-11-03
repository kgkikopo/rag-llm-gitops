# 14.5. Configuring internal OVN IPv4 subnets for hosted clusters

In hosted clusters, you can configure internal OVN subnets to avoid routing conflicts, customize network architecture, or enable virtual private cloud (VPC) peering. 

Avoid CIDR conflicts
     Connect VPCs that host Red Hat OpenShift Service on AWS clusters with other VPCs that use the default OVN internal subnets of 100.88.0.0/16 and 100.64.0.0/16. To avoid a conflict on a `kubevirt` hosted cluster, the HyperShift Operator sets the OVN join subnet to `100.66.0.0/16` instead of `100.64.0.0/16` or `100.65.0.0/16`. The default classless inter-domain routing (CIDR) for the OVN gateway router is `100.64.0.0/16`. The default CIDR for the user-defined network (UDN) join subnet is `100.65.0.0/16`. 
Customize network architecture
     Configure internal OVN subnets to align with your corporate network policies. 
Enable VPC peering
     Deploy hosted clusters in environments where default subnets conflict with peered networks. 

To configure OVN-internal subnets, you expose two OVN-Kubernetes internal subnet configuration options: 

`internalJoinSubnet`
     Internal subnet used by OVN-Kubernetes for the join network (default: `100.64.0.0/16`) 
`internalTransitSwitchSubnet`
     Internal subnet used for the distributed transit switch in OVN Interconnect architecture (default: `100.88.0.0/16`) 

You can configure internal OVN subnets in an existing hosted cluster or configure the subnets while you create a hosted cluster. 

**Prerequisites**

  * Your hosted cluster version must be OpenShift Container Platform 4.20 or later. 
  * For the network type, your hosted cluster must use `networkType: OVNKubernetes`. 
  * Custom subnets must not overlap with the following subnets: 

    * Machine CIDRs 
    * Service CIDRs 
    * Cluster network CIDRs 
    * Any other networks in your infrastructure 




**Procedure**

  * To configure internal OVN subnets while you create a hosted cluster, in the configuration file for the hosted cluster, include the following section: 

```yaml
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_control_plane_namespace>
spec:
  networking:
    networkType: OVNKubernetes
    machineCIDR: 10.0.0.0/16
    serviceCIDR: 172.30.0.0/16
    clusterNetwork:
    - cidr: 10.128.0.0/14
  operatorConfiguration:
    clusterNetworkOperator:
      ovnKubernetesConfig:
        ipv4:
          internalJoinSubnet: "100.99.0.0/16"
          internalTransitSwitchSubnet: "100.69.0.0/16"
```


where: 

`metadata`
     Specifies the name of the hosted cluster and the name of the hosted control plane namespace. 
`spec.operatorConfiguration.clusterNetworkOperator.ovnKubernetesConfig.ipv4`
     Specifies the subnets to use. Both subnet fields in this section must be in a valid IPv4 CIDR notation, such as `192.168.1.0/24`. The prefix range is `/0` to `/30`, inclusive. The first octet cannot be 0, and the string length must be 9-18 characters. The subnet fields cannot use the same value. The subnet must be large enough to accommodate one IP address per node in the cluster. When you plan subnet size, consider future cluster growth. If you omit these fields, the default value for the `internalJoinSubnet` field is `100.64.0.0/16`, and the default value for the `internalTransitSwitchSubnet` field is `100.88.0.0/16`. 

For full details about creating a hosted cluster, see "Creating a hosted cluster by using the CLI". 

  * To configure internal OVN subnets in an existing hosted cluster, enter the following command: 

```shell-session
$ oc patch hostedcluster <hosted_cluster_name> \
  -n <hosted_control_plane_namespace> \
  --type=merge \
  -p '{
    "spec": {
      "operatorConfiguration": {
        "clusterNetworkOperator": {
          "ovnKubernetesConfig": {
            "ipv4": {
              "internalJoinSubnet": "100.99.0.0/16",
              "internalTransitSwitchSubnet": "100.69.0.0/16"
            }
          }
        }
      }
    }
  }'
```


where: 

`spec.operatorConfiguration.clusterNetworkOperator.ovnKubernetesConfig.ipv4`
    

Specifies the subnets to use. Both subnet fields in this section must be in a valid IPv4 CIDR notation, such as `192.168.1.0/24`. The prefix range is `/0` to `/30`, inclusive. The first octet cannot be 0, and the string length must be 9-18 characters. The subnet fields cannot use the same value. The subnet must be large enough to accommodate one IP address per node in the cluster. When you plan subnet size, consider future cluster growth. If you omit these fields, the default value for the `internalJoinSubnet` field is `100.64.0.0/16`, and the default value for the `internalTransitSwitchSubnet` field is `100.88.0.0/16`. 

Important

When you make this change to an existing hosted cluster, the `ovnkube-node` DaemonSet is rolled out and the OVN components on compute nodes are restarted. During this process, you might experience brief network disruptions. 




**Verification**

  1. Verify that the hosted configuration is correct by entering the following command: 

```shell-session
$ oc get hostedcluster <hosted_cluster_name> -n <hosted_control_plane_namespace> \
  -o jsonpath='{.spec.operatorConfiguration.clusterNetworkOperator.ovnKubernetesConfig}' | jq .
```


**Example output**

```shell-session
{
  "ipv4": {
    "internalJoinSubnet": "100.99.0.0/16",
    "internalTransitSwitchSubnet": "100.69.0.0/16"
  }
}
```


  2. Check the Network Operator configuration in the hosted cluster: 

     1. Extract the hosted cluster kubeconfig file by entering the following command: 

```shell-session
$ oc extract secret/<hosted_cluster_name>-admin-kubeconfig \
  -n <hosted_control_plane_namespace> --to=- > <hosted_cluster_kubeconfig_file>
```


     2. Verify the Network Operator configuration by entering the following command: 

```shell-session
$ oc get network.operator.openshift.io cluster \
  --kubeconfig=<hosted_cluster_kubeconfig_file> \
  -o jsonpath='{.spec.defaultNetwork.ovnKubernetesConfig.ipv4}' | jq .
```


**Example output**

```shell-session
{
  "internalJoinSubnet": "100.99.0.0/16",
  "internalTransitSwitchSubnet": "100.69.0.0/16"
}
```


  3. Create 2 test pods by completing the following steps: 

     1. In node 1, create pod 1, as shown in the following example: 

```yaml
kind: Pod
apiVersion: v1
  metadata:
    name: "<pod_1>"
    namespace: "<hosted_control_plane_namespace>"
    labels:
      name: <pod_name>
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
    - image: "<image_url>"
      name: <pod_name>
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
    nodeName: "${NODE1}"
```


     2. In node 2, create pod 2, as shown in the following example: 

```yaml
kind: Pod
apiVersion: v1
  metadata:
    name: "<pod_2>"
    namespace: "<hosted_control_plane_namespace>"
    labels:
      name: <pod_name>
  spec:
    securityContext:
      runAsNonRoot: true
      seccompProfile:
        type: RuntimeDefault
    containers:
    - image: "<image_url>"
      name: <pod_name>
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
    nodeName: "${NODE2}"
```


  4. Create a test service that backs up both pods, as shown in the following example: 

```yaml
kind: Service
apiVersion: v1
  metadata:
    name: "<test_service_name"
    namespace: "<hosted_control_plane_namespace>"
    labels:
      name: test-service
  spec:
    internalTrafficPolicy: "Cluster"
    externalTrafficPolicy: ""
    ipFamilyPolicy: "SingleStack"
    ports:
    - name: http
      port: <service_test_port_number>
      protocol: "TCP"
      targetPort: 8080
    selector:
      name: "<pod_name>"
    type: "ClusterIP"
```


  5. Verify that the OVN pods are running: 

     1. Enter the following command: 

```shell-session
$ oc rollout status daemonset/ovnkube-node \
  -n openshift-ovn-kubernetes \
  --kubeconfig=<hosted_cluster_kubeconfig_file> \
  --timeout=5m
```


     2. Enter the following command: 

```shell-session
$ oc get pods -n openshift-ovn-kubernetes --kubeconfig=<hosted_cluster_kubeconfig_file>
```


All `ovnkube-node` pods should be in `Running` state with all containers ready. 

  6. Make sure that the changes synchronized to the Network Operator by entering the following command: 

```shell-session
$ oc get network.operator.openshift.io/cluster \
  -ojsonpath='{.spec.defaultNetwork.ovnKubernetesConfig.ipv4}' \
  --kubeconfig=<clusters-hostedclustername> | jq .
```


  7. Get the IP address of pod 2 and transfer it from pod 1: 

     1. Enter the following command: 

```shell-session
$ pod2_ip=oc get pod -n e2e-test-networking-ovnkubernetes-xxt8s <pod_2> -o=jsonpath={.status.podIPs[0].ip}
```


     2. Enter the following command: 

```shell-session
$ oc exec <pod_1> -- /bin/sh -x -c curl --connect-timeout 5 -s <pod2_ip>:8080
```


  8. Get the service IP address and verify that the pod can be visited externally from a service: 

     1. Enter the following command: 

```shell-session
$ SERVICE_IP=oc get service test-service-o=jsonpath={.spec.clusterIPs[0]}
```


     2. Enter the following command: 

```shell-session
$ oc exec <pod_1> -- /bin/sh -x -c curl --connect-timeout 5 -s $SERVICE_IP:<service_test_port_number>
```


**Additional resources**

  * [Troubleshooting internal subnets for hosted clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-troubleshooting#hcp-ts-internal-subnets_hcp-troubleshooting "15.9. Known limitations for internal subnets for hosted clusters")
  * [Creating a hosted cluster by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/deploying-hosted-control-planes#hcp-bm-hc_hcp-deploy-bm "4.3.6.1. Creating a hosted cluster by using the CLI")
