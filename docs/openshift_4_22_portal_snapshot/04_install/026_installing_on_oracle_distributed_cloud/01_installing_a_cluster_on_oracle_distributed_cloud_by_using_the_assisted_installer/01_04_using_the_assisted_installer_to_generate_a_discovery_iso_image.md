# 1.4. Using the Assisted Installer to generate a discovery ISO image

Create the cluster configuration and generate the discovery ISO image in the Assisted Installer web console. 

## 1.4.1. Creating the cluster

To begin creating the cluster, set the cluster details. 

**Prerequisites**

  * You created a child compartment and an object storage bucket on Oracle Distributed Cloud. For details, see _Preparing the Oracle Distributed Cloud environment_. 
  * You reviewed details about the OpenShift Container Platform installation and update processes. 



**Procedure**

  1. Log in to the [Assisted Installer web console](https://console.redhat.com/) with your credentials. 
  2. In the **Red Hat OpenShift** tile, select **OpenShift**. 
  3. In the **Red Hat OpenShift Container Platform** tile, select **Create Cluster**. 
  4. On the **Cluster Type** page, scroll down to the end of the **Cloud** tab, and select **Oracle Cloud Infrastructure (virtual machines)**. 
  5. On the **Create an OpenShift Cluster** page, select the **Interactive** tile. 
  6. On the **Cluster Details** page, complete the following fields: 

Field| Action required  
---|---  
**Cluster name** |  Specify the name of your cluster, such as `oci`. This is the same value as the cluster name in Oracle Distributed Cloud.   
**Base domain** |  Specify the base domain of the cluster, such as `openshift-demo.devcluster.openshift.com`.  This must be the same value as the zone DNS server in Oracle Distributed Cloud.   
**OpenShift version** |  * For installations on virtual machines only, specify `OpenShift 4.14` or a later version.  * For installations that include bare metal machines, specify `OpenShift 4.16` or a later version.   
**CPU architecture** |  Specify `x86_64` or `Arm64`.   
**Integrate with external partner platforms** |  Specify `Oracle Cloud Infrastructure`.  After you specify this value, the **Include custom manifests** checkbox is selected by default and the **Custom manifests** page is added to the wizard.   
Show more

  7. Leave the default settings for the remaining fields, and click **Next**. 
  8. On the **Operators** page, click **Next**. 



## 1.4.2. Generating the Discovery ISO image

After setting cluster details, generate and download the Discovery ISO image. 

**Procedure**

  1. On the **Host Discovery** page, click **Add hosts** and complete the following steps: 

     1. For the **Provisioning type** field, select **Minimal image file**. 
     2. For the **SSH public key** field, add the SSH public key from your local system, by copying the output of the following command: 

```shell-session
$ cat ~/.ssh/id_rsa.put
```


The SSH public key will be installed on all OpenShift Container Platform control plane and compute nodes. 

     3. Click **Generate Discovery ISO** to generate the discovery ISO image file. 
     4. Click **Download Discovery ISO** to save the file to your local system. 




**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Configuring your firewall](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
