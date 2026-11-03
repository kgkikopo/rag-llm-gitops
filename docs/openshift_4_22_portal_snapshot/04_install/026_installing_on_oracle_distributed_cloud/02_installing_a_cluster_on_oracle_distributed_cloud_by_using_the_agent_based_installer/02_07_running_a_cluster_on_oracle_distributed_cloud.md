# 2.7. Running a cluster on Oracle Distributed Cloud

To run a cluster on Oracle® Distributed Cloud, you must upload the generated agent ISO image to the default Object Storage bucket on Oracle Distributed Cloud. 

Additionally, you must create a compute instance from the supplied base image, so that OpenShift Container Platform and Oracle Distributed Cloud can communicate with each other for the purposes of running the cluster on Oracle Distributed Cloud. 

Note

Oracle Distributed Cloud supports the following OpenShift Container Platform cluster topologies: 

  * Installing an OpenShift Container Platform cluster on a single node. 
  * A highly available cluster that has a minimum of three control plane instances and two compute instances. 
  * A compact three-node cluster that has a minimum of three control plane instances. 



**Prerequisites**

  * You generated an agent ISO image. See the "Creating configuration files for installing a cluster on OCI" section. 



**Procedure**

  1. Upload the agent ISO image to Oracle’s default Object Storage bucket and import the agent ISO image as a custom image to this bucket. Ensure you that you configure the custom image to boot in Unified Extensible Firmware Interface (UEFI) mode. For more information, see [Creating the OpenShift Container Platform ISO Image (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/installing-agent-image-creation.htm). 
  2. Create a compute instance from the supplied base image for your cluster topology. See [Creating the OpenShift Container Platform cluster on OCI (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/installing-agent-first-node.htm). 

Important

Before you create the compute instance, check that you have enough memory and disk resources for your cluster. Additionally, ensure that at least one compute instance has the same IP address as the address stated under `rendezvousIP` in the `agent-config.yaml` file. 




**Additional resources**

  * [Instance Sizing Recommendations for OpenShift Container Platform Nodes (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/installing-agent-about-instance-configurations.htm)
  * [Troubleshooting OpenShift Container Platform on OCI (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/openshift-troubleshooting.htm)
