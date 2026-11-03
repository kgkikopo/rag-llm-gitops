# 2.1. Requirements for clusters on RHOSP or RHOSO that use either SR-IOV or OVS-DPDK

If you use SR-IOV or OVS-DPDK with your deployment, you must meet certain requirements. 

Ensure that RHOSP compute nodes use a flavor that supports huge pages. 

## 2.1.1. Requirements for clusters on RHOSP or RHOSO that use SR-IOV

To use single-root I/O virtualization (SR-IOV) with your deployment, you must meet specific requirements. 

The requirements are as follows: 

  * If you use Red Hat OpenStack Platform (RHOSP), see "Planning an SR-IOV deployment (Red Hat OpenStack Platform (RHOSP) documentation)". 
  * If you use Red Hat OpenStack Services on OpenShift (RHOSO), see "Planning an SR-IOV deployment (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)". 
  * OpenShift Container Platform must support the NICs that you use. For a list of supported NICs, see "About Single Root I/O Virtualization (SR-IOV) hardware networks". 
  * For each node that will have an attached SR-IOV NIC, your RHOSP cluster must have: 

    * One instance from the quota. 
    * One port attached to the machines subnet. 
    * One port for each SR-IOV Virtual Function. 
    * A flavor with at least 16 GB memory, 4 vCPUs, and 25 GB storage space. 

  * SR-IOV deployments often employ performance optimizations, such as dedicated or isolated CPUs. For maximum performance, configure your underlying RHOSP deployment to use these optimizations, and then run OpenShift Container Platform compute machines on the optimized infrastructure. 

    * If you use RHOSP, see "Configuring CPUs on Compute nodes (Red Hat OpenStack Platform (RHOSP) documentation)". 
    * If you use RHOSO, see "NFV performance considerations (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)". 




**Additional resources**

  * [About Single Root I/O Virtualization (SR-IOV) hardware networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#about-sriov)
  * [Planning an SR-IOV deployment (Red Hat OpenStack Platform (RHOSP) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_network_functions_virtualization/plan-sriov-deploy_rhosp-nfv)
  * [Configuring CPUs on Compute nodes (Red Hat OpenStack Platform (RHOSP) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_the_compute_service_for_instance_creation/assembly_configuring-cpus-on-compute-nodes)
  * [Planning an SR-IOV deployment (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_services_on_openshift/18.0/html/deploying_a_network_functions_virtualization_environment/plan-sriov-deploy_rhoso-nfv)
  * [NFV performance considerations (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_services_on_openshift/18.0/html-single/deploying_a_network_functions_virtualization_environment/index#nfv-perf-consider_rhoso-nfv)



## 2.1.2. Requirements for clusters on RHOSP or RHOSO that use OVS-DPDK

To use Open vSwitch with the Data Plane Development Kit (OVS-DPDK) with your deployment, you must meet specific requirements. 

The requirements are as follows: 

  * If you use Red Hat OpenStack Platform (RHOSP): 

    * Plan your OVS-DPDK deployment. For more information, see "Planning your OVS-DPDK deployment (Red Hat OpenStack Platform (RHOSP) documentation)". 
    * Configure your OVS-DPDK deployment. For more information, see "Configuring an OVS-DPDK deployment (Red Hat OpenStack Platform (RHOSP) documentation)". 

  * If you use Red Hat OpenStack Services on OpenShift (RHOSO): 

    * Plan your OVS-DPDK deployment. For more information, see "Planning an OVS-DPDK deployment (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)". 
    * Configure your OVS-DPDK deployment. For more information, see"Creating the data plane for SR-IOV and DPDK environments (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)". 




**Additional resources**

  * [Planning your OVS-DPDK deployment (Red Hat OpenStack Platform (RHOSP) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_network_functions_virtualization/plan-ovs-dpdk-deploy_rhosp-nfv)
  * [Creating a flavor and deploying an instance for OVS-DPDK](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_network_functions_virtualization/config-dpdk-deploy_rhosp-nfv#create-flavor-deploy-instance-ovsdpdk_cfgdpdk-nfv)
  * [Creating a custom OVS-DPDK Compute service](https://docs.redhat.com/en/documentation/red_hat_openstack_services_on_openshift/18.0/html/deploying_a_network_functions_virtualization_environment/assembly_create-data-plane-sriov-dpdk_rhoso-nfv)
  * [Configuring an OVS-DPDK deployment (Red Hat OpenStack Platform (RHOSP) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_network_functions_virtualization/config-dpdk-deploy_rhosp-nfv)
  * [Planning an OVS-DPDK deployment (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_services_on_openshift/18.0/html/deploying_a_network_functions_virtualization_environment/plan-ovs-dpdk-deploy_rhoso-nfv)
  * [Creating the data plane for SR-IOV and DPDK environments (Red Hat OpenStack Services on OpenShift (RHOSO) documentation)](https://docs.redhat.com/en/documentation/red_hat_openstack_services_on_openshift/18.0/html/deploying_a_network_functions_virtualization_environment/assembly_create-data-plane-sriov-dpdk_rhoso-nfv)
