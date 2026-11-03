# 8.6. Configure a secondary external gateway

You can configure an external gateway on the default network for a namespace in your cluster. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster with a user with `cluster-admin` privileges. 



**Procedure**

  1. Create a YAML file that contains an `AdminPolicyBasedExternalRoute` object. For more information, see "AdminPolicyBasedExternalRoute object configuration". 
  2. To create an admin policy based external route, enter the following command: 

```shell-session
$ oc create -f <file>.yaml
```


     * `<file>`: Specifies the name of the YAML file that you created in a previous step. 

**Example output**

```plaintext
adminpolicybasedexternalroute.k8s.ovn.org/default-route-policy created
```


  3. To confirm that the admin policy based external route was created, enter the following command: 

```shell-session
$ oc describe apbexternalroute <name> | tail -n 6
```


     * `<name>`: Specifies the name of the `AdminPolicyBasedExternalRoute` object. 

**Example output**

```plaintext
Status:
  Last Transition Time:  2023-04-24T15:09:01Z
  Messages:
  Configured external gateway IPs: 172.18.0.8
  Status:  Success
Events:  <none>
```
