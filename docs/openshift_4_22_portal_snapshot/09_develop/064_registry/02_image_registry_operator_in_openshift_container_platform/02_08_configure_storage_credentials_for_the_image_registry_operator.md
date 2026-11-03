# 2.8. Configure storage credentials for the Image Registry Operator

In addition to the `configs.imageregistry.operator.openshift.io` Custom Resource (CR) and ConfigMap resources, storage credential configuration is provided to the Operator by a separate secret resource. This resource is located within the `openshift-image-registry` namespace. 

You can create an `image-registry-private-configuration-user` secret that in turn creates custom credentials needed for storage access and management. If default credentials exist, the custom credentials override the default credentials used by the Operator. 

**Procedure**

  * Create an OpenShift Container Platform secret that contains the required keys. 

```shell-session
$ oc create secret generic image-registry-private-configuration-user --from-literal=KEY1=value1 --from-literal=KEY2=value2 --namespace openshift-image-registry
```
