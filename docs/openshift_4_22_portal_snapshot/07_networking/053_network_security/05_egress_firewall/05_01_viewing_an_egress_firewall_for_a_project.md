# 5.1. Viewing an egress firewall for a project

As a cluster administrator, you can list the names of any existing egress firewalls and view the traffic rules for a specific egress firewall. 

## 5.1.1. View an EgressFirewall custom resource (CR)

You can view an `EgressFirewall` CR in your cluster. 

**Prerequisites**

  * A cluster using the OVN-Kubernetes network plugin. 
  * Install the OpenShift Command-line Interface (CLI), commonly known as `oc`. 
  * You must log in to the cluster. 



**Procedure**

  1. Optional: To view the names of the `EgressFirewall` CR defined in your cluster, enter the following command: 

```shell-session
$ oc get egressfirewall --all-namespaces
```


  2. To inspect a policy, enter the following command. Replace `<policy_name>` with the name of the policy to inspect. 

```shell-session
$ oc describe egressfirewall <policy_name>
```


**Example output**

```shell-session
Name:		default
Namespace:	project1
Created:	20 minutes ago
Labels:		<none>
Annotations:	<none>
Rule:		Allow to 1.2.3.0/24
Rule:		Allow to www.example.com
Rule:		Deny to 0.0.0.0/0
```
