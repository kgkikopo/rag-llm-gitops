# 4.13. Specifying advanced network configuration

You can use advanced network configuration for your OpenShift Container Platform network plugin to integrate your cluster into your existing network environment. 

You can specify advanced network configuration only before you install the cluster. 

Important

Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported. 

**Prerequisites**

  * You have created the `install-config.yaml` file and completed any modifications to it. 



**Procedure**

  1. Change to the directory that contains the installation program and create the manifests: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


where `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster. 

  2. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
```


  3. Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example: 

The following example enables IPsec for the OVN-Kubernetes network provider: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      ipsecConfig:
        mode: Full
```


  4. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program consumes the `manifests/` directory when you create the Ignition config files. 
  5. Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`: 

```shell-session
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
```


Because you create and manage these resources yourself, you do not have to initialize them. 

     * You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment.
