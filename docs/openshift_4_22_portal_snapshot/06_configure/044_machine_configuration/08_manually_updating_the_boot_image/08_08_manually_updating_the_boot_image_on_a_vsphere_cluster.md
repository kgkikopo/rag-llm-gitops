# 8.8. Manually updating the boot image on a vSphere cluster

You can manually update the boot image for your VMware vSphere cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly. 

vSphere boot images use a template that you create by uploading a Red Hat Enterprise Linux CoreOS (RHCOS) OVA image to the vSphere vCenter. The template image is used by all machine sets as the boot image. Use the following procedure to identify the correct boot image to use as the new boot image, create the template from the image in vCenter, and modify your compute machine sets to use that template image. 

Note

For clusters that use a default RHCOS image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement". 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have installed the OpenShift CLI (`oc`). 
  * You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement". 
  * You have disabled boot image management for the cluster. For more information, see "Disabling boot image management". 
  * You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 



**Procedure**

  1. Obtain the latest boot image to use as the new boot image: 

     1. Obtain the name of the new boot image by running the following command: 

```shell-session
$ openshift-install coreos print-stream-json | jq '.architectures.x86_64.artifacts.vmware'
```


**Example output**

```shell-session
{
  "release": "9.6.20251023-0",
  "formats": {
    "ova": {
      "disk": {
        "location": "https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251023-0/x86_64/rhcos-9.6.20251023-0-vmware.x86_64.ova",
        "sha256": "14fa549bb83b2e730de22312419b503bc1ce85adf72269582f0af60e366d87ff"
      }
    }
  }
}
```


     2. Use the URL in the `location` field to download the image. 

  2. In the vSphere Client, create a template for the OVA image: 

     1. From the **Hosts and Clusters** tab, right-click your cluster name and select **Deploy OVF Template**. 
     2. On the **Select an OVF** tab, specify the name of the RHCOS OVA file that you downloaded. 
     3. On the **Select a name and folder** tab, set a **Virtual machine name** for your template, such as using the RHCOS version number in the image name. Click the name of your vSphere cluster and select the folder. 
     4. On the **Select a compute resource** tab, click the name of your vSphere cluster. 
     5. On the **Select storage** tab, configure the storage options for your VM. 

        * Select **Thin Provision** or **Thick Provision** , based on your storage preferences. 
        * Select the data store that you specified in your `install-config.yaml` file. 
        * If you want to encrypt your virtual machines, select **Encrypt this virtual machine**. See "Requirements for encrypting virtual machines" for more information. 

     6. On the **Select network** tab, specify the network that you configured for the cluster, if available. 
     7. When creating the OVF template, do not specify values on the **Customize template** tab or configure the template any further. 
     8. On the **Ready to complete** tab, verify your settings and click **Finish**. 

The vSphere Client uploads the boot image to create the OVF template. This can take a few minutes depending on network speeds. You can keep track of this process in the task tab under _Deploy OVF template_. 

     9. After the upload is complete, click the new virtual machine and click **Template** **Convert to template** **Yes**. 

You now have a VM template based on the new boot image, which you can use to update the machine set objects. 

  3. Update each of your compute machine sets to include the new boot image: 

     1. Obtain the name of your machine sets for use in the following step by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api
```


**Example output**

```shell-session
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-xw7zmyt-72292-x7nqv-worker-a   1         1         1       1           53m
```


     2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command: 

```shell-session
$ oc patch machineset <machineset-name> -n openshift-machine-api --type json \
  -p '[{"op": "replace", "path": "/spec/template/spec/providerSpec/value/template", "value": "ci-ln-6vjqx8t-c1627-bwxkr-rhcos-generated-region-generated-zone"}]'
```


Replace `<machineset_name>` with the name of your machine set. 

  4. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version". 



**Verification**

  1. Scale up a machine set to check that the new node is using the new boot image: 

     1. Increase the machine set replicas by one to trigger a new machine by running the following command: 

```shell-session
$ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
```


where: 

`<count>`
     Specifies the total number of replicas, including any existing replicas, that you want for this machine set. 
`<machineset_name>`
     Specifies the name of the machine set to scale. 

     2. Optional: View the status of the machine set as it provisions by running the following command: 

```shell-session
$ oc get machines.machine.openshift.io -n openshift-machine-api -w
```


It can take several minutes for the machine set to achieve the `Running` state. 

     3. Verify that the new node has been created and is in the `Ready` state by running the following command: 

```shell-session
$ oc get nodes
```


  2. Verify that the new node is using the new boot image by running the following command: 

```shell-session
$ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
```


Replace `<new_node>` with the name of your new node. 

**Example output**

```shell-session
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251212-1"
}
```


where: 

`version`
     Specifies the boot image version.
