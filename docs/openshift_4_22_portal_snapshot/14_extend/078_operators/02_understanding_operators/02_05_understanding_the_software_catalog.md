# 2.5. Understanding the software catalog

The software catalog in OpenShift Container Platform provides a web console interface for discovering, installing, and managing Operators through Operator Lifecycle Manager (OLM). 

## 2.5.1. About the software catalog

The _software catalog_ is the web console interface in OpenShift Container Platform that cluster administrators use to discover and install Operators. 

With one click, an Operator can be pulled from its off-cluster source, installed and subscribed on the cluster, and made ready for engineering teams to self-service manage the product across deployment environments using Operator Lifecycle Manager (OLM). 

Cluster administrators can choose from catalogs grouped into the following categories: 

Category| Description  
---|---  
Red Hat Operators  |  Red Hat products packaged and shipped by Red Hat. Supported by Red Hat.   
Certified Operators  |  Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV.   
Community Operators  |  Optionally-visible software maintained by relevant representatives in the community Operators GitHub repository. No official support.   
Custom Operators  |  Operators you add to the cluster yourself. If you have not added any custom Operators, the **Custom** category does not appear in the web console software catalog.   
Show more

Operators in the software catalog are packaged to run on OLM. This includes a YAML file called a cluster service version (CSV) containing all of the CRDs, RBAC rules, deployments, and container images required to install and securely run the Operator. It also contains user-visible information like a description of its features and supported Kubernetes versions. 

## 2.5.2. Software catalog architecture

The software catalog UI component is driven by the Marketplace Operator by default on OpenShift Container Platform in the `openshift-marketplace` namespace. 

### 2.5.2.1. OperatorHub custom resource

The Marketplace Operator manages an `OperatorHub` custom resource (CR) named `cluster` that manages the default `CatalogSource` objects provided with the software catalog. You can modify this resource to enable or disable the default catalogs, which is useful when configuring OpenShift Container Platform in restricted network environments. 

**Example`OperatorHub` custom resource**

```yaml
apiVersion: config.openshift.io/v1
kind: OperatorHub
metadata:
  name: cluster
spec:
  disableAllDefaultSources: true
  sources: [
    {
      name: "community-operators",
      disabled: false
    }
  ]
```


\+ where: 

`spec.disableAllDefaultSources`
     Controls availability of all default catalogs that are configured by default during an OpenShift Container Platform installation. Setting to `true` disables all default catalog sources. 
`spec.sources`
     Disables default catalogs individually by changing the `disabled` parameter value per source. 

## 2.5.3. Additional resources

  * [Catalog source](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-catalogsource_olm-understanding-olm "2.4.1.2.2. Catalog source")
  * [Operator installation and upgrade workflow in OLM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/understanding-operators#olm-upgrades_olm-workflow "2.4.3.1. Operator installation and upgrade workflow in OLM")
  * [Red Hat Partner Connect](https://connect.redhat.com)
