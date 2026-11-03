# 17.3. Manually importing a hosted cluster on AWS

You can import a hosted cluster on Amazon Web Services (AWS) with the command-line interface. 

**Procedure**

  1. Create your `ManagedCluster` resource by using the following sample YAML file: 

```yaml
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  annotations:
    import.open-cluster-management.io/hosting-cluster-name: local-cluster
    import.open-cluster-management.io/klusterlet-deploy-mode: Hosted
    open-cluster-management/created-via: hypershift
  labels:
    cloud: auto-detect
    cluster.open-cluster-management.io/clusterset: default
    name: <hosted_cluster_name>
    vendor: OpenShift
  name: <hosted_cluster_name>
spec:
  hubAcceptsClient: true
  leaseDurationSeconds: 60
```


Replace `<hosted_cluster_name>` with the name of your hosted cluster. 

  2. Run the following command to apply the resource: 

```shell-session
$ oc apply -f <file_name>
```


Replace `<file_name>` with the YAML file name you created in the previous step. 

  3. If you have Red Hat Advanced Cluster Management installed, create your `KlusterletAddonConfig` resource by using the following sample YAML file. If you have installed multicluster engine Operator only, skip this step: 

```yaml
apiVersion: agent.open-cluster-management.io/v1
kind: KlusterletAddonConfig
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  clusterName: <hosted_cluster_name>
  clusterNamespace: <hosted_cluster_namespace>
  clusterLabels:
    cloud: auto-detect
    vendor: auto-detect
  applicationManager:
    enabled: true
  certPolicyController:
    enabled: true
  iamPolicyController:
    enabled: true
  policyController:
    enabled: true
  searchCollector:
    enabled: false
```


     * Replace `<hosted_cluster_name>` with the name of your hosted cluster. 
     * Replace `<hosted_cluster_namespace>` with the name of your hosted cluster namespace. 

  4. Run the following command to apply the resource: 

```shell-session
$ oc apply -f <file_name>
```


Replace `<file_name>` with the name of the YAML that you created in the previous step. 

  5. After the import process is complete, your hosted cluster becomes visible in the console. You can also check the status of your hosted cluster by running the following command: 

```shell-session
$ oc get managedcluster <hosted_cluster_name>
```
