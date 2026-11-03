# 15.9. Known limitations for internal subnets for hosted clusters

Several known limitations exist for internal subnets on hosted clusters. 

  * IPv6 subnets are not supported. 
  * The hosted control planes command-line interface, `hcp`, might not have native flags for the subnet fields. Manual YAML editing or `oc patch` is required. 
  * Modifying OVN subnets after you create a cluster triggers a rollout of OVN components, which might cause brief network disruptions. 
  * You cannot modify OVN subnet configuration while a cluster update is in progress or scheduled. 



## 15.9.1. Configuring the ovnKubernetesConfig object fails with an error

When you try to configure the `ovnKubernetesConfig` object on a hosted cluster by using a different network type, such as `OpenShiftSDN`, an error occurs because hosted control planes works only with the `OVNKubernetes` network type. 

**Procedure**

  * Verify the network type of your hosted cluster by entering the following command: 

```shell-session
$ oc get hostedcluster <hosted_cluster_name> -n <hosted_control_plane_namespace> \
  -o jsonpath='{.spec.networking.networkType}'
```


## 15.9.2. Setting CIDR values in internal subnet fields

If the `internalJoinSubnet` field and the `internalTransitSwitchSubnet` field are set to the same classless inter-domain routing (CIDR) values, an error occurs. 

**Procedure**

  * Use different subnets for each field, as shown in the following example: 

```yaml
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  # ...
spec:
  #...
  operatorConfiguration:
    clusterNetworkOperator:
      ovnKubernetesConfig:
        ipv4:
          internalJoinSubnet: "100.99.0.0/16"
          internalTransitSwitchSubnet: "100.69.0.0/16"
# ...
```


## 15.9.3. Ensuring a valid IPv4 CIDR format

If you do not specify subnets in a valid classless inter-domain range (CIDR) format, an error occurs. 

**Procedure**

  * Ensure that the CIDR format follows the following format: 

```plaintext
X.X.X.X/Y
```


where: 

`X`
     is a value from `0` to `255`. The first octet must not be `0`. 
`Y`
    

is a value from `0` to `30`. 

**Valid examples**

```plaintext
100.99.0.0/16
192.168.1.0/24
```


**Invalid examples**

```plaintext
100.99.0.0
256.1.1.0/16
0.99.0.0/16
```


## 15.9.4. Avoiding an overlap between OVN subnets and CIDR values

If the configured OVN subnets overlap with the machine classless inter-domain routing (CIDR), service CIDR, cluster network CIDR, or with each other, an error occurs. 

**Procedure**

  * Use subnets that do not overlap with any network CIDR. You can use a CIDR calculator to verify that no overlaps exist. 

**Example of configuration with no overlaps**

```yaml
spec:
  networking:
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


## 15.9.5. Resolving a stuck OVN rollout

After you change an existing configuration, the OVN component rollout might take a long time or encounter issues. 

**Procedure**

  1. Check the status of the `ovnkube-node` DaemonSet rollout by entering the following command: 

```shell-session
$ oc rollout status daemonset/ovnkube-node \
  -n openshift-ovn-kubernetes \
  --kubeconfig=hosted-kubeconfig
```


  2. Check the pod logs for errors by entering the following command: 

```shell-session
$ oc logs -n openshift-ovn-kubernetes \
  -l app=ovnkube-node \
  --kubeconfig=hosted-kubeconfig
```


If the rollout is stuck, you might need to revert the configuration change.
