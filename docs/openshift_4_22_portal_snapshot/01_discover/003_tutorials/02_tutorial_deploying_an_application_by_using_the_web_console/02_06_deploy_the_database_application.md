# 2.6. Deploy the database application

Deploy a MongoDB database application to contain the information that your application requires. For this tutorial, you will deploy a database application called `mongodb-nationalparks` that holds the national park location information. 

**Prerequisites**

  * You have deployed the `parksmap` front-end application. 
  * You have deployed the `nationalparks` back-end application. 



**Procedure**

  1. From the **Quick create** ( ![fa plus circle](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Tutorials-en-US/images/c1952cc876dd671e19fa1e45646b272c/fa-plus-circle.png) ) menu in the upper right corner, click **Container images**. 
  2. Select **Image name from external registry** and enter `registry.redhat.io/rhmap47/mongodb`. 
  3. In the **Runtime icon** field, search for and select `mongodb`. 
  4. Scroll to the **General** section. 
  5. In the **Application name** field, enter `national-parks-app`. 
  6. In the **Name** field, enter `mongodb-nationalparks`. 
  7. Scroll to the **Deploy** section. 
  8. In the **Resource type** field, ensure that **Deployment** is selected. 
  9. Click **Show advanced Deployment option**. 
  10. Under **Environment variables (runtime only)** , add the following names and values: 

Table 2.1. Environment variable names and valuesName| Value  
---|---  
`MONGODB_USER` |  `mongodb`  
`MONGODB_PASSWORD` |  `mongodb`  
`MONGODB_DATABASE` |  `mongodb`  
`MONGODB_ADMIN_PASSWORD` |  `mongodb`  
Show more

Tip

Click **Add value** to add each additional environment variable. 

  11. In the **Advanced options** section, clear **Create a route**. 

The database application does not need to be accessed externally, so a route is not required. 

  12. Click **Create**. 

You are redirected to the **Topology** page where you can see the `mongodb-nationalparks` deployment in the `national-parks-app` application. 




## 2.6.1. Provide access to the database by creating a secret

Create a `Secret` resource to securely provide the back-end application with the sensitive database connection credentials. 

The `nationalparks` application needs information, such as the database name, username, and passwords, to access the MongoDB database. However, because this information is sensitive, you should not store it directly in the pod. 

You can use a _secret_ to store sensitive information, and share that secret with workloads. 

`Secret` objects provide a mechanism to hold sensitive information such as passwords, OpenShift Container Platform client configuration files, and private source repository credentials. Secrets decouple sensitive content from the pods. You can mount secrets into containers by using a volume plugin or by passing the secret in as an environment variable. The system can then use secrets to provide the pod with the sensitive information. 

The following procedure creates the `nationalparks-mongodb-parameters` secret and mounts it to the `nationalparks` workload. 

**Prerequisites**

  * You have deployed the `nationalparks` back-end application. 
  * You have deployed the `mongodb-nationalparks` database application. 



**Procedure**

  1. Navigate to **Workloads** **Secrets**. 
  2. Click **Create** **Key/value secret**. 
  3. In the **Secret name** field, enter `nationalparks-mongodb-parameters`. 
  4. Enter the following values for **Key** and **Value** : 

Table 2.2. Secret keys and valuesKey| Value  
---|---  
`DATABASE_SERVICE_NAME` |  `mongodb-nationalparks`  
`MONGODB_USER` |  `mongodb`  
`MONGODB_PASSWORD` |  `mongodb`  
`MONGODB_DATABASE` |  `mongodb`  
`MONGODB_ADMIN_PASSWORD` |  `mongodb`  
Show more

Tip

Click **Add key/value** to add each additional key/value pair. 

  5. Click **Create**. 
  6. Click **Add Secret to workload**. 
  7. From the **Add this secret to workload** list, select `nationalparks`. 
  8. Click **Save**. 

This change in configuration triggers a new rollout of the `nationalparks` deployment with the environment variables properly injected. 




**Additional resources**

  * [Understanding secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-secrets-about_nodes-pods-secrets)



## 2.6.2. Load data into the database

After you have deployed the `mongodb-nationalparks` database application, load the national park location information into the database. 

**Prerequisites**

  * You have deployed the `nationalparks` back-end application. 
  * You have deployed the `mongodb-nationalparks` database application. 



**Procedure**

  1. Navigate to **Workloads** **Topology**. 
  2. Click the `nationalparks` deployment and select the **Resources** tab. 
  3. Copy the **Location** URL from your route. 
  4. Paste the URL into your web browser and add the following at the end of the URL: 

```plaintext
/ws/data/load
```


For example: 

```plaintext
https://nationalparks-user-getting-started.apps.cluster.example.com/ws/data/load
```


**Example output**

```plaintext
Items inserted in database: 2893
```
