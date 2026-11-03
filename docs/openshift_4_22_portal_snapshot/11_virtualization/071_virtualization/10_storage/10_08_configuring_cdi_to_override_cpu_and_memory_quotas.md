# 10.8. Configuring CDI to override CPU and memory quotas

You can configure the Containerized Data Importer (CDI) to import, upload, and clone virtual machine disks into namespaces that are subject to CPU and memory resource restrictions. 

## 10.8.1. About CPU and memory quotas in a namespace

A _resource quota_ , defined by the `ResourceQuota` object, imposes restrictions on a namespace that limit the total amount of compute resources that can be consumed by resources within that namespace. 

The `HyperConverged` custom resource (CR) defines the user configuration for the Containerized Data Importer (CDI). The CPU and memory request and limit values are set to a default value of `0`. This ensures that pods created by CDI that do not specify compute resource requirements are given the default values and are allowed to run in a namespace that is restricted with a quota. 

## 10.8.2. Overriding CPU and memory defaults

Modify the default settings for CPU and memory requests and limits for your use case by adding the `spec.resourceRequirements.storageWorkloads` stanza to the `HyperConverged` custom resource (CR). 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `HyperConverged` CR by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  2. Add the `spec.resourceRequirements.storageWorkloads` stanza to the CR, setting the values based on your use case. For example: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  resourceRequirements:
    storageWorkloads:
      limits:
        cpu: "500m"
        memory: "2Gi"
      requests:
        cpu: "250m"
        memory: "1Gi"
```


  3. Save and exit the editor to update the `HyperConverged` CR. 



## 10.8.3. Additional resources

  * [Resource quotas per project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#quotas-setting-per-project)
