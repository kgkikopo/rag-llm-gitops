# 1.6. Completing the remaining Assisted Installer steps

After provisioning Oracle® Distributed Cloud resources and uploading OpenShift Container Platform custom manifests to Oracle Distributed Cloud, complete the remaining cluster installation steps on the Assisted Installer before you can create an Oracle Distributed Cloud instance. 

These steps include assigning node roles and adding custom manifests. 

## 1.6.1. Assigning node roles

Following host discovery, the role of all nodes appears as **Auto-assign** by default. Change each of the node roles to either **Control Plane node** or **Worker**. 

**Prerequisites**

  * You created and applied the Terraform stack in Oracle Distributed Cloud. For details, see "Provisioning OCI infrastructure for your cluster". 



**Procedure**

  1. From the Assisted Installer user interface, go to the **Host discovery** page. 
  2. Under the **Role** column, select either **Control plane node** or **Worker** for each targeted hostname. Then click **Next**. 

Note

     1. Before continuing to the next step, wait for each node to reach `Ready` status. 
     2. Expand the node to verify that the hardware type is bare metal. 

  3. Accept the default settings for the **Storage** and **Networking** pages. Then click **Next**. 



## 1.6.2. Adding custom manifests

Add the mandatory custom manifests provided by Oracle. 

For details, see [Custom Manifests (Oracle documentation).](https://github.com/dfoster-oracle/oci-openshift/blob/v1.0.0-release-preview/custom_manifests/README.md)

**Prerequisites**

  * You copied the `dynamic_custom_manifest.yml` file from the Terraform stack in Oracle Distributed Cloud. For details, see "Provisioning OCI infrastructure for your cluster". 



**Procedure**

  1. On the **Custom manifests** page, in the **Folder** field, select `manifests`. This is the Assisted Installer folder where you want to save the custom manifest file. 
  2. In the **File name** field, enter a filename, for example, `dynamic_custom_manifest.yml`. 
  3. Paste the contents of the `dynamic_custom_manifest.yml` file that you copied from Oracle Distributed Cloud: 

     1. In the **Content** section, click the **Paste content** icon. 
     2. If you are using Firefox, click **OK** to close the dialog box, and then press **Ctrl+V**. Otherwise, skip this step. 

  4. Click **Next** to save the custom manifest. 
  5. From the **Review and create** page, click **Install cluster** to create your OpenShift Container Platform cluster on Oracle Distributed Cloud. 

After the cluster installation and initialization operations, the Assisted Installer indicates the completion of the cluster installation operation. For more information, see "Completing the installation" section in the Assisted Installer for OpenShift Container Platform document. 




**Additional resources**

  * [Assisted Installer for OpenShift Container Platform](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform/)
