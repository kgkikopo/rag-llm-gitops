# 22.2. Implement worker latency profiles at cluster creation

During cluster creation, you can implement worker latency profiles so that you can control the reaction of the cluster to latency issues without relying on manual methods to determine the best values. 

Important

To edit the configuration of the installation program, first use the command `openshift-install create manifests` to create the default node manifest and other manifest YAML files. This file structure must exist before you can add `workerLatencyProfile`. The platform on which you are installing might have varying requirements. Refer to the Installing section of the documentation for your specific platform. 

**Procedure**

  1. Create the manifest that is needed to build the cluster by using a folder name appropriate for your installation. 
  2. Create a YAML file to define `config.node`. The file must be in the `manifests` directory. 
  3. When defining `workerLatencyProfile` in the manifest for the first time, specify any of the profiles at cluster creation time: `Default`, `MediumUpdateAverageReaction` or `LowUpdateSlowReaction`. 



**Verification**

  * View the manifest file by running the following command. The output of the command should show the creation of the `spec.workerLatencyProfile` `Default` value in the manifest file. 

```shell-session
$ openshift-install create manifests --dir=<cluster_install_dir>
```


  * `<cluster_install_dir>`: Specifies the directory where you installed your cluster. 
  * Edit the manifest and add the value by entering the following command. The following example command uses the `vi` editor to show an example manifest file with the "Default" `workerLatencyProfile` value added. 

```shell-session
$ vi <cluster_install_dir>/manifests/config-node-default-profile.yaml
```


  * `<cluster_install_dir>`: Specifies the directory where you installed your cluster. 

**Example output**

```yaml
apiVersion: config.openshift.io/v1
kind: Node
metadata:
name: cluster
spec:
workerLatencyProfile: "Default"
# ...
```
