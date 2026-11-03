# 5.5. Obtaining your cluster ID

When providing information to Red Hat Support, it is helpful to provide the unique identifier for your cluster. You can have your cluster ID autofilled by using the OpenShift Container Platform web console. You can also manually obtain your cluster ID by using the web console or the OpenShift CLI (`oc`). 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have access to the web console or the OpenShift CLI (`oc`) installed. 



**Procedure**

  * To open a support case and have your cluster ID autofilled using the web console: 

    1. From the toolbar, navigate to **(?) Help** and select **Share Feedback** from the list. 
    2. Click **Open a support case** from the **Tell us about your experience** window. 

  * To manually obtain your cluster ID using the web console: 

    1. Navigate to **Home** **Overview**. 
    2. The value is available in the **Cluster ID** field of the **Details** section. 

  * To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command: 

```shell-session
$ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
```
