# Chapter 2. Tutorial: Deploying an application by using the web console

To learn how to stand up an application on OpenShift Container Platform by using the web console, follow the provided tutorial. In this tutorial, you will deploy the services that are required for an application that displays a map of national parks across the world. 

To complete this tutorial, you will perform the following steps: 

  1. [Create a project for the application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console#getting-started-web-console-creating-new-project_dev-app-web-console "2.2. Create a project"). 

This step allows your application to be isolated from other cluster user’s workloads. 

  2. [Grant view permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console#getting-started-web-console-granting-permissions_dev-app-web-console "2.3. Grant view permissions"). 

This step grants `view` permissions to interact with the OpenShift API to help discover services and other resources running within the project. 

  3. [Deploy the front-end application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console#getting-started-web-console-deploying-first-image_dev-app-web-console "2.4. Deploy the front-end application"). 

This step deploys the `parksmap` front-end application, exposes it externally, and scales it up to two instances. 

  4. [Deploy the back-end application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console#getting-started-web-console-deploying-python-app_dev-app-web-console "2.5. Deploy the back-end application"). 

This step deploys the `nationalparks` back-end application and exposes it externally. 

  5. [Deploy the database application](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console#getting-started-web-console-connecting-database_dev-app-web-console "2.6. Deploy the database application"). 

This step deploys the `mongodb-nationalparks` MongoDB database, loads data into the database, and sets up the necessary credentials to access the database. 




After you complete these steps, you can [view the national parks application in a web browser](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/tutorials/dev-app-web-console#getting-started-web-console-view_dev-app-web-console "2.7. View the application in a web browser").

- [2.1. Prerequisites](02_01_prerequisites.md)
- [2.2. Create a project](02_02_create_a_project.md)
- [2.3. Grant view permissions](02_03_grant_view_permissions.md)
- [2.4. Deploy the front-end application](02_04_deploy_the_front_end_application.md)
- [2.5. Deploy the back-end application](02_05_deploy_the_back_end_application.md)
- [2.6. Deploy the database application](02_06_deploy_the_database_application.md)
- [2.7. View the application in a web browser](02_07_view_the_application_in_a_web_browser.md)
