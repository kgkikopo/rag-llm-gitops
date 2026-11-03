# 1.3. Enable the Developer perspective in the web console

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



**Additional resources**

  * [Learn more about Cluster Administrator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/overview/#learn_more_about_openshift)
  * [Viewing the applications in your project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-viewing-application-composition-using-topology-view)
  * [Viewing cluster information](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/using-dashboard-to-get-cluster-info "Chapter 3. Using the OpenShift Container Platform dashboard to get cluster information")
  * [Configuring the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/configuring-web-console "Chapter 5. Configuring the web console in OpenShift Container Platform")
  * [Customizing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/customizing-web-console "Chapter 6. Customizing the web console in OpenShift Container Platform")
  * [About the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/customizing-web-console "Chapter 6. Customizing the web console in OpenShift Container Platform")
  * [Using the web terminal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/web-terminal#odc-using-web-terminal "8.3. Using the web terminal")
  * [Creating quick start tutorials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/creating-quick-start-tutorials "Chapter 10. Creating quick start tutorials in the web console")
  * [Disabling the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/disabling-web-console "Chapter 9. Disabling the web console in OpenShift Container Platform")
