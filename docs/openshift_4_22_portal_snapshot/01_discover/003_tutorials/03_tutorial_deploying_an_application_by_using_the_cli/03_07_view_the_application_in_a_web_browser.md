# 3.7. View the application in a web browser

After you have deployed the necessary applications and loaded data into the database, you are now ready view your application through a browser. You can get the URL for the application by retrieving the route information for the front-end application. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 
  * You have deployed the `nationalparks` back-end application. 
  * You have deployed the `mongodb-nationalparks` database application. 
  * You have loaded the data into the `mongodb-nationalparks` database. 



**Procedure**

  1. Get your route information to retrieve your map application URL by running the following command: 

```shell-session
$ oc get route parksmap
```


**Example output**

```shell-session
NAME       HOST/PORT                                                  PATH   SERVICES    PORT       TERMINATION   WILDCARD
parksmap   parksmap-user-getting-started.apps.cluster.example.com            parksmap    8080-tcp   edge          None
```


  2. From the above output, copy the value in the `HOST/PORT` column. 
  3. Add `https://` in front of the copied value to get the application URL. This is necessary because the route is a secured route. 

**Example application URL**

```plaintext
https://parksmap-user-getting-started.apps.cluster.example.com
```


  4. Paste this application URL into your web browser. Your browser should display a map of the national parks across the world. 

**Figure 3.1. National parks across the world**

![Map of the national parks across the world](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/715bfb995a0e1e9f086dd6b601b252ce/getting-started-map-national-parks.png) ![Map of the national parks across the world](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/715bfb995a0e1e9f086dd6b601b252ce/getting-started-map-national-parks.png)

If you allow the application to access your location, the map will center on your location.
