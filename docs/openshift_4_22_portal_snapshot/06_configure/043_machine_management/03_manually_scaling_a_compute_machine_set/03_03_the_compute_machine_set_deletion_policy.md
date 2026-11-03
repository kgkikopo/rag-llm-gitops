# 3.3. The compute machine set deletion policy

Compute machine sets can be configured to use the `Random`, `Newest`, and `Oldest` deletion options. The default is `Random`, meaning that random machines are chosen and deleted when scaling compute machine sets down. 

The deletion policy can be set according to the use case by modifying the particular compute machine set as in the following example: 

```yaml
spec:
  deletePolicy: <delete_policy>
  replicas: <desired_replica_count>
```


Specific machines can also be prioritized for deletion by adding the annotation `machine.openshift.io/delete-machine=true` to the machine of interest, regardless of the deletion policy. 

Important

By default, the OpenShift Container Platform router pods are deployed on workers. Because the router is required to access some cluster resources, including the web console, do not scale the worker compute machine set to `0` unless you first relocate the router pods. 

Note

Custom compute machine sets can be used for use cases requiring that services run on specific nodes and that those services are ignored by the controller when the worker compute machine sets are scaling down. This prevents service disruption.
