# 16.2. Destroying a hosted cluster on bare metal

You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve. 

## 16.2.1. Destroying a hosted cluster on bare metal by using the CLI

If you created a hosted cluster by using the command-line interface (CLI), you can destroy that hosted cluster and its back-end resources by running a command. 

**Procedure**

  * Delete the hosted cluster and its back-end resources by running the following command: 

```shell-session
$ oc delete -f <hosted_cluster_config>.yaml
```


Specify the name of the configuration YAML file that was rendered when you created the hosted cluster. 

Note

If you created the hosted cluster without specifying the `--render` and `--render-sensitive` flags in its configuration file, you must remove its back-end resources manually. 




## 16.2.2. Destroying a hosted cluster on bare metal by using the web console

You can use the multicluster engine Operator web console to destroy a hosted cluster on bare metal. 

**Procedure**

  1. In the console, click **Infrastructure** **Clusters**. 
  2. On the **Clusters** page, select the cluster that you want to destroy. 
  3. In the **Actions** menu, select **Destroy clusters** to remove the cluster.
