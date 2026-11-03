# 2.5. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on IBM PowerVC. 

**Prerequisites**

  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 



**Procedure**

  1. Create the `install-config.yaml` file. 

     1. Change to the directory that contains the installation program and run the following command: 

```shell-session
$ ./openshift-install create install-config --dir <installation_directory>
```


        * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates. 

When specifying the directory: 

        * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory. 
        * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

     2. At the prompts, provide the configuration details for your cloud: 

        1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

        2. Enter a descriptive name for your cluster. 

  2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section. 
  3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 




## 2.5.1. Installation configuration for a cluster on IBM PowerVC with a user-managed load balancer

The `install-config.yaml` parameters required to deploy an OpenShift Container Platform cluster on IBM PowerVC using an external, user-managed load balancer help you configure networking, compute, and platform settings for this setup. 

The following example `install-config.yaml` file demonstrates this configuration. 

Important

This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program. 

```yaml
apiVersion: v1
baseDomain: mydomain.test
compute:
- architecture: ppc64le
  hyperthreading: Enabled
  name: worker
  platform:
    powervc:
      zones:
        - powervc-sample-project
  replicas: 3
controlPlane:
  architecture: ppc64le
  name: master
  platform:
    powervc:
      zones:
        - s1122
  replicas: 3
metadata:
  creationTimestamp: null
  name: ocp-on-powervc
networking:
  clusterNetwork:
  - cidr: 10.100.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.100.32.0/20
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  powervc:
    apiVIPs:
    - 10.20.188.52
    cloud: powervc
    clusterOSImage: my-rhcos-image
    defaultMachinePlatform:
      type: my-powervc-project
    ingressVIPs:
    - 10.20.188.52
    controlPlanePort:
      fixedIPs:
        - subnet:
            id: ae643a65-d0fc-4408-90c6-a820340bfade
```


  * `apiVIPs`: Specifies the address of the user-managed load balancer. 
  * `ingressVIPs`: Specifies the address of the user-managed load balancer. 
  * `controlPlanePort.fixedIPs.subnet.id`: Specifies the subnet that is served by the user-managed DHCP server. 



**Additional resources**

  * [Installation configuration parameters for IBM PowerVC](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_powervc/installation-config-parameters-ibm-powervc "Chapter 3. Installation configuration parameters for IBM PowerVC")
