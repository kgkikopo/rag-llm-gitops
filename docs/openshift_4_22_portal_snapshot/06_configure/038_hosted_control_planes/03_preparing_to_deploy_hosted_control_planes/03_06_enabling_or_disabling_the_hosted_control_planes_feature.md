# 3.6. Enabling or disabling the hosted control planes feature

The hosted control planes feature, as well as the `hypershift-addon` managed cluster add-on, are enabled by default. If needed, you can disable the feature, or if you disabled it, you can manually enable it. 

You can uninstall the HyperShift Operator and disable the hosted control planes feature. When you disable the hosted control planes feature, you must destroy the hosted cluster and the managed cluster resource on multicluster engine Operator, as described in the _Destroying a hosted cluster_ section. 

**Additional resources**

  * [Destroying a hosted cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/destroying-a-hosted-cluster#hcp-destroy-aws "16.1. Destroying a hosted cluster on AWS")



## 3.6.1. Manually enabling the hosted control planes feature

If the hosted control planes feature is disabled, you can manually enable it. 

**Procedure**

  1. Run the following command to enable the feature: 

```shell-session
$ oc patch mce multiclusterengine --type=merge -p \
  '{"spec":{"overrides":{"components":[{"name":"hypershift","enabled": true}]}}}'
```


The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`. 

  2. Run the following command to verify that the `hypershift` and `hypershift-local-hosting` features are enabled in the `MultiClusterEngine` custom resource: 

```shell-session
$ oc get mce multiclusterengine -o yaml
```


The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`. 

**Example output**

```yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  overrides:
    components:
    - name: hypershift
      enabled: true
    - name: hypershift-local-hosting
      enabled: true
```


## 3.6.2. Manually enabling the hypershift-addon managed cluster add-on for local-cluster

Enabling the hosted control planes feature automatically enables the `hypershift-addon` managed cluster add-on. If you need to enable the `hypershift-addon` managed cluster add-on manually, use the `hypershift-addon` to install the HyperShift Operator on `local-cluster`. 

**Procedure**

  1. Create the `ManagedClusterAddon` add-on named `hypershift-addon` by creating a file that resembles the following example: 

```yaml
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: ManagedClusterAddOn
metadata:
  name: hypershift-addon
  namespace: local-cluster
spec:
  installNamespace: open-cluster-management-agent-addon
```


  2. Apply the file by running the following command: 

```shell-session
$ oc apply -f <filename>
```


Replace `filename` with the name of the file that you created. 

  3. Confirm that the `hypershift-addon` managed cluster add-on is installed by running the following command: 

```shell-session
$ oc get managedclusteraddons -n local-cluster hypershift-addon
```


If the add-on is installed, the output resembles the following example: 

```shell-session
NAME               AVAILABLE   DEGRADED   PROGRESSING
hypershift-addon   True
```


Your `hypershift-addon` managed cluster add-on is installed and the hosting cluster is available to create and manage hosted clusters. 




## 3.6.3. Uninstalling the HyperShift Operator

Before you can disable the hosted control planes feature, you need to uninstall the HyperShift Operator and disable the `hypershift-addon` from the `local-cluster`. 

**Procedure**

  1. Run the following command to ensure that there is no hosted cluster running: 

```shell-session
$ oc get hostedcluster -A
```


Important

If a hosted cluster is running, the HyperShift Operator does not uninstall, even if the `hypershift-addon` is disabled. 

  2. Disable the `hypershift-addon` by running the following command: 

```shell-session
$ oc patch mce multiclusterengine --type=merge -p \
  '{"spec":{"overrides":{"components":[{"name":"hypershift-local-hosting","enabled": false}]}}}'
```


The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`. 

Note

You can also disable the `hypershift-addon` for the `local-cluster` from the multicluster engine Operator console after disabling the `hypershift-addon`. 




## 3.6.4. Disabling the hosted control planes feature

If you no longer use the hosted control planes feature, you can disable it. 

**Prerequisites**

  * You uninstalled the HyperShift Operator. For more information, see "Uninstalling the HyperShift Operator". 



**Procedure**

  1. Run the following command to disable the hosted control planes feature: 

```shell-session
$ oc patch mce multiclusterengine --type=merge -p \
  '{"spec":{"overrides":{"components":[{"name":"hypershift","enabled": false}]}}}'
```


The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`. 

  2. You can verify that the `hypershift` and `hypershift-local-hosting` features are disabled in the `MultiClusterEngine` custom resource by running the following command: 

```shell-session
$ oc get mce multiclusterengine -o yaml
```


The default `MultiClusterEngine` resource instance name is `multiclusterengine`, but you can get the `MultiClusterEngine` name from your cluster by running the following command: `$ oc get mce`. 

See the following example where `hypershift` and `hypershift-local-hosting` have their `enabled:` flags set to `false`: 

```yaml
apiVersion: multicluster.openshift.io/v1
kind: MultiClusterEngine
metadata:
  name: multiclusterengine
spec:
  overrides:
    components:
    - name: hypershift
      enabled: false
    - name: hypershift-local-hosting
      enabled: false
```
