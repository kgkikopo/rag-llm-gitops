# 2.1. Image Registry on cloud platforms and OpenStack

The Image Registry Operator installs a single instance of the OpenShift image registry and manages all registry configuration, including setting up registry storage. 

Note

Storage is only automatically configured when you install an installer-provisioned infrastructure cluster on AWS, Azure, Google Cloud, IBM®, or RHOSP. 

When you install or upgrade an installer-provisioned infrastructure cluster on AWS, Azure, Google Cloud, IBM®, or RHOSP, the Image Registry Operator sets the `spec.storage.managementState` parameter to `Managed`. If the `spec.storage.managementState` parameter is set to `Unmanaged`, the Image Registry Operator takes no action related to storage. 

After the control plane deploys in the management cluster, the Operator creates a default `configs.imageregistry.operator.openshift.io` custom resource (CR) instance based on configuration detected in the cluster. 

If insufficient information is available to define a complete `configs.imageregistry.operator.openshift.io` CR, the incomplete resource is defined and the Operator updates the resource status with information about what is missing. 

Important

The Image Registry Operator’s behavior for managing the pruner is orthogonal to the `managementState` specified on the `ClusterOperator` object for the Image Registry Operator. If the Image Registry Operator is not in the `Managed` state, the image pruner can still be configured and managed by the `Pruning` custom resource. 

However, the `managementState` of the Image Registry Operator alters the behavior of the deployed image pruner job: 

  * `Managed`: the `--prune-registry` flag for the image pruner is set to `true`. 
  * `Removed`: the `--prune-registry` flag for the image pruner is set to `false`, meaning the image pruner job only prunes image metadata in etcd.
