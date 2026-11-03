# 15.4. Troubleshoot hosted clusters on OpenShift Virtualization

When you troubleshoot a hosted cluster on OpenShift Virtualization, start with the top-level `HostedCluster` and `NodePool` resources and then work down the stack until you find the root cause. The following steps can help you discover the root cause of common issues. 

## 15.4.1. Troubleshooting HostedCluster resource stuck in a partial state

If a hosted control plane is not coming fully online because a `HostedCluster` resource is pending, identify the problem by checking prerequisites, resource conditions, and node and Operator status. 

**Procedure**

  * Ensure that you meet all of the prerequisites for a hosted cluster on OpenShift Virtualization. 
  * View the conditions on the `HostedCluster` and `NodePool` resources for validation errors that prevent progress. 
  * By using the `kubeconfig` file of the hosted cluster, inspect the status of the hosted cluster: 

    * View the output of the `oc get clusteroperators` command to see which cluster Operators are pending. 
    * View the output of the `oc get nodes` command to ensure that worker nodes are ready. 




## 15.4.2. Identifying why no compute nodes are registered

If a hosted control plane is not coming fully online because the hosted control plane has no compute nodes registered, identify the problem by checking the status of various parts of the hosted control plane. 

**Procedure**

  * View the `HostedCluster` and `NodePool` conditions for failures that indicate what the problem might be. 
  * Enter the following command to view the KubeVirt compute node virtual machine (VM) status for the `NodePool` resource: 

```shell-session
$ oc get vm -n <namespace>
```


  * If the VMs are stuck in the provisioning state, enter the following command to view the CDI import pods within the VM namespace for clues about why the importer pods have not completed: 

```shell-session
$ oc get pods -n <namespace> | grep "import"
```


  * If the VMs are stuck in the starting state, enter the following command to view the status of the virt-launcher pods: 

```shell-session
$ oc get pods -n <namespace> -l kubevirt.io=virt-launcher
```


If the virt-launcher pods are in a pending state, investigate why the pods are not being scheduled. For example, not enough resources might exist to run the virt-launcher pods. 

  * If the VMs are running but they are not registered as compute nodes, use the web console to gain VNC access to one of the affected VMs. The VNC output indicates whether the ignition configuration was applied. If a VM cannot access the hosted control plane ignition server on startup, the VM cannot be provisioned correctly. 
  * If the ignition configuration was applied but the VM is still not registering as a node, see "Identifying the problem: Access the VM console logs" to learn how to access the VM console logs during startup. 



