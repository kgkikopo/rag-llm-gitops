# 8.5. Manually updating the boot image on an IBM Cloud(R) cluster

For an IBM Cloud cluster, you can manually update the boot image for the compute nodes in your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly. 

Note

The standard boot image management feature is not supported for IBM Cloud clusters. 

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain IBM Cloud authentication credentials, download a boot image, upload that image to the IBM Cloud image service, and modify your compute machine sets to use the new boot image. 

This procedure uses the default IBM Cloud Cloud Object Storage (COS) bucket in your cluster, which was created during cluster installation. Each COS bucket has a specific Cloud Resource Name (CRN), which the IBM Cloud CLI uses the to select the correct COS bucket. The following procedure shows how to obtain the CRN for the default COS bucket. For more information on the CRN, see [Cloud Resource Names in the IBM Cloud documentation](https://cloud.ibm.com/docs/account?topic=account-crn). 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
  * You have the OpenShift CLI (`oc`) installed. 
  * You have the [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started) installed. 
  * You have installed the IBM Cloud Virtual Private Cloud (VPC) CLI plugin. 
  * You have installed the IBM Cloud Object Storage plugin. 



**Procedure**

  1. Obtain the resource group and region from the `infrastructure` object and set the values in an environment variable by running the following commands: 

```shell-session
$ export RESOURCE_GROUP=$(oc get infrastructure cluster -o jsonpath='{.status.infrastructureName}')
```


```shell-session
$ export REGION=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.ibmcloud.location}')
```


  2. Generate an IBM Cloud API key and log in to your IBM Cloud: 

     1. Follow the instructions in [Creating your IBM Cloud API key in the IBM Cloud](https://www.ibm.com/docs/en/masv-and-l/cd?topic=cli-creating-your-cloud-api-key) documentation to generate the API key. 

To ensure that the key has the appropriate permissions, you must use the same IBM Cloud account used to create the OpenShift Container Platform cluster when generating the key. 

     2. Set the API key in an environment variable by running the following command: 

```shell-session
$ export IBM_API_KEY=<Your_IBM_Cloud_API_Key>
```


     3. Log in to your IBM Cloud by running the following command: 

```shell-session
$ ibmcloud login --apikey ${IBM_API_KEY} -r ${REGION} -g ${RESOURCE_GROUP}
```


`IBM_API_KEY`, `REGION`, and `RESOURCE_GROUP` are environment variables you created in previous steps. 

**Example output**

```shell-session
API endpoint: https://cloud.ibm.com
Authenticating...
Retrieving API key token...
OK

Targeted account OpenShift-QE (xxxxxxxxxxxxxxxx) <-> xxxxxx

Targeted resource group xxxxxxx-ibm3h-9pbgg

Targeted region eu-gb


API endpoint:     https://cloud.ibm.com
Region:           eu-gb
User:             xxxxx
Account:          xxxxx
Resource group:   xxxxx
```


  3. Obtain the URL of the RHCOS image to use as the boot image and set the location in an environment variable by running one of the following commands, based on your cluster architecture: 

     * Linux (x86_64, amd64): 

```shell-session
$ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.ibmcloud.formats["qcow2.gz"].disk.location')
```


     * Linux on IBM Z® and IBM® LinuxONE (s390x): 

```shell-session
export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.s390x.artifacts.ibmcloud.formats["qcow2.gz"].disk.location')
```


  4. Obtain the boot image: 

     1. Download the image by using the following command: 

```shell-session
$ curl -L -o /tmp/rhcos-new.qcow2.gz "${RHCOS_URL}"
```


`RHCOS_URL` is the environment variable you created in a previous step. 

     2. Decompress the downloaded image by running the following command: 

```shell-session
$ gunzip /tmp/rhcos-new.qcow2.gz
```


  5. Upload the boot image to the default IBM Cloud Cloud Object Storage (COS) bucket: 

     1. Obtain the CRN for your COS bucket and set the CRN in an environment variable by running the following command: 

```shell-session
$ export COS_CRN=$(ibmcloud resource service-instance "${RESOURCE_GROUP}-cos" --output json | jq -r '.[0].crn')
```


     2. Optional: Check that the CRN is correct by running the following command: 

```shell-session
$ echo ${COS_CRN}
```


     3. Configure the default COS bucket with the CRN by running the following command: 

```shell-session
$ ibmcloud cos config crn --crn "${COS_CRN}"
```


`COS_CRN` is the environment variable you created in a previous step. 

     4. Upload the boot image to the COS bucket by running the following command: 

```shell-session
$ ibmcloud cos object-put --bucket "${RESOURCE_GROUP}-vsi-image" --key "rhcos-new.qcow2" --body /tmp/rhcos-new.qcow2 --region "${REGION}"
```


`RESOURCE_GROUP` and `REGION` are environment variables you created in previous steps. 

     5. Optional: Check that image was uploaded to the COS bucket by running the following command: 

```shell-session
$ ibmcloud cos objects --bucket "${RESOURCE_GROUP}-vsi-image" --region "${REGION}"
```


`RESOURCE_GROUP` and `REGION` are environment variables you created in previous steps. 

**Example output**

```shell-session
OK
Found 2 objects in bucket 'xxxxxx-ibm3h-9pbgg-vsi-image':
```


     6. Set an environment variable to create a descriptive name for your boot image: 

```shell-session
$ export IMAGE_NAME="<descriptive_image_name>"
```


Setting a descriptive name for your boot image, such as using the Red Hat Enterprise Linux CoreOS (RHCOS) version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future. 

     7. Create a custom image for your IBM Cloud Virtual Private Cloud (VPC) from the uploaded boot image by running one of the following commands, based on your cluster architecture: 

        * Linux (x86_64, amd64): 

```shell-session
$ ibmcloud is image-create "${RESOURCE_GROUP}-${IMAGE_NAME}" --file "cos://${REGION}/${RESOURCE_GROUP}-vsi-image/rhcos-new.qcow2" --os-name rhel-coreos-stable-amd64 --resource-group-name "${RESOURCE_GROUP}"
```


You must set the `--os-name` argument to `rhel-coreos-stable-amd64` as shown. This parameter configures several Red Hat Enterprise Linux CoreOS (RHCOS) default values that are required. 

`RESOURCE_GROUP`, `IMAGE_NAME`, and `REGION` are environment variables you created in previous steps. 

        * Linux on IBM Z® and IBM® LinuxONE (s390x): 

```shell-session
$ ibmcloud is image-create "${RESOURCE_GROUP}-${IMAGE_NAME}" --file "cos://${REGION}/${RESOURCE_GROUP}-vsi-image/rhcos-new.qcow2" --os-name red-8-s390x-byol --resource-group-name "${RESOURCE_GROUP}"
```


You must set the `--os-name` argument to `red-8-s390x-byol` as shown. This parameter configures several Red Hat Enterprise Linux CoreOS (RHCOS) default values that are required. 

`RESOURCE_GROUP`, `IMAGE_NAME`, and `REGION` are environment variables you created in previous steps. 

     8. Optional: Observe the new image being uploaded until its status changes from `pending` to `available`. 

```shell-session
$ watch ibmcloud is image "${RESOURCE_GROUP}-${IMAGE_NAME}"
```


`RESOURCE_GROUP` and `IMAGE_NAME` are environment variables you created in previous steps. 

  6. Update each of your compute machine sets to include the new boot image: 

     1. Obtain the name of your machine sets for use in the following step by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api
```


**Example output**

```shell-session
NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
```


     2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command: 

```shell-session
$ oc patch machineset <machineset-name> -n openshift-machine-api --type merge \
  -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":"'${RESOURCE_GROUP}'-'${IMAGE_NAME}'"}}}}}}'
```


Replace `<machineset_name>` with the name of your machine set. 

`IMAGE_NAME` is the environment variable you created in a previous step. 

  7. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version". 



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

     3. Verify that the new node has been created and is in the `Ready` state by running the following command. 

```shell-session
$ oc get nodes
```


     4. Verify that the new node is using the new boot image by running the following command: 

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

`<version>`
     Specifies the boot image version. 

After you migrate all machine sets to the new boot image, the old boot image is no longer needed. You can remove the old boot image from your COS bucket.
