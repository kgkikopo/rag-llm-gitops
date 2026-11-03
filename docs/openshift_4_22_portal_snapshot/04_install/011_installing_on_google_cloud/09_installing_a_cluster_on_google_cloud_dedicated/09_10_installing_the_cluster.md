# 9.10. Installing the cluster

To deploy OpenShift Container Platform in a sovereign cloud environment with strict data isolation, you can install a cluster on Google Cloud Dedicated by configuring and running the installation program. 

**Prerequisites**

  * You prepared your GCD environment. 
  * You obtained the OpenShift Container Platform installation program. 
  * You obtained the pull secret for your cluster. 
  * You obtained your GCD region name and custom API endpoints from your local operating partner, such as Thales. 



**Procedure**

  1. Create an `install-config.yaml` file. You can generate a template file by running the following command or manually create the file: 

```shell-session
$ ./openshift-install create install-config --dir <installation_directory>
```


Replace `<installation_directory>` with the name of the directory that contains the installation files for your cluster. 

Note

You cannot select a GCD sovereign cloud region by using the guided terminal prompts. You must manually edit the `install-config.yaml` file to configure GCD-specific parameters. 

  2. Edit the `install-config.yaml` file to configure it for your GCD environment: 

Note

The installation program automatically detects the GCD sovereign cloud environment based on the region and the domain-scoped project ID in your credential file. You do not need to manually configure API endpoints. 

     1. Specify the GCD region: 

```yaml
platform:
  gcp:
    region: <gcd_region_name>
```


     2. Configure the cluster for private networking: 

```yaml
publish: Internal
```


where: 

`publish`
     Specifies the cluster publishing strategy. For GCD, you must use `Internal`. Public clusters are not supported. 

     3. Optional: If you need to provide a custom Red Hat Enterprise Linux CoreOS (RHCOS) image, add the compute platform image field: 

```yaml
platform:
  gcp:
    defaultMachinePlatform:
      osImage:
        project: <project_id>
        name: <image_name>
```


where: 

`platform.gcp.defaultMachinePlatform.osImage.project`
     Specifies the Google Cloud project ID where your custom RHCOS image is stored. 
`platform.gcp.defaultMachinePlatform.osImage.name`
    

Specifies the name of your custom RHCOS image. 

Important

You must specify a custom RHCOS image. The RHCOS image is not pre-published in GCD regions. If you do not provide the `osImage.name` and `osImage.project` fields, the installation fails. 

     4. Optional: Configure Customer-Managed Encryption Keys (CMEK) if required for regulatory compliance: 

Important

When you use CMEK with GCD, you must use regional keys. Global keys are not supported. 

```yaml
platform:
  gcp:
    defaultMachinePlatform:
      osDisk:
        encryptionKey:
          kmsKey:
            name: <regional_key_name>
            keyRing: <key_ring_name>
            location: <region_name>
            projectID: <project_id>
```


where: 

`platform.gcp.defaultMachinePlatform.osDisk.encryptionKey.kmsKey.name`
     Specifies a regional KMS key, not a global key. 

     5. Configure storage to use `hyperdisk-balanced` storage: 

```yaml
platform:
  gcp:
    defaultMachinePlatform:
      osDisk:
        diskType: hyperdisk-balanced
```


where: 

`platform.gcp.defaultMachinePlatform.osDisk.diskType`
     Specifies the disk type for machine storage. GCD supports only `hyperdisk-balanced` storage. Other disk types are not available. 

  3. Back up the `install-config.yaml` file by running the following command: 

```shell-session
$ cp <installation_directory>/install-config.yaml <installation_directory>/install-config.yaml.backup
```


Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up. 

  4. Generate the Kubernetes manifests for the cluster by running the following command: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


  5. Deploy the OpenShift Container Platform cluster by running the following command: 

```shell-session
$ ./openshift-install create cluster --dir <installation_directory> --log-level=info
```


Note

If you provided correct configuration values, the cluster creation process should complete successfully. However, the installation program might fail if it cannot validate your custom API endpoints or if there are connectivity issues with your GCD environment. 

When the cluster deployment is complete, the installation program displays information about accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user. 

To verify that the cluster Operators are running, set the `KUBECONFIG` environment variable and check the cluster Operator status by running the following commands: 

```shell-session
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
```


```shell-session
$ oc get clusteroperators
```


Verify that all cluster Operators show `AVAILABLE=True`, `PROGRESSING=False`, and `DEGRADED=False`.
