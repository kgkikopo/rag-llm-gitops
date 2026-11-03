# 1.7. Completing the installation by using the Assisted Installer web console

After you configure the infrastructure, the instances are now running and are ready to be registered with Red Hat. 

## 1.7.1. Assigning node roles

If the Terraform scripts completed successfully, twelve hosts are now listed for the cluster. Three control plane hosts and three compute hosts have the status "Disconnected". Three control plane hosts and three compute hosts have the status "Insufficient". 

Delete the disconnected hosts and assign roles to the remaining hosts. 

**Procedure**

  1. From the [Assisted Installer web console](https://console.redhat.com/openshift/assisted-installer/clusters), select the cluster and navigate to the **Host discovery** page. 
  2. Delete the six hosts with a "Disconnected" status, by clicking the option button for each host and selecting **Remove host**. The status of the remaining hosts changes from "Insufficient" to "Ready". This process can take up to three minutes. 
  3. From the **Role** column, assign the **Control plane** role to the three nodes with a boot size of 1.10 TB. Assign the **Worker** role to the three nodes with boot size of 100 GB. 
  4. Rename any hosts with a name shorter than 63 characters, by clicking the option button for the host and selecting **Change hostname**. Otherwise the cluster installation will fail. 
  5. Click **Next**. 
  6. On the **Storage** page, click **Next**. 



## 1.7.2. Configuring networking

On the **Networking** page, add the NTP sources for any hosts that display the `Some validations failed` status. 

**Procedure**

  1. In the **Host inventory** table, click the **Some validations failed** link for each host displaying this status. 
  2. Click **Add NTP sources** , and then add the IP address `169.254.169.254` for one of the nodes. 
  3. Wait for 2 - 3 minutes until all the **Some validations failed** indicators disappear. 
  4. Select **Next**. 



## 1.7.3. Adding custom manifests

Create, modify, and upload the four mandatory custom manifests provided by Oracle. 

  * In the `C3/custom_manifests_C3/manifests` folder, the following manifests are mandatory: 

    * `oci-ccm.yml`
    * `oci-csi.yml`

  * In the `C3/custom_manifests_C3/openshift` folder, the following manifests are mandatory: 

    * `machineconfig-ccm.yml`
    * `machineconfig-csi.yml`




**Prerequisites**

  * Prepare the custom manifests. For details, see step 8 in the "Install the Cluster using the RH Assisted Installer UI" section of the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP). 



**Procedure**

  1. Navigate to the **Custom manifests** page. 
  2. Upload and save the `oci-ccm.yml` and `oci-csi.yml` manifest files: 

     1. In the **Folder** field, select **manifests**. 
     2. In the **File name** field, enter `oci-ccm.yml`. 
     3. In the **Content** section, click **Browse**. 
     4. Select the **oci-ccm.yml** file from the `C3/custom_ manifest_C3/manifests` folder. 
     5. Click **Add another manifest** and repeat the previous substeps for the `oci-csi.yml` file. 

  3. Upload and save the `machineconfig-ccm.yml` and `machineconfig-csi.yml` manifest files: 

     1. Click **Add another manifest**. 
     2. In the **Folder** field, select **openshift**. 
     3. In the **File name** field, enter `machineconfig-ccm.yml`. 
     4. In the **Content** section, click **Browse**. 
     5. Select the **machineconfig-ccm.yml** file from the `C3/custom_ manifest_C3/openshift` folder. 
     6. Click **Add another manifest** and repeat the previous substeps for the `machineconfig-csi.yml` file. 

  4. Click **Next** to save the custom manifests. 
  5. From the **Review and create** page, click **Install cluster** to create your OpenShift Container Platform cluster. This process takes approximately thirty minutes.
