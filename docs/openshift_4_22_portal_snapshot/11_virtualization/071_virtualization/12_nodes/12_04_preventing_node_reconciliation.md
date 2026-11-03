# 12.4. Preventing node reconciliation

Use `skip-node` annotation to prevent the `node-labeller` from reconciling a node. 

## 12.4.1. Skip node labeling reconciliation

If you want the `node-labeller` to skip a node, annotate that node by using the OpenShift CLI (`oc`). 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Annotate the node that you want to skip by running the following command: 

```shell-session
$ oc annotate node <node_name> node-labeller.kubevirt.io/skip-node=true
```


Replace `<node_name>` with the name of the relevant node to skip. 

Reconciliation resumes on the next cycle after the node annotation is removed or set to false. 




## 12.4.2. Additional resources

  * [Managing node labeling for obsolete CPU models](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/nodes#virt-managing-node-labeling-obsolete-cpu-models "12.3. Managing node labeling for obsolete CPU models")
