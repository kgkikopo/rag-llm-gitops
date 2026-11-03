# 17.2. Manually importing hosted clusters

Typically, hosted clusters are automatically imported to multicluster engine Operator after the hosted control plane becomes available. However, you can import hosted clusters manually as required. 

**Procedure**

  1. In the console, click **Infrastructure** **Clusters** and select the hosted cluster that you want to import. 
  2. Click **Import hosted cluster**. 

Note

For your _discovered_ hosted cluster, you can also import from the console, but the cluster must be in an upgradeable state. Import on your cluster is disabled if the hosted cluster is not in an upgradeable state because the hosted control plane is not available. Click **Import** to begin the process. The status is `Importing` while the cluster receives updates and then changes to `Ready`.
