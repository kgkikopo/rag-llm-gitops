# 3.5. Deploy the back-end application

Deploy the back-end application that provides the service that queries the database to return the national park data required for your application. 

The following procedure deploys `nationalparks`, which is the back-end component for the `national-parks-app` application. The Python application performs 2D geo-spatial queries against a MongoDB database to locate and return map coordinates of all national parks in the world. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 



**Procedure**

  * Create the `nationalparks` back-end application by running the following command: 

```shell-session
$ oc new-app https://github.com/openshift-roadshow/nationalparks-py.git --name nationalparks -l 'app=national-parks-app,component=nationalparks,role=backend,app.kubernetes.io/part-of=national-parks-app,app.kubernetes.io/name=python' --allow-missing-images=true
```


**Example output**

```plaintext
--> Found image 9531750 (2 weeks old) in image stream "openshift/python" under tag "3.11-ubi8" for "python"

    Python 3.11
    -----------
...

--> Creating resources with label app=national-parks-app,app.kubernetes.io/name=python,app.kubernetes.io/part-of=national-parks-app,component=nationalparks,role=backend ...
    imagestream.image.openshift.io "nationalparks" created
    buildconfig.build.openshift.io "nationalparks" created
    deployment.apps "nationalparks" created
    service "nationalparks" created
--> Success
    Build scheduled, use 'oc logs -f buildconfig/nationalparks' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose service/nationalparks'
    Run 'oc status' to view your app.
```


## 3.5.1. Expose the back-end service

To expose the back-end service so that it is accessible externally, create a route. 

**Prerequisites**

  * You have deployed the `nationalparks` back-end application. 
  * You have `cluster-admin` or project-level `admin` privileges. 



**Procedure**

  1. Create a route to expose the `nationalparks` back-end application by running the following command: 

```shell-session
$ oc create route edge nationalparks --service=nationalparks
```


  2. Label the `nationalparks` route by running the following command: 

```shell-session
$ oc label route nationalparks type=parksmap-backend
```


The application code expects the `nationalparks` route to be labeled with `type=parksmap-backend`. 




**Additional resources**

  * [oc label](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-label)
