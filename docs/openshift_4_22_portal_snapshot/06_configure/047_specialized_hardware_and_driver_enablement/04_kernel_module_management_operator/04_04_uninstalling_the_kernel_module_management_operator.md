# 4.4. Uninstalling the Kernel Module Management Operator

You can uninstall the Kernel Module Management (KMM) Operator from OpenShift Container Platform by using CLI or uninstalling the Operator. 

## 4.4.1. Uninstalling a Red Hat catalog installation

To uninstall a Kernel Module Management (KMM) Operator installation from the Red Hat catalog on OpenShift Container Platform, you can remove the Operator from **Installed Operators** in the web console. 

**Procedure**

  * Use the OpenShift console under **Operators** -→ **Installed Operators** to locate and uninstall the Operator. 

Note

Alternatively, you can delete the `Subscription` resource in the KMM namespace. 




## 4.4.2. Uninstalling a CLI installation

To uninstall a Kernel Module Management (KMM) Operator CLI installation from OpenShift Container Platform, you can run `oc delete -k` against the upstream configuration manifest. 

**Procedure**

  * Run the following command to uninstall the KMM Operator: 

```shell-session
$ oc delete -k https://github.com/rh-ecosystem-edge/kernel-module-management/config/default
```


Note

Using this command deletes the `Module` CRD and all `Module` instances in the cluster.
