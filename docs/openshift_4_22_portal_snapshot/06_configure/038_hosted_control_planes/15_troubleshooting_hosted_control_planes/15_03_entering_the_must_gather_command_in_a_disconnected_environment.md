# 15.3. Entering the must-gather command in a disconnected environment

When you need to troubleshoot an issue in a disconnected environment, you can gather information by running the `must-gather` command. The command generates output for the management cluster and the hosted cluster. 

**Procedure**

  1. In a disconnected environment, mirror the Red Hat Operator catalog images into their mirror registry. For more information, see "Install on disconnected networks". 
  2. Run the following command to extract logs that reference the image from their mirror registry: 

```shell-session
REGISTRY=registry.example.com:5000
IMAGE=$REGISTRY/rhacm2/acm-must-gather-rhel9:v2.17

$ oc adm must-gather \
  --image=$IMAGE /usr/bin/gather \
  hosted-cluster-namespace=HOSTEDCLUSTERNAMESPACE \
  hosted-cluster-name=HOSTEDCLUSTERNAME \
  --dest-dir=./data
```


**Additional resources**

  * [Install on disconnected networks](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/clusters/cluster_mce_overview#install-on-disconnected-networks)
