# 5.4. Configuring cluster details and choosing Operators to install

Once the rendezvous node has been booted from the ISO image, configure details about your cluster and choose Virtualization Operators to install from the web console. 

**Prerequisites**

  * You have the URL of the installation web console that was provided by the rendezvous node. 



**Procedure**

  1. In a web browser, go to the URL provided by the rendezvous node. 
  2. Configure your cluster in the **Cluster details** page: 

     1. Enter a name for the cluster in the **Cluster name** field. 
     2. Enter a base domain for the cluster in the **Base domain** field. All subdomains for the cluster will use this base domain. 

Note

The base domain must be a valid DNS name. You must not have a wildcard domain set up for the base domain. 

     3. Enter your pull secret in the **Pull secret** field. You can obtain a copy of your pull secret from the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/install/pull-secret). 
     4. Optional: In the **Number of control plane nodes** field, select the number of control plane nodes for your installation from the dropdown menu. The default value is `3`. 
     5. Optional: Select the **Include custom manifests** checkbox if you want to upload custom manifests to further configure your cluster. This option adds an additional page for custom manifests that you use later in the configuration process. 

Important

If you have already added custom manifests, clearing the **Include custom manifests** checkbox automatically deletes them all. You must confirm the deletion. 

     6. Optional: Under **Encryption of installation disks** , select the toggle switch for each disk you want to encrypt. 
     7. If you are encrypting disks, select either **TPM v2** or **Tang** as your encryption method. 
     8. If you are encrypting disks using a Tang server, enter the **Server URL** and **Server Thumbprint** in the **Tang servers** section of the page. You can select **Add another Tang server** to configure details for additional Tang server. 
     9. Click **Next** to continue. Once you proceed to the next page, you cannot go back to change any of these cluster details. 

  3. Choose additional Operators to install in the **Operators** page: 

     1. If you want to install all of the Operators recommended for running Virtualization on your cluster, select **Virtualization** in the **Bundles** section. 
     2. If you want to install only some Operators, select the individual Operators from the Single Operators section. 

Note

Some of the listed Operators are available only as part of the Virtualization Operator bundle. 

     3. Click **Next** to continue.
