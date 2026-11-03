# 4.3. Cluster tabs

Selecting an active, installed cluster shows tabs associated with that cluster. The following tabs display after the cluster’s installation completes: 

  * Overview 
  * Access control 
  * Add-ons 
  * Networking 
  * Machine pools 
  * Red Hat Lightspeed Advisor 
  * Support 
  * Settings 



## 4.3.1. Overview tab

The **Overview** tab provides information about how the cluster was configured: 

  * **Cluster ID** is the unique identification for the created cluster. This ID can be used when issuing commands to the cluster from the command line. 
  * **Domain prefix** is the prefix that is used throughout the cluster. The default value is the cluster’s name. 
  * **Type** shows the type of cluster, for example Red Hat OpenShift Service on AWS (classic architecture), Red Hat OpenShift Service on AWS, or OpenShift Dedicated. 
  * **Control plane type** is the architecture type of the cluster. The field only displays if the cluster uses a hosted control plane architecture. 
  * **Region** is the server region. 
  * **Version** is the OpenShift version that is installed on the cluster. If there is an update available, you can update from this field. 
  * **Created at** shows the date and time that the cluster was created. 
  * **Owner** identifies who created the cluster and has owner rights. 
  * **Delete Protection: <status>** shows whether or not the cluster’s delete protection is enabled. 
  * **Total vCPU** shows the total available virtual CPU for this cluster. 
  * **Total memory** shows the total available memory for this cluster. 
  * **Infrastructure AWS account** displays the AWS account that is responsible for cluster creation and maintenance. 
  * **Nodes** shows the actual and desired nodes on the cluster. These numbers might not match due to cluster scaling. 
  * **Network** field shows the address and prefixes for network connectivity. 
  * **OIDC configuration** field shows the Open ID Connect configuration for the cluster. 
  * **Resource usage** section of the tab displays the resources in use with a graph. 
  * **Advisor recommendations** section gives insight in relation to security, performance, availability, and stability. This section requires the use of remote health functionality. See _Using Red Hat Lightspeed to identify issues with the cluster_ in the _Additional resources_ section. 



## 4.3.2. Access control tab

The **Access control** tab allows the cluster owner to set up an identity provider, grant elevated permissions, and grant roles to other users. 

## 4.3.3. Add-ons tab

## 4.3.4. Red Hat Lightspeed Advisor tab

The **Red Hat Lightspeed Advisor** tab uses the Remote Health functionality of the OpenShift Container Platform to identify and mitigate risks to security, performance, availability, and stability. 

**Additional resources**

  * [Using Red Hat Lightspeed to identify issues with your cluster](https://docs.openshift.com/container-platform/latest/support/getting-support.html)



## 4.3.5. Machine pools tab

The **Machine pools** tab allows the cluster owner to create new machine pools if there is enough available quota, or edit an existing machine pool. 

Selecting the ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Architecture-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) > **Edit** option opens the "Edit machine pool" dialog. In this dialog, you can change the node count per availability zone, edit node labels and taints, and view any associated AWS security groups. 

## 4.3.6. Support tab

In the **Support** tab, you can add notification contacts for individuals that should receive cluster notifications. The username or email address that you provide must relate to a user account in the Red Hat organization where the cluster is deployed. 

Also from this tab, you can open a support case to request technical support for your cluster. 

## 4.3.7. Settings tab

The **Settings** tab provides a few options for the cluster owner: 

  * **Update strategy** allows you to determine if the cluster automatically updates on a certain day of the week at a specified time or if all updates are scheduled manually. 
  * **Update status** shows the current version and if there are any updates available.
