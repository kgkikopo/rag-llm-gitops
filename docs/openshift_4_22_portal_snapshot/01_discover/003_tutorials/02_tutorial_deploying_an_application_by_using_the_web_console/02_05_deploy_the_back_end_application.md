# 2.5. Deploy the back-end application

Deploy the back-end application that provides the service that queries the database to return the national park data required for your application. 

The following procedure deploys `nationalparks`, which is the back-end component for the `national-parks-app` application. The Python application performs 2D geo-spatial queries against a MongoDB database to locate and return map coordinates of all national parks in the world. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 



**Procedure**

  1. From the **Quick create** ( ![fa plus circle](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/c1952cc876dd671e19fa1e45646b272c/fa-plus-circle.png) ) menu in the upper right corner, click **Import from Git**. 
  2. In the **Git Repo URL** field, enter `https://github.com/openshift-roadshow/nationalparks-py.git`. 

A builder image is automatically detected, but the import strategy defaults to Dockerfile instead of Python. 

  3. Change the import strategy: 

     1. Click **Edit Import Strategy**. 
     2. Select **Builder Image**. 
     3. Select **Python**. 

  4. Scroll to the **General** section. 
  5. In the **Application** field, ensure that the value is `national-parks-app`. 
  6. In the **Name** field, enter `nationalparks`. 
  7. Scroll to the **Deploy** section. 
  8. In the **Resource type** field, ensure that **Deployment** is selected. 
  9. In the **Advanced options** section, ensure that **Create a route** is selected. 

By default, services running on OpenShift Container Platform are not accessible externally. You must select this option to create a route so that external clients can access your service. 

  10. Click the **Labels** hyperlink. 

The application code requires certain labels to be set. 

  11. Add the following labels to the text area and press Enter after each key/value pair: 

     * `app=national-parks-app`
     * `component=nationalparks`
     * `role=backend`
     * `type=parksmap-backend`

  12. Click **Create**. 

You are redirected to the **Topology** page where you can see the `nationalparks` deployment in the `national-parks-app` application. 




**Verification**

  1. Navigate to **Workloads** **Topology**. 
  2. Click the `nationalparks` deployment in the `national-parks-app` application. 
  3. Click the **Resources** tab. 

Wait for the build to complete successfully. 




**Additional resources**

  * [Adding services to your application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-adding-services-to-your-application_viewing-application-composition-using-topology-view)
  * [Importing a codebase from Git to create an application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#odc-importing-codebase-from-git-to-create-application_odc-creating-applications-using-developer-perspective)
