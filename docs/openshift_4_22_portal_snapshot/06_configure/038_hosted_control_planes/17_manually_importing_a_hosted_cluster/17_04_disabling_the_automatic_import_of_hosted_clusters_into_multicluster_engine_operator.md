# 17.4. Disabling the automatic import of hosted clusters into multicluster engine Operator

Hosted clusters are automatically imported into multicluster engine Operator after the control plane becomes available. If needed, you can disable the automatic import of hosted clusters. 

Any hosted clusters that were previously imported are not affected, even if you disable automatic import. When you upgrade to multicluster engine Operator 2.5 and automatic import is enabled, all hosted clusters that are not imported are automatically imported if their control planes are available. 

Note

If Red Hat Advanced Cluster Management is installed, all Red Hat Advanced Cluster Management add-ons are also enabled. 

When automatic import is disabled, only newly created hosted clusters are not automatically imported. Hosted clusters that were already imported are not affected. You can still manually import clusters by using the console or by creating the `ManagedCluster` and `KlusterletAddonConfig` custom resources. 

**Procedure**

  1. On the hub cluster, open the `hypershift-addon-deploy-config` specification that is in the `AddonDeploymentConfig` resource in the namespace where multicluster engine Operator is installed by entering the following command: 

```shell-session
$ oc edit addondeploymentconfig hypershift-addon-deploy-config \
  -n multicluster-engine
```


  2. In the `spec.customizedVariables` section, add the `autoImportDisabled` variable with value of `"true"`, as shown in the following example: 

```yaml
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: AddOnDeploymentConfig
metadata:
  name: hypershift-addon-deploy-config
  namespace: multicluster-engine
spec:
  customizedVariables:
   - name: hcMaxNumber
     value: "80"
  - name: hcThresholdNumber
    value: "60"
  - name: autoImportDisabled
    value: "true"
```


  3. To re-enable automatic import, set the value of the `autoImportDisabled` variable to `"false"` or remove the variable from the `AddonDeploymentConfig` resource.