**Additional resources**

  * [Identifying the problem: Access the VM console logs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.11/html/clusters/cluster_mce_overview#identifying-vm-console-logs)



## 15.4.3. Identifying why compute nodes are not ready

During cluster creation, nodes enter the `NotReady` state temporarily while the networking stack is rolled out. This part of the process is normal. However, if this part of the process takes longer than 15 minutes, identify the problem by investigating the node object and pods. 

**Procedure**

  1. Enter the following command to view the conditions on the node object and determine why the node is not ready: 

```shell-session
$ oc get nodes -o yaml
```


  2. Enter the following command to look for failing pods within the cluster: 

```shell-session
$ oc get pods -A --field-selector=status.phase!=Running,status,phase!=Succeeded
```


## 15.4.4. Identifying why ingress and console cluster Operators are not coming online

If a hosted control plane is not coming fully online because the Ingress and console cluster Operators are not online, check the wildcard DNS routes and load balancer. 

**Procedure**

  * If the cluster uses the default Ingress behavior, enter the following command to ensure that wildcard DNS routes are enabled on the OpenShift Container Platform cluster that the virtual machines (VMs) are hosted on: 

```shell-session
$ oc patch ingresscontroller -n openshift-ingress-operator \
  default --type=json -p \
  '[{ "op": "add", "path": "/spec/routeAdmission", "value": {wildcardPolicy: "WildcardsAllowed"}}]'
```


  * If you use a custom base domain for the hosted control plane, complete the following steps: 

    * Ensure that the load balancer is targeting the VM pods correctly. 
    * Ensure that the wildcard DNS entry is targeting the load balancer IP address. 




## 15.4.5. Identifying why load balancer services for the hosted cluster are unavailable

If a hosted control plane is not coming fully online because the load balancer services are not becoming available, check events, details, and the Kubernetes Cluster Configuration Manager (KCCM) pod. 

**Procedure**

  * Look for events and details that are associated with the load balancer service within the hosted cluster. 
  * By default, load balancers for the hosted cluster are handled by the kubevirt-cloud-controller-manager within the hosted control plane namespace. Ensure that the KCCM pod is online and view its logs for errors or warnings. To identify the KCCM pod in the hosted control plane namespace, enter the following command: 

```shell-session
$ oc get pods -n <hosted_control_plane_namespace> \
  -l app=cloud-controller-manager
```


## 15.4.6. Identifying why hosted cluster PVCs are not available

If a hosted control plane is not coming fully online because the persistent volume claims (PVCs) for a hosted cluster are not available, check the PVC events and details, and component logs. 

**Procedure**

  * Look for events and details that are associated with the PVC to understand which errors are occurring. 
  * If a PVC is failing to attach to a pod, view the logs for the kubevirt-csi-node `daemonset` component within the hosted cluster to further investigate the problem. To identify the kubevirt-csi-node pods for each node, enter the following command: 

```shell-session
$ oc get pods -n openshift-cluster-csi-drivers -o wide \
  -l app=kubevirt-csi-driver
```


  * If a PVC cannot bind to a persistent volume (PV), view the logs of the kubevirt-csi-controller component within the hosted control plane namespace. To identify the kubevirt-csi-controller pod within the hosted control plane namespace, enter the following command: 

```shell-session
$ oc get pods -n <hcp namespace> -l app=kubevirt-csi-driver
```


## 15.4.7. Identifying why VM nodes are not joining the cluster

If a hosted control plane is not coming fully online because the virtual machine (VM) nodes are not correctly joining the cluster, access the VM console logs. 

**Procedure**

  * To access the VM console logs, complete the steps in "How to get serial console logs for VMs part of OpenShift Virtualization Hosted Control Plane clusters". 



**Additional resources**

  * [How to get serial console logs for VMs part of OpenShift Virtualization Hosted Control Plane clusters (Red Hat Knowledgebase)](https://access.redhat.com/solutions/7037705)



## 15.4.8. Resolving RHCOS image mirroring failures

For hosted control planes on OpenShift Virtualization in a disconnected environment, if `oc-mirror` fails to automatically mirror the Red Hat Enterprise Linux CoreOS (RHCOS) image to the internal registry, you can manually mirror the RHCOS image to the internal registry. 

When you create your first hosted cluster, the Kubevirt virtual machine does not boot, because the boot image is not available in the internal registry. 

To resolve this issue, manually mirror the RHCOS image to the internal registry. 

**Procedure**

  1. Get the internal registry name by running the following command: 

```shell-session
$ oc get imagecontentsourcepolicy -o json \
  | jq -r '.items[].spec.repositoryDigestMirrors[0].mirrors[0]'
```


  2. Get a payload image by running the following command: 

```shell-session
$ oc get clusterversion version -ojsonpath='{.status.desired.image}'
```


  3. Extract the `0000_50_installer_coreos-bootimages.yaml` file that contains boot images from your payload image on the hosted cluster. Replace `<payload_image>` with the name of your payload image. Run the following command: 

```shell-session
$ oc image extract \
  --file /release-manifests/0000_50_installer_coreos-bootimages.yaml \
  <payload_image> --confirm
```


  4. Get the RHCOS image by running the following command: 

```shell-session
$ cat 0000_50_installer_coreos-bootimages.yaml | yq -r .data.stream \
  | jq -r '.architectures.x86_64.images.kubevirt."digest-ref"'
```


  5. Mirror the RHCOS image to your internal registry by running the following command: 

```shell-session
$ oc image mirror <rhcos_image> <internal_registry>
```


     * Replace `<rhcos_image>` with your RHCOS image; for example, `quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:d9643ead36b1c026be664c9c65c11433c6cdf71bfd93ba229141d134a4a6dd94`. 
     * Replace `<internal_registry>` with the name of your internal registry; for example, `virthost.ostest.test.metalkube.org:5000/localimages/ocp-v4.0-art-dev`. 

  6. Create a YAML file named `rhcos-boot-kubevirt.yaml` that defines the `ImageDigestMirrorSet` object. See the following example configuration: 

```yaml
apiVersion: config.openshift.io/v1
kind: ImageDigestMirrorSet
metadata:
  name: rhcos-boot-kubevirt
spec:
  repositoryDigestMirrors:
    - mirrors:
        - virthost.ostest.test.metalkube.org:5000/localimages/ocp-v4.0-art-dev
      source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```


     * `spec.repositoryDigestMirrors.mirrors` specifies the name of your internal registry. 
     * `spec.repositoryDigestMirrors.source` specifies your RHCOS image without its digest. 

  7. Apply the `rhcos-boot-kubevirt.yaml` file to create the `ImageDigestMirrorSet` object by running the following command: 

```shell-session
$ oc apply -f rhcos-boot-kubevirt.yaml
```


## 15.4.9. Returning non-bare-metal clusters to the late binding pool

If you are using late binding managed clusters without `BareMetalHosts`, you must complete additional manual steps to delete a late binding cluster and return the nodes back to the Discovery ISO. 

For late binding managed clusters without `BareMetalHosts`, removing cluster information does not automatically return all nodes to the Discovery ISO. 

To unbind the non-bare-metal nodes with late binding, complete the following steps. 

**Procedure**

  1. Remove the cluster information. For more information, see "Removing a cluster from management". 
  2. Clean the root disks. 
  3. Reboot manually with the Discovery ISO. 



**Additional resources**

  * [Removing a cluster from management](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/clusters/cluster_mce_overview#remove-managed-cluster)
