# 6.12. Developer catalog and sub-catalog customization

As a cluster administrator, you have the ability to organize and manage the Developer catalog or its sub-catalogs. You can enable or disable the sub-catalog types or disable the entire developer catalog. 

The `developerCatalog.types` object includes the following parameters that you must define in a snippet to use them in the YAML view: 

  * `state`: Defines if a list of developer catalog types should be enabled or disabled. 
  * `enabled`: Defines a list of developer catalog types (sub-catalogs) that are visible to users. 
  * `disabled`: Defines a list of developer catalog types (sub-catalogs) that are not visible to users. 



You can enable or disable the following developer catalog types (sub-catalogs) using the YAML view or the form view. 

  * `Builder Images`
  * `Templates`
  * `Devfiles`
  * `Samples`
  * `Helm Charts`
  * `Event Sources`
  * `Event Sinks`
  * `Operator Backed`



## 6.12.1. Customize a developer catalog or its sub-catalogs using the YAML view

You can customize a developer catalog by editing the YAML content in the YAML view. 

**Prerequisites**

  * An OpenShift web console session with cluster administrator privileges. 



**Procedure**

  1. In the **Administrator** perspective of the web console, navigate to **Administration** **Cluster Settings**. 
  2. Select the **Configuration** tab, click the **Console (operator.openshift.io)** resource and view the **Details** page. 
  3. Click the **YAML** tab to open the editor and edit the YAML content as needed. 

For example, to disable a developer catalog type, insert the following snippet that defines a list of disabled developer catalog resources: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Disabled
        disabled:
          - BuilderImage
          - Devfile
          - HelmChart
...
```


  4. Click **Save**. 

Note

By default, the developer catalog types are enabled in the Administrator view of the Web Console. 




### 6.12.1.1. Example YAML file changes

You can customize a developer catalog by dynamically editing YAML content in the YAML editor. 

Use the following snippet to display all the sub-catalogs by setting the _state_ type to **Enabled**. 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
```


Use the following snippet to disable all sub-catalogs by setting the _state_ type to **Disabled** : 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Disabled
```


Use the following snippet when a cluster administrator defines a list of sub-catalogs, which are enabled in the Web Console. 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
        enabled:
          - BuilderImage
          - Devfile
          - HelmChart
          - ...
```


## 6.12.2. Customize a developer catalog or its sub-catalogs using the form view

You can customize a developer catalog by using the form view in the Web Console. 

**Prerequisites**

  * An OpenShift web console session with cluster administrator privileges. 
  * The Developer perspective is enabled. 



**Procedure**

  1. In the **Administrator** perspective, navigate to **Administration** **Cluster Settings**. 
  2. Select the **Configuration** tab and click the **Console (operator.openshift.io)** resource. 
  3. Click **Actions** **Customize**. 
  4. Enable or disable items in the **Pre-pinned navigation items** , **Add page** , and **Developer Catalog** sections. 

**Verification**

After you have customized the developer catalog, your changes are automatically saved in the system and take effect in the browser after a refresh. 

![Developer catalog customization options in the form view](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/e4e3156b9ff5dfbfbe6845fbdd7d47e9/odc_customizing_developer_catalog.png) ![Developer catalog customization options in the form view](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Web_console-en-US/images/e4e3156b9ff5dfbfbe6845fbdd7d47e9/odc_customizing_developer_catalog.png)




Note

As an administrator, you can define the navigation items that appear by default for all users. You can also reorder the navigation items. 

Tip

You can use a similar procedure to customize Web UI items such as Quick starts, Cluster roles, and Actions.
