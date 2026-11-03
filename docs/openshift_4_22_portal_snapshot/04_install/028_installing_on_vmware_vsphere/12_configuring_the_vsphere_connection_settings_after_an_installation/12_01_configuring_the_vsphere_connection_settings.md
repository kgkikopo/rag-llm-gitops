# 12.1. Configuring the vSphere connection settings

Modify the following vSphere configuration settings as required: 

  * vCenter address 
  * vCenter cluster 
  * vCenter username 
  * vCenter password 
  * vCenter address 
  * vSphere data center 
  * vSphere datastore 
  * Virtual machine folder 



**Prerequisites**

  * The Assisted Installer has finished installing the cluster successfully. 
  * The cluster is connected to `<https://console.redhat.com>`. 



**Procedure**

  1. In the Administrator perspective, navigate to **Home Overview**. 
  2. Under **Status** , click **vSphere connection** to open the **vSphere connection configuration** wizard. 
  3. In the **vCenter** field, enter the network address of the vSphere vCenter server. This can be either a domain name or an IP address. It appears in the vSphere web client URL; for example `https://[your_vCenter_address]/ui`. 
  4. In the **vCenter cluster** field, enter the name of the vSphere vCenter cluster where OpenShift Container Platform is installed. 

Important

This step is mandatory if you installed OpenShift Container Platform 4.13 or later. 

  5. In the **Username** field, enter your vSphere vCenter username. 
  6. In the **Password** field, enter your vSphere vCenter password. 

Warning

The system stores the username and password in the `vsphere-creds` secret in the `kube-system` namespace of the cluster. An incorrect vCenter username or password makes the cluster nodes unschedulable. 

  7. In the **Datacenter** field, enter the name of the vSphere data center that contains the virtual machines used to host the cluster; for example, `SDDC-Datacenter`. 
  8. In the **Default data store** field, enter the path and name of the vSphere data store that stores the persistent data volumes; for example, `/SDDC-Datacenter/datastore/datastorename`. 

Warning

Updating the vSphere data center or default data store after the configuration has been saved detaches any active vSphere `PersistentVolumes`. 

  9. In the **Virtual Machine Folder** field, enter the data center folder that contains the virtual machine of the cluster; for example, `/SDDC-Datacenter/vm/ci-ln-hjg4vg2-c61657-t2gzr`. For the OpenShift Container Platform installation to succeed, all virtual machines comprising the cluster must be located in a single data center folder. 
  10. Click **Save Configuration**. This updates the `cloud-provider-config` ConfigMap resource in the `openshift-config` namespace, and starts the configuration process. 
  11. Reopen the **vSphere connection configuration** wizard and expand the **Monitored operators** panel. Check that the status of the operators is either **Progressing** or **Healthy**.
