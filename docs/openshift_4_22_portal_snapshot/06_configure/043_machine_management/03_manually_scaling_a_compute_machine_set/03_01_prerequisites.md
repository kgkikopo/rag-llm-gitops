# 3.1. Prerequisites

* If you enabled the cluster-wide proxy and scale up compute machines not included in `networking.machineNetwork[].cidr` from the installation configuration, you must add the compute machines to the Proxy object’s `noProxy` field to prevent connection issues. See "Add the compute machines to the Proxy object’s `noProxy` field" for more information. 



Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API. 

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation. 

To view the platform type for your cluster, run the following command: 

```shell-session
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```
