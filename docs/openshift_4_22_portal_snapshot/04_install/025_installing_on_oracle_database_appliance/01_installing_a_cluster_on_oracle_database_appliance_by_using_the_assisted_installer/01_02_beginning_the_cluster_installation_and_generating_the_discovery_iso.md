# 1.2. Beginning the cluster installation and generating the Discovery ISO

Begin installing the OpenShift Container Platform cluster in the Oracle Database Appliance (ODA) environment by using the Red Hat Hybrid Cloud Console. 

**Procedure**

  1. Log in to the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/cluster-list). 
  2. On the **Cluster List** page, click **Create cluster**. 
  3. Click the **Datacenter** tab. 
  4. Under **Assisted Installer** , click **Create cluster**. 
  5. Configure your cluster on the **Cluster details** page: 

     1. Enter a name for the cluster in the **Cluster name** field. 
     2. Enter a base domain for the cluster in the **Base domain** field. All subdomains for the cluster will use this base domain. 

Note

The base domain must be a valid DNS name. You must not have a wildcard domain set up for the base domain. 

     3. Select a version from the **OpenShift version** dropdown list. By default, the dropdown list displays the latest version. 
     4. Optional: In the **Number of control plane nodes** field, select the number of control plane nodes for your installation from the dropdown menu. The default value is `3`. 
     5. Optional: Select the **Include custom manifests** checkbox if you want to upload custom manifests to further configure your cluster. This option adds an additional page for custom manifests that you use later in the configuration process. 

Important

If you have already added custom manifests, clearing the **Include custom manifests** checkbox automatically deletes them all. You must confirm the deletion. 

     6. Click **Next** to continue. Once you proceed to the next page, you cannot go back to change any of these cluster details. 

  6. Choose additional Operators to install on the **Operators** page: 

     1. If you want to install an Operator bundle, select an option in the **Bundles** section. 
     2. If you want to install only some Operators, select the individual Operators from the **Single Operators** section. 
     3. Click **Next** to continue. 

  7. Upload an SSH public key and generate the Discovery ISO: 

     1. Click the **Add Hosts** button in the **Host Discovery** page. 
     2. Upload an SSH public key in the **SSH public key** section so that you can connect to the cluster nodes as the `core` user. If you do not already have an SSH public key, see "Generating a key pair for cluster node SSH access" for more information. 
     3. Select **Show proxy settings**. 
     4. Enter values for the **HTTP proxy URL** , **HTTPS URL proxy** , and **No proxy domains** fields. 
     5. Click **Generate Discovery ISO**. 

  8. Copy the command from the **Command to download the ISO** field and run the command as a root user in the ODA environment. 

**Example command**

```shell-session
# wget -O discovery_image_example.iso 'https://api.openshift.com/api/assisted-images/bytoken/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Njg0Mjc3MDIsInN1YiI6ImNhMzZjZWU1LTQ3ZWEtNDc0Ny05OTg5LTVhZTYyMmMzMjZlNSJ9.jl-HvaxBR-WX73vpxO-Fy65bmY-RE5iL6AqL0wbWCmE/4.20/x86_64/minimal.iso'
```


**Additional resources**

  * [Generating a key pair for cluster node SSH access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#ssh-agent-using_installing-platform-agnostic)
