# 1.5. Preparing the OCI image

Generate the OpenShift Container Platform ISO image in the Assisted Installer on the Red Hat portal. Then, convert the image to an Oracle Edge Cloud compatible image and upload it to the **Custom Images** page of your Oracle Edge Cloud environment. 

You can generate, convert and upload the image on your laptop and not on the bastion server or within environments such as Oracle Solution Center. 

## 1.5.1. Generating the image in the Assisted Installer

Create a cluster and download the discovery ISO image. 

**Procedure**

  1. Log in to [Assisted Installer web console](https://console.redhat.com/) with your credentials. 
  2. In the **Red Hat OpenShift** tile, select **OpenShift**. 
  3. In the **Red Hat OpenShift Container Platform** tile, select **Create Cluster**. 
  4. On the **Cluster Type** page, scroll to the end of the **Cloud** tab, and select **Oracle Cloud Infrastructure (virtual machines)**. 
  5. On the **Create an OpenShift Cluster** page, select the **Interactive** tile. 
  6. On the **Cluster Details** page, complete the following fields: 

Field| Action required  
---|---  
**Cluster name** |  Specify the name of your OpenShift Container Platform cluster. This name is the same name you used to create the resource via the Terraform scripts. The name must be between 1-54 characters. It can use lowercase alphanumeric characters or hyphen (-), but must start and end with a lowercase letter or a number.   
**Base domain** |  Specify the base domain of the cluster. This is the value used for the `zone_dns` variables in the Terraform scripts that run on Oracle® Edge Cloud. Make a note of the value.   
**OpenShift version** |  Select **OpenShift 4.16.20**. If it is not immediately visible, scroll to the end of the dropdown menu, select **Show all available versions** , and type the version in the search box.   
**Integrate with external partner platforms** |  Select **Oracle Cloud Infrastructure**.  After you specify this value, the **Include custom manifests** checkbox is selected by default and the **Custom manifests** page is added to the wizard.   
Show more

  7. Leave the default settings for the remaining fields, and click **Next**. 
  8. On the **Operators** page, click **Next**. 
  9. On the **Host Discovery** page, click **Add hosts** and complete the following steps: 

Note

The minimal ISO image is the mandatory **Provisioning type** for the Oracle Edge Cloud, and cannot be changed. 

     1. In the **SSH public key** field, add the SSH public key by copying the output of the following command: 

```shell-session
$ cat ~/.ssh/id_rsa.put
```


The SSH public key will be installed on all OpenShift Container Platform control plane and compute nodes. 

     2. Click the **Show proxy settings** checkbox. 
     3. Add the proxy variables from the `/etc/environment` file of the bastion server that you configured earlier: 

```shell-session
http_proxy=http://www-proxy.<your_domain>.com:80
https_proxy=http://www-proxy.<your_domain>.com:80
no_proxy=localhost,127.0.0.1,1,2,3,4,5,6,7,8,9,0,.<your_domain>.com
#(ie.oracle.com,.oraclecorp.com)
```


     4. Click **Generate Discovery ISO** to generate the discovery ISO image file. 

  10. Click **Download Discovery ISO** to save the file to your local system. After you download the ISO file, you can rename it as required, for example `discovery_image_<your_cluster_name>.iso`. 



## 1.5.2. Converting and uploading the image to Oracle Edge Cloud

Convert the ISO image to an Oracle Cloud Infrastructure (OCI) image and upload it to your Oracle Edge Cloud system from your OCI Home Region Object Store. 

**Procedure**

  1. Convert the image from ISO to OCI. 
  2. Upload the OCI image to an OCI bucket, and generate a Pre-Authenticated Request (PAR) URL. 
  3. Import the OCI image to the Oracle® Edge Cloud portal. 
  4. Copy the Oracle Cloud Identifier (OCID) of the image for use in the next procedure. 

For the full procedure, see step 6 - 8 in the "OpenShift Image Preparation" section of the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).
