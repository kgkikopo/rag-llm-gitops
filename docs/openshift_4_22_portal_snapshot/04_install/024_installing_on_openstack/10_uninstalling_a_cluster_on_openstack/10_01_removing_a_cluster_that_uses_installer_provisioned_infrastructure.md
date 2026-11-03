# 10.1. Removing a cluster that uses installer-provisioned infrastructure

To remove an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, you can use the installation program and the installation files from your original deployment to uninstall the cluster from your cloud platform. 

Note

If you deployed your cluster to the AWS C2S Secret Region, the installation program does not support destroying the cluster; you must manually remove the cluster resources. 

Note

After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource. For example, some Google Cloud resources require [IAM permissions](https://cloud.google.com/iam/docs/overview#concepts_related_to_access_management) in shared VPC host projects, or there might be unused [health checks that must be deleted](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/delete). 

**Prerequisites**

  * You have a copy of the installation program that you used to deploy the cluster. 
  * You have the files that the installation program generated when you created your cluster. 
  * You installed the `core-installer` tool by entering the `sudo dnf install coreos-installer` command in your CLI. 



**Procedure**

  1. From the directory that has the installation program on the computer that you used to install the cluster, run the following command: 

```shell-session
$ ./openshift-install destroy cluster \
--dir <installation_directory> --log-level info
```


where: 

`<installation_directory>`
     Specify the path to the directory that you stored the installation files in. 
`--log-level info`
    

To view different details, specify `warn`, `debug`, or `error` instead of `info`. 

Note

You must specify the directory that includes the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster. 

  2. Optional: Use the `coreos-installer` tool to add the `coreos.inst.wipe=yes` flag to the Preboot Execution Environment (PXE) boot configuration. This operation wipes the disk on your system so that if you create a new cluster, you have a clean installation environment. For more detailed instructions, see [How to wipe OpenStack disks in OpenShift Container Platform 4 reinstallation](https://access.redhat.com/solutions/7128657) (Knowledgebase article). 
  3. Optional: Delete the `<installation_directory>` directory and the OpenShift Container Platform installation program.
