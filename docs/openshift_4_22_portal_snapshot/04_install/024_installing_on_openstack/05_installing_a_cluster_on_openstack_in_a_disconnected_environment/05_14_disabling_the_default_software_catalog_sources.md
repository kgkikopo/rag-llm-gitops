# 5.14. Disabling the default software catalog sources

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator. 

**Procedure**

  * Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object: 

```shell-session
$ oc patch OperatorHub cluster --type json \
    -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
```


Tip

Or, you can use the web console to manage catalog sources. From the **Administration** **Cluster Settings** **Configuration** **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.
