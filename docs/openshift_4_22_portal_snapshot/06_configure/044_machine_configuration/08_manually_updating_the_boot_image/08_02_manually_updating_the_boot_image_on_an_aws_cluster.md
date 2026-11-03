# 8.2. Manually updating the boot image on an AWS cluster

You can manually update the boot image for your Amazon Web Services (AWS) cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly. 

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct Amazon Machine Image (AMI) to use as the new boot image, and modify your compute machine sets to use that image. 

The process differs for clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS) image and clusters that use a custom RHCOS image from the AWS Marketplace. The following procedure helps determine which type of image you use. 

Note

For clusters that use a default RHCOS image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement". 

**Prerequisites**

  * You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2). 
  * You have installed the OpenShift CLI (`oc`). 
  * You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement". 
  * You have disabled boot image management for the cluster. For more information, see "Disabling boot image management". 
  * You have installed the [AWS CLI](https://aws.amazon.com/cli/). 
  * You configured an AWS account to host the cluster. For information, see "Configuring an AWS account". 
  * For a cluster that uses a default RHCOS image, ensure you have met the following additional prerequisites: 

    * You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program." 
    * For a cluster that uses a default RHCOS image, you have installed the [`jq`](https://jqlang.org/) program. 




**Procedure**

  1. Determine if your cluster uses a default RHCOS image or a custom RHCOS image from the AWS Marketplace image: 

     1. Obtain the current AWS region where the cluster is installed and set the value in an environment variable by running the following command: 

```shell-session
$ export REGION=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}')
```


     2. Obtain the current Amazon Machine Image (AMI) ID for your region and set the value in an environment variable by running the following command: 

```shell-session
$ export CURRENT_AMI=$(oc get machineset -n openshift-machine-api -o jsonpath='{.items[0].spec.template.spec.providerSpec.value.ami.id}')
```


     3. Obtain the product ID for your AMI and set the value in an environment variable by running the following command: 

```shell-session
$ export PRODUCT_ID=$(aws ec2 describe-images --image-ids "$CURRENT_AMI" --region "$REGION" \
  --query 'Images[0].Name' --output text | \
  grep -oE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
```


`CURRENT_AMI` and `REGION` are environment variables you created in previous steps. 

     4. Display the contents of the `PRODUCT_ID` environment variable by running the following command: 

```shell-session
$ echo $PRODUCT_ID
```


        * If the output for the `PRODUCT_ID` environment variable is empty, as shown in the following example, your cluster uses a standard OpenShift Container Platform image. 

**Example with empty output**

```shell-session

```


        * If the output for the `PRODUCT_ID` environment variable is not empty, as shown in the following example, your cluster uses an AWS Marketplace image. 

**Example with non-empty output**

```shell-session
59ead7de-2540-4653-a8b0-fa7926d5c845
```


        * If the command returns an error, and you are unable to determine your cluster variant, contact Red Hat Support. If Red Hat Support determines that your cluster uses an AWS Marketplace image, you can set the `PRODUCT_ID` environment variable with the appropriate product ID from the following table. 

```shell-session
$ export PRODUCT_ID=<Product_ID_from_table>
```


Variant| Product ID  
---|---  
[OpenShift Container Platform on x86 - NA](https://aws.amazon.com/marketplace/procurement/?productId=59ead7de-2540-4653-a8b0-fa7926d5c845) |  `59ead7de-2540-4653-a8b0-fa7926d5c845`  
[OpenShift Kubernetes Engine on x86 - NA](https://aws.amazon.com/marketplace/procurement?productId=963b36c3-de6f-48ed-b802-2b38b2a2cdeb) |  `963b36c3-de6f-48ed-b802-2b38b2a2cdeb`  
[OpenShift Platform Plus on x86 - NA](https://aws.amazon.com/marketplace/procurement?productId=f5da01a6-d046-487c-9072-42fe53b1cad4) |  `f5da01a6-d046-487c-9072-42fe53b1cad4`  
[OpenShift Container Platform on ARM - NA](https://aws.amazon.com/marketplace/procurement?productId=abc249f8-7440-45f7-a4b1-c026baff64c1) |  `abc249f8-7440-45f7-a4b1-c026baff64c1`  
[OpenShift Kubernetes Engine on ARM - NA](https://aws.amazon.com/marketplace/procurement?productId=d2d3ebcd-c1ca-43d8-bf0a-530433200f35) |  `d2d3ebcd-c1ca-43d8-bf0a-530433200f35`  
[OpenShift Platform Plus on ARM - NA](https://aws.amazon.com/marketplace/procurement?productId=be6d3e94-c8dc-4a3e-9218-4b449b11f06f) |  `be6d3e94-c8dc-4a3e-9218-4b449b11f06f`  
[OpenShift Container Platform on x86 - EU, ME and Africa](https://aws.amazon.com/marketplace/procurement?productId=962791c7-3ae5-46d1-ba62-c7a5ebac54fd) |  `962791c7-3ae5-46d1-ba62-c7a5ebac54fd`  
[OpenShift Kubernetes Engine on x86 - EU, ME and Africa](https://aws.amazon.com/marketplace/procurement?productId=7026c8d7-392c-4010-b93c-f93f7bc5495f) |  `7026c8d7-392c-4010-b93c-f93f7bc5495f`  
[OpenShift Platform Plus on x86 - EU, ME and Africa](https://aws.amazon.com/marketplace/procurement?productId=628c9df3-0254-4f91-bc1f-8619d1b8eaa8) |  `628c9df3-0254-4f91-bc1f-8619d1b8eaa8`  
Show more

  2. Determine the AMI for the new boot image by using one of the following steps, depending upon the type of image used in your cluster: 

     * For a cluster that uses a default RHCOS image, perform the following steps: 

       1. Set an environment variable with your cluster architecture by running the following command: 

```shell-session
$ export ARCH=<architecture_type>
```


Replace `<architecture_type>` with one of the following values: 

          * Specify `aarch64` for the AArch64 or ARM64 architecture. 
          * Specify `ppc64le` for the IBM Power® (ppc64le) architecture. 
          * Specify `s390x` for the IBM Z® and IBM® LinuxONE (s390x) architecture. 
          * Specify `x86_64` for the x86_64 or AMD64 architecture. 

You can find the architecture as a label in any `MachineSet` object. 

**Example machine set with an architecture label**

```shell-session
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
# ...
```


       2. Obtain the AMI for the new boot image and set an environment variable with the AMI by running the following command: 

```shell-session
$ export AMI_ID=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.aws.regions.\"${REGION}\".image")
```


`ARCH` and `REGION` are environment variables you created in previous steps. 

       3. View the RHCOS version of the new boot image by running the following command: 

```shell-session
$ openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.aws.regions.\"${REGION}\".release"
```


**Example output**

```shell-session
9.6.20251212-1
```


Make note of the RHCOS version for later use. 

     * For a cluster that uses a custom RHCOS image, perform the following steps: 

       1. Obtain a list of valid AMI images by running the following command: 

```shell-session
$ aws ec2 describe-images --region "${REGION}" --filters "Name=name,Values=*${PRODUCT_ID}*" \
  --query 'reverse(sort_by(Images, &CreationDate))[].[CreationDate,ImageId,Name]' --output table
```


`REGION` and `PRODUCT_ID` are environment variables you created in previous steps. 

This command returns the AMIs ordered by creation date, with the latest images first. The RHCOS version of each AMI is contained in the AMI name. Choose the latest image version available. 

Make note of the Red Hat Enterprise Linux CoreOS (RHCOS) version for later use. 

       2. Set an environment variable with the AMI of the new boot image by running the following command: 

```shell-session
$ export AMI_ID=<ami-value>
```


  3. Update each of your compute machine sets to include the new boot image: 

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
$ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"ami":{"id":"'${AMI_ID}'"}}}}}}}'
```


Replace `<machineset_name>` with the name of your machine set. 

`AMI_ID` is the environment variable you created in a previous step. 

  4. If boot image skew enforcement in your cluster is set to the manual mode, update the boot image version in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version." 



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
