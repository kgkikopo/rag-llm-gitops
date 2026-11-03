# 3.5. Uninstall the Network Observability Operator

Uninstall the Network Observability Operator using the OpenShift Container Platform web console Operator Hub, working in the **Ecosystem** **Installed Operators** area. 

**Procedure**

  1. Remove the `FlowCollector` custom resource. 

     1. Click **Flow Collector** , which is next to the **Network Observability Operator** in the **Provided APIs** column. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) for the **cluster** and select **Delete FlowCollector**. 

  2. Uninstall the Network Observability Operator. 

     1. Navigate back to the **Ecosystem** **Installed Operators** area. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **Network Observability Operator** and select **Uninstall Operator**. 
     3. **Home** **Projects** and select `openshift-netobserv-operator`
     4. Navigate to **Actions** and select **Delete Project**

  3. Remove the `FlowCollector` custom resource definition (CRD). 

     1. Navigate to **Administration** **CustomResourceDefinitions**. 
     2. Look for **FlowCollector** and click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_Observability-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) . 
     3. Select **Delete CustomResourceDefinition**. 

Important

The Loki Operator and Kafka remain if they were installed and must be removed separately. Additionally, you might have remaining data stored in an object store, and a persistent volume that must be removed.
