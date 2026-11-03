# 1.8. Creating a Jenkins service from a template

Templates provide parameter fields to define all the environment variables with predefined default values. OpenShift Container Platform provides templates to make creating a new Jenkins service easy. The Jenkins templates should be registered in the default `openshift` project by your cluster administrator during the initial cluster setup. 

The two available templates both define deployment configuration and a service. The templates differ in their storage strategy, which affects whether the Jenkins content persists across a pod restart. 

Note

A pod might be restarted when it is moved to another node or when an update of the deployment configuration triggers a redeployment. 

  * `jenkins-ephemeral` uses ephemeral storage. On pod restart, all data is lost. This template is only useful for development or testing. 
  * `jenkins-persistent` uses a Persistent Volume (PV) store. Data survives a pod restart. 



To use a PV store, the cluster administrator must define a PV pool in the OpenShift Container Platform deployment. 

After you select which template you want, you must instantiate the template to be able to use Jenkins. 

**Procedure**

  * Create a new Jenkins application using one of the following methods: 

    * A PV: 

```shell-session
$ oc new-app jenkins-persistent
```


    * Or an `emptyDir` type volume where configuration does not persist across pod restarts: 

```shell-session
$ oc new-app jenkins-ephemeral
```


With both templates, you can run `oc describe` on them to see all the parameters available for overriding. 

For example: 

```shell-session
$ oc describe jenkins-ephemeral
```
