# 12.3. Edit the application configuration using the Developer perspective

You can use the **Topology** view in the **Developer** perspective to edit the configuration of your application. 

Note

Currently, only configurations of applications created by using the **From Git** , **Container Image** , **From Catalog** , or **From Dockerfile** options in the **Add** workflow of the **Developer** perspective can be edited. Configurations of applications created by using the CLI or the **YAML** option from the **Add** workflow cannot be edited. 

**Prerequisites**

Ensure that you have created an application using the **From Git** , **Container Image** , **From Catalog** , or **From Dockerfile** options in the **Add** workflow. 

**Procedure**

  1. After you have created an application and it is displayed in the **Topology** view, right-click the application to see the edit options available. 

**Figure 12.1. Edit application**

![odc edit app](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/af0e4e672bc9f7ace9cb16c43c3cae66/odc_edit_app.png) ![odc edit app](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/af0e4e672bc9f7ace9cb16c43c3cae66/odc_edit_app.png)

  2. Click **Edit _application-name_** to see the **Add** workflow you used to create the application. The form is pre-populated with the values you had added while creating the application. 
  3. Edit the necessary values for the application. 

Note

You cannot edit the **Name** field in the **General** section, the CI/CD pipelines, or the **Create a route to the application** field in the **Advanced Options** section. 

  4. Click **Save** to restart the build and deploy a new image. 

**Figure 12.2. Edit and redeploy application**

![odc edit redeploy](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/8704b4f1d2c66eb8d1ff18ab7fa776df/odc_edit_redeploy.png) ![odc edit redeploy](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Building_applications-en-US/images/8704b4f1d2c66eb8d1ff18ab7fa776df/odc_edit_redeploy.png)
