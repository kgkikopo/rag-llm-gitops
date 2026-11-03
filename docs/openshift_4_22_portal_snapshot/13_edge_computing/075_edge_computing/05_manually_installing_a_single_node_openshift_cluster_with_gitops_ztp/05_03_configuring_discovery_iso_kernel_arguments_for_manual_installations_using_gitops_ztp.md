# 5.3. Configuring Discovery ISO kernel arguments for manual installations using GitOps ZTP

The GitOps Zero Touch Provisioning (ZTP) workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. 

This is useful for cluster installations with specific environmental requirements. For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation. In OpenShift Container Platform 4.22, you can only add kernel arguments. You can not replace or delete kernel arguments. 

**Prerequisites**

  * You have installed the OpenShift CLI (oc). 
  * You have logged in to the hub cluster as a user with cluster-admin privileges. 
  * You have applied a `ClusterInstance` CR to the hub cluster. 



**Procedure**

  1. Edit the `spec.kernelArguments` specification in the `InfraEnv` CR to configure kernel arguments: 

```yaml
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  name: <cluster_name>
  namespace: <cluster_name>
spec:
  kernelArguments:
    - operation: append
      value: audit=0
    - operation: append
      value: trace=1
  clusterRef:
    name: <cluster_name>
    namespace: <cluster_name>
  pullSecretRef:
    name: pull-secret
```


where: 

`operation`
     Specify the `append` operation to add a kernel argument. 
`value`
     Specify the kernel argument you want to configure. This example configures the `audit` kernel argument and the `trace` kernel argument. 

Note

The `ClusterInstance` CR generates the `InfraEnv` resource as part of the day-0 installation CRs. 




**Verification**

To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file. 

  1. Begin an SSH session with the target host: 

```shell-session
$ ssh -i /path/to/privatekey core@<host_name>
```


  2. View the system’s kernel arguments by using the following command: 

```shell-session
$ cat /proc/cmdline
```
