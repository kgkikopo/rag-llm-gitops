# 8.2. Configuring the web terminal

You can configure timeout and image settings for the web terminal, either for your current session or for all user sessions if you are a cluster administrator. 

## 8.2.1. Configuring the web terminal timeout for a session

You can change the default timeout period for the web terminal for your current session. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster that has the Web Terminal Operator installed. 
  * You are logged into the web console. 



**Procedure**

  1. Click the web terminal icon ( ![odc wto icon](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/0b390aa1a0ac54c6972fff7f11551183/odc-wto-icon.png) ). 
  2. Optional: Set the web terminal timeout for the current session: 

     1. Click Timeout. 
     2. In the field that is displayed, enter the timeout value. 
     3. From the drop-down list, select a timeout interval of **Seconds** , **Minutes** , **Hours** , or **Milliseconds**. 

  3. Optional: Select a custom image for the web terminal to use. 

     1. Click Image. 
     2. In the field that is displayed, enter the URL of the image that you want to use. 

  4. Click **Start** to begin a terminal instance using the specified timeout setting. 



## 8.2.2. Configuring the web terminal timeout for all users

You can use the **Administrator** perspective of the web console to set the default web terminal timeout period for all users. 

**Prerequisites**

  * You have cluster administrator permissions and are logged in to the web console. 
  * You have installed the Web Terminal Operator. 



**Procedure**

  1. In the **Administrator** perspective, navigate to **Administration** **Cluster Settings**. 
  2. On the **Cluster Settings** page, click the **Configuration** tab. 
  3. On the **Configuration** page, click the **Console** configuration resource with the description **operator.openshift.io**. 

![Image of the Configuration page showing the correct Console configuration resource to select](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/415bd51512976c8041fcc74c37166f1a/cluster-settings-console.png) ![Image of the Configuration page showing the correct Console configuration resource to select](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/415bd51512976c8041fcc74c37166f1a/cluster-settings-console.png)

  4. From the **Action** drop-down list, select **Customize** , which opens the **Cluster configuration** page. 
  5. Click the **Web Terminal** tab, which opens the **Web Terminal Configuration** page. 
  6. Set a value for the timeout. From the drop-down list, select a time interval of **Seconds** , **Minutes** , **Hours** , or **Milliseconds**. 
  7. Click **Save**. 



## 8.2.3. Configuring the web terminal image for a session

You can change the default image for the web terminal for your current session. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster that has the Web Terminal Operator installed. 
  * You are logged into the web console. 



**Procedure**

  1. Click the web terminal icon ( ![odc wto icon](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/0b390aa1a0ac54c6972fff7f11551183/odc-wto-icon.png) ). 
  2. Click **Image** to display advanced configuration options for the web terminal image. 
  3. Enter the URL of the image that you want to use. 
  4. Click **Start** to begin a terminal instance using the specified image setting. 



## 8.2.4. Configuring the web terminal image for all users

You can use the **Administrator** perspective of the web console to set the default web terminal image for all users. 

**Prerequisites**

  * You have cluster administrator permissions and are logged in to the web console. 
  * You have installed the Web Terminal Operator. 



**Procedure**

  1. In the **Administrator** perspective, navigate to **Administration** **Cluster Settings**. 
  2. On the **Cluster Settings** page, click the **Configuration** tab. 
  3. On the **Configuration** page, click the **Console** configuration resource with the description **operator.openshift.io**. 

![Image of the Configuration page showing the correct Console configuration resource to select](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/415bd51512976c8041fcc74c37166f1a/cluster-settings-console.png) ![Image of the Configuration page showing the correct Console configuration resource to select](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/415bd51512976c8041fcc74c37166f1a/cluster-settings-console.png)

  4. From the **Action** drop-down list, select **Customize** , which opens the **Cluster configuration** page. 
  5. Click the **Web Terminal** tab, which opens the **Web Terminal Configuration** page. 
  6. Enter the URL of the image that you want to use. 
  7. Click **Save**.
