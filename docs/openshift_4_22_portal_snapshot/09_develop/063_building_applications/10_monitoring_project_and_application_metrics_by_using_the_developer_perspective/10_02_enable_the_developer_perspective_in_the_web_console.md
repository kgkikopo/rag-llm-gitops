# 10.2. Enable the Developer perspective in the web console

Enable the **Developer** perspective in the web console to give your developers tools to manage applications, visualize topology, and monitor projects as they develop and build them. 

Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. There is no longer a **Developer** perspective by default; however, cluster administrators can enable the **Developer** perspective for developers to use. 

You can enable the **Developer** perspective with the following steps: 

**Prerequisites**

  * You have access to the web console as a user with `cluster-admin` privileges. 



**Procedure**

  1. Navigate to the **Cluster Settings** page by clicking Administration Cluster Settings. 
  2. Select the **Configuration** tab. 
  3. Type `console` in the search field to locate the Console Operator resource and select `operator.openshift.io`. 
  4. On the **Cluster Details** page, click the **Actions** menu and select **Customize**. 
  5. In the **General** tab, locate the **Perspectives** section. You can enable or disable the **Developer** perspective as needed. Changes are automatically applied. 
  6. Optional: You can enable the **Developer** perspective by using the CLI with the following command: 

```shell-session
$ oc patch console.operator.openshift.io/cluster --type='merge' -p '{"spec":{"customization":{"perspectives":[{"id":"dev","visibility":{"state":"Enabled"}}]}}}'
```


Note

The change reflects in the web console after the console pod restarts successfully. 




**Verification**

  1. Locate the perspective switcher in the web console. 
  2. Verify that **Developer** is displayed as an available perspective option.
