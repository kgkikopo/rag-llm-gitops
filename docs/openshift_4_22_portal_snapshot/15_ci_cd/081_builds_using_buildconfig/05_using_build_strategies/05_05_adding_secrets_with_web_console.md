# 5.5. Adding secrets with web console

You can add a secret to your build configuration so that it can access a private repository. 

**Procedure**

To add a secret to your build configuration so that it can access a private repository from the OpenShift Container Platform web console: 

  1. Create a new OpenShift Container Platform project. 
  2. Create a secret that contains credentials for accessing a private source code repository. 
  3. Create a build configuration. 
  4. On the build configuration editor page or in the `create app from builder image` page of the web console, set the **Source Secret**. 
  5. Click **Save**.
