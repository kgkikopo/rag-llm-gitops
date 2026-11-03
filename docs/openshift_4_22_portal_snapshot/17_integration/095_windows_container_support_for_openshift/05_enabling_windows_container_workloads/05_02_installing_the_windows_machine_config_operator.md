# 5.2. Installing the Windows Machine Config Operator

You can install the Windows Machine Config Operator using either the web console or OpenShift CLI (`oc`). 

Note

Due to a limitation within the Windows operating system, `clusterNetwork` CIDR addresses of class E, such as `240.0.0.0`, are not compatible with Windows nodes. 

## 5.2.1. Install the Windows Machine Config Operator by using the web console

You can use the OpenShift Container Platform web console to install the Windows Machine Config Operator (WMCO). 

Note

Dual NIC is not supported on WMCO-managed Windows instances. 

**Procedure**

  1. From the **Administrator** perspective in the OpenShift Container Platform web console, navigate to the **Ecosystem** **Software Catalog** page. 
  2. Use the **Filter by keyword** box to search for `Windows Machine Config Operator` in the catalog. Click the **Windows Machine Config Operator** tile. 
  3. Review the information about the Operator and click **Install**. 
  4. On the **Install Operator** page: 

     1. Select the **stable** channel as the **Update Channel**. The **stable** channel enables the latest stable release of the WMCO to be installed. 
     2. The **Installation Mode** is preconfigured because the WMCO must be available in a single namespace only. 
     3. Choose the **Installed Namespace** for the WMCO. The default Operator recommended namespace is `openshift-windows-machine-config-operator`. 
     4. Click the **Enable Operator recommended cluster monitoring on the Namespace** checkbox to enable cluster monitoring for the WMCO. 
     5. Select an **Approval Strategy**. 

        * The **Automatic** strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available. 
        * The **Manual** strategy requires a user with appropriate credentials to approve the Operator update. 

  5. Click **Install**. The WMCO is now listed on the **Installed Operators** page. 

Note

The WMCO is installed automatically into the namespace you defined, like `openshift-windows-machine-config-operator`. 

  6. Verify that the **Status** shows **Succeeded** to confirm successful installation of the WMCO. 



## 5.2.2. Install the Windows Machine Config Operator by using the CLI

You can use the OpenShift CLI (`oc`) to install the Windows Machine Config Operator (WMCO). 

Note

Dual NIC is not supported on WMCO-managed Windows instances. 

**Procedure**

  1. Create a namespace for the WMCO. 

     1. Create a `Namespace` object YAML file for the WMCO. For example, `wmco-namespace.yaml`: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-windows-machine-config-operator
  labels:
    openshift.io/cluster-monitoring: "true"
```


where 

`metadata.name`
     Specifies the namespace to create the secret. You should deploy the WMCO in the `openshift-windows-machine-config-operator` namespace. 
`metadata.labels`
     Specifies the label required for enabling cluster monitoring for the WMCO. 

     2. Create the namespace: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f wmco-namespace.yaml
```


  2. Create the Operator group for the WMCO. 

     1. Create an `OperatorGroup` object YAML file. For example, `wmco-og.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: windows-machine-config-operator
  namespace: openshift-windows-machine-config-operator
spec:
  targetNamespaces:
  - openshift-windows-machine-config-operator
```


     2. Create the Operator group: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f wmco-og.yaml
```


  3. Subscribe the namespace to the WMCO. 

     1. Create a `Subscription` object YAML file. For example, `wmco-sub.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: windows-machine-config-operator
  namespace: openshift-windows-machine-config-operator
spec:
  channel: "stable"
  installPlanApproval: "Automatic"
  name: "windows-machine-config-operator"
  source: "redhat-operators"
  sourceNamespace: "openshift-marketplace"
```


where: 

`spec.channel`
     Specifies `stable` as the channel. 
`spec.installPlanApproval`
     Specifies an approval strategy. You can set `Automatic` or `Manual`. 
`spec.source`
     Specifies the `redhat-operators` catalog source, which contains the `windows-machine-config-operator` package manifests. If your OpenShift Container Platform is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator LifeCycle Manager (OLM). 
`spec.sourceNamespace`
     Specifies the namespace of the catalog source. Use `openshift-marketplace` for the default software catalog sources. 

     2. Create the subscription: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f wmco-sub.yaml
```


The WMCO is now installed to the `openshift-windows-machine-config-operator`. 

  4. Verify the WMCO installation: 

```shell-session
$ oc get csv -n openshift-windows-machine-config-operator
```


**Example output**

```shell-session
NAME                                    DISPLAY                           VERSION   REPLACES   PHASE
windows-machine-config-operator.2.0.0   Windows Machine Config Operator   2.0.0                Succeeded
```
