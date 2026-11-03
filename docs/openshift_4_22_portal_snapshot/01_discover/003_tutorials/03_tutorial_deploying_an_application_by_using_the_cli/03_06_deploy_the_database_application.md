# 3.6. Deploy the database application

Deploy a MongoDB database application to contain the information that your application requires. For this tutorial, you will deploy a database application called `mongodb-nationalparks` that holds the national park location information. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 
  * You have deployed the `nationalparks` back-end application. 



**Procedure**

  * Deploy the `mongodb-nationalparks` database application by running the following command: 

```shell-session
$ oc new-app registry.redhat.io/rhmap47/mongodb --name mongodb-nationalparks -e MONGODB_USER=mongodb -e MONGODB_PASSWORD=mongodb -e MONGODB_DATABASE=mongodb -e MONGODB_ADMIN_PASSWORD=mongodb -l 'app.kubernetes.io/part-of=national-parks-app,app.kubernetes.io/name=mongodb'
```


**Example output**

```plaintext
--> Found container image 7a61087 (12 days old) from quay.io for "quay.io/mongodb/mongodb-enterprise-server"

    * An image stream tag will be created as "mongodb-nationalparks:latest" that will track this image

--> Creating resources with label app.kubernetes.io/name=mongodb,app.kubernetes.io/part-of=national-parks-app ...
    imagestream.image.openshift.io "mongodb-nationalparks" created
    deployment.apps "mongodb-nationalparks" created
    service "mongodb-nationalparks" created
--> Success
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose service/mongodb-nationalparks'
    Run 'oc status' to view your app.
```


## 3.6.1. Provide access to the database by creating a secret

Create a `Secret` resource to securely provide the back-end application with the sensitive database connection credentials. 

The `nationalparks` application needs information, such as the database name, username, and passwords, to access the MongoDB database. However, because this information is sensitive, you should not store it directly in the pod. 

You can use a _secret_ to store sensitive information, and share that secret with workloads. 

`Secret` objects provide a mechanism to hold sensitive information such as passwords, OpenShift Container Platform client configuration files, and private source repository credentials. Secrets decouple sensitive content from the pods. You can mount secrets into containers by using a volume plugin or by passing the secret in as an environment variable. The system can then use secrets to provide the pod with the sensitive information. 

The following procedure creates the `nationalparks-mongodb-parameters` secret and mounts it to the `nationalparks` workload. 

**Prerequisites**

  * You have deployed the `nationalparks` back-end application. 
  * You have deployed the `mongodb-nationalparks` database application. 



**Procedure**

  1. Create the secret with the required database access information by running the following command: 

```shell-session
$ oc create secret generic nationalparks-mongodb-parameters --from-literal=DATABASE_SERVICE_NAME=mongodb-nationalparks --from-literal=MONGODB_USER=mongodb --from-literal=MONGODB_PASSWORD=mongodb --from-literal=MONGODB_DATABASE=mongodb --from-literal=MONGODB_ADMIN_PASSWORD=mongodb
```


  2. Import the environment from the secret to the `nationalparks` workload by running the following command: 

```shell-session
$ oc set env --from=secret/nationalparks-mongodb-parameters deploy/nationalparks
```


  3. Wait for the `nationalparks` deployment to roll out a new revision with this environment information. Check the status of the `nationalparks` deployment by running the following command: 

```shell-session
$ oc rollout status deployment nationalparks
```


**Example output**

```shell-session
deployment "nationalparks" successfully rolled out
```


**Additional resources**

  * [Understanding secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-secrets-about_nodes-pods-secrets)
  * [oc create secret generic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-create-secret-generic)
  * [oc set env](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-set-env)
  * [oc rollout status](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-rollout-status)



## 3.6.2. Load data into the database

After you have deployed the `mongodb-nationalparks` database application, load the national park location information into the database. 

**Prerequisites**

  * You have deployed the `nationalparks` back-end application. 
  * You have deployed the `mongodb-nationalparks` database application. 



**Procedure**

  * Load the national parks data by running the following command: 

```shell-session
$ oc exec $(oc get pods -l component=nationalparks | tail -n 1 | awk '{print $1;}') -- curl -s http://localhost:8080/ws/data/load
```


**Example output**

```plaintext
"Items inserted in database: 2893"
```


**Verification**

  * Verify that the map data was loaded properly by running the following command: 

```shell-session
$ oc exec $(oc get pods -l component=nationalparks | tail -n 1 | awk '{print $1;}') -- curl -s http://localhost:8080/ws/data/all
```


**Example output (trimmed)**

```shell-session
...
, {"id": "Great Zimbabwe", "latitude": "-20.2674635", "longitude": "30.9337986", "name": "Great Zimbabwe"}]
```


**Additional resources**

  * [oc exec](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#oc-exec)
