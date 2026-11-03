# 1.2. Compute machine management

As a cluster administrator, you can manage the compute machines in your OpenShift Container Platform cluster. 

For example, you can perform the following actions: 

  * Create a compute machine set for the following cloud providers: 

    * [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-aws "2.1. Creating a compute machine set on AWS")
    * [Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-azure "2.2. Creating a compute machine set on Azure")
    * [Azure Stack Hub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-azure-stack-hub "2.3. Creating a compute machine set on Azure Stack Hub")
    * [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-gcp "2.4. Creating a compute machine set on Google Cloud")
    * [IBM Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-ibm-cloud "2.5. Creating a compute machine set on IBM Cloud")
    * [IBM Power Virtual Server](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-ibm-power-vs "2.6. Creating a compute machine set on IBM Power Virtual Server")
    * [Nutanix](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-nutanix "2.7. Creating a compute machine set on Nutanix")
    * [RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-osp "2.8. Creating a compute machine set on OpenStack")
    * [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-vsphere "2.9. Creating a compute machine set on vSphere")

  * Create a machine set for a bare metal deployment: [Creating a compute machine set on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#creating-machineset-bare-metal "2.10. Creating a compute machine set on bare metal")
  * [Manually scale a compute machine set](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/manually-scaling-machineset "Chapter 3. Manually scaling a compute machine set") by adding or removing a machine from the compute machine set. 
  * [Modify a compute machine set](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/modifying-machineset "Chapter 4. Modifying a compute machine set") through the `MachineSet` YAML configuration file. 
  * [Delete](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/deleting-machine "Chapter 6. Deleting a machine") a machine. 
  * [Create infrastructure compute machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-infrastructure-machinesets "Chapter 8. Creating infrastructure machine sets"). 
  * Configure and deploy a [machine health check](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/deploying-machine-health-checks "Chapter 12. Deploying machine health checks") to automatically fix damaged machines in a machine pool. 



Note

When creating a new machine set, you should specify the latest image to use for the boot image. For more information about updating the boot image on your cluster, see "Manually updating the boot image" and "Boot image management". The method to update or specify the image varies by platform. 

**Additional resources**

  * [Manually updating the boot image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images-manual)
  * [Boot image management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images)
