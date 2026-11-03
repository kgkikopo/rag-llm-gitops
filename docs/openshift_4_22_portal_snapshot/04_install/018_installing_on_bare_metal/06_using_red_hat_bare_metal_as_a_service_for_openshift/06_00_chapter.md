# Chapter 6. Using Red Hat Bare-Metal-as-a-Service for OpenShift

You can provision and manage bare-metal hosts by using the Metal3 API and the Bare Metal Operator (BMO). These hosts, external to the OpenShift Container Platform cluster, can run workloads that might not be suitable for containerization or virtualization, such as legacy applications or applications that require direct hardware access. 

Red Hat Bare-Metal-as-a-Service for OpenShift has the following capabilities: 

  * Provisioning of bare-metal hosts, including initial configuration. 
  * Lifecycle management such as power management, firmware updates, and decommissioning by using the BMO. 



As standalone systems, these hosts operate independently of the OpenShift Container Platform cluster and support diverse workloads by integrating bare metal resources with containerized and virtualized applications. Red Hat Bare-Metal-as-a-Service for OpenShift can run other operating systems, but only Red Hat Enterprise Linux (RHEL) and CentOS Stream 9 were tested.

- [6.1. Prerequisites for using Red Hat Bare-Metal-as-a-Service for OpenShift](06_01_prerequisites_for_using_red_hat_bare_metal_as_a_service_for_openshift.md)
- [6.2. Using the Bare Metal Operator to manage resources across all namespaces](06_02_using_the_bare_metal_operator_to_manage_resources_across_all_namespaces.md)
- [6.3. Setting up a dedicated namespace](06_03_setting_up_a_dedicated_namespace.md)
- [6.4. Creating a BMC secret](06_04_creating_a_bmc_secret.md)
- [6.5. Creating a bare-metal host resource](06_05_creating_a_bare_metal_host_resource.md)
- [6.6. Configuring users for Red Hat Bare-Metal-as-a-Service for OpenShift hosts](06_06_configuring_users_for_red_hat_bare_metal_as_a_service_for_openshift_hosts.md)
- [6.7. Configuring the networkData parameter in the BareMetalHost resource](06_07_configuring_the_networkdata_parameter_in_the_baremetalhost_resource.md)
- [6.8. Deploying an image to the bare-metal host](06_08_deploying_an_image_to_the_bare_metal_host.md)
