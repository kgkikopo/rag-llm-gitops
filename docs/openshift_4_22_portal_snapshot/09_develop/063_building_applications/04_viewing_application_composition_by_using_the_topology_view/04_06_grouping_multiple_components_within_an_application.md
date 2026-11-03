# 4.6. Grouping multiple components within an application

You can use the **+Add** view to add multiple components or services to your project and use the topology **Graph view** to group applications and resources within an application group. 

**Prerequisites**

  * You have created and deployed minimum two or more components on OpenShift Container Platform using the **Developer** perspective. 



**Procedure**

  * To add a service to the existing application group, press `Shift`\+ drag it to the existing application group. Dragging a component and adding it to an application group adds the required labels to the component. 

**Figure 4.4. Application grouping**

![odc app grouping label](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/17864e83a2e05d6b87f16aa1604cf1be/odc_app_grouping_label.png) ![odc app grouping label](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/17864e83a2e05d6b87f16aa1604cf1be/odc_app_grouping_label.png)




Alternatively, you can also add the component to an application as follows: 

  1. Click the service pod to see the **Overview** panel to the right. 
  2. Click the **Actions** drop-down menu and select **Edit Application Grouping**. 
  3. In the **Edit Application Grouping** dialog box, click the **Application** drop-down list, and select an appropriate application group. 
  4. Click **Save** to add the service to the application group. 

You can remove a component from an application group by selecting the component and using `Shift`\+ drag to drag it out of the application group.
