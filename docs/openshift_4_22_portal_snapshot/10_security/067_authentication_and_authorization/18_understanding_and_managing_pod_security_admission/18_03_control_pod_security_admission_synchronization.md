# 18.3. Control pod security admission synchronization

To customize which namespaces have their pod security admission labels automatically updated, you can enable or disable synchronization for most namespaces. 

Important

You cannot enable pod security admission synchronization on some system-created namespaces. For more information, see _Pod security admission synchronization namespace exclusions_. 

**Procedure**

  * For each namespace that you want to configure, set a value for the `security.openshift.io/scc.podSecurityLabelSync` label: 

    * To disable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `false`. 

Run the following command: 

```shell-session
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=false
```


    * To enable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `true`. 

Run the following command: 

```shell-session
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=true
```


Note

Use the `--overwrite` flag to overwrite the value if this label is already set on the namespace. 




**Additional resources**

  * [Pod security admission synchronization namespace exclusions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/understanding-and-managing-pod-security-admission#security-context-constraints-psa-sync-exclusions_understanding-and-managing-pod-security-admission "18.2.1. Pod security admission synchronization namespace exclusions")
