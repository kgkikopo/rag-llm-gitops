# 3.1. Creating an IBM Power Virtual Server workspace

To set up the infrastructure needed for your OpenShift Container Platform cluster, you can create an IBM Power® Virtual Server workspace and retrieve its GUID for use during installation. 

**Procedure**

  1. To create an IBM Power® Virtual Server workspace, complete step 1 to step 5 from the IBM Cloud® documentation for [Creating an IBM Power® Virtual Server](https://cloud.ibm.com/docs/power-iaas?topic=power-iaas-creating-power-virtual-server). 
  2. After it has finished provisioning, retrieve the 32-character alphanumeric Globally Unique Identifier (GUID) of your new workspace by entering the following command: 

```shell-session
$ ibmcloud resource service-instance <workspace name>
```
