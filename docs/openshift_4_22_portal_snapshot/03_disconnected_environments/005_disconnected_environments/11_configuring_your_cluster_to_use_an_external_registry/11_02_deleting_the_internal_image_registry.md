# 11.2. Deleting the internal image registry

You can complete configuring your cluster to use an external image registry by deleting the resource responsible for maintaining the internal image registry that was installed on your cluster. 

**Prerequisites**

  * You installed your cluster using the method described in "Installing a cluster without an external registry". 
  * You have successfully performed a cluster update using images mirrored to your external image registry. You can ensure that your cluster has been updated to this new version by running the `oc get clusterversion` command. 

Important

The version you updated your cluster to must not be listed in the `status.releases` field of the `InternalReleaseImage` custom resource (CR). You can check the contents of the CR by running the `oc get InternalReleaseImage -o yaml` command. 




**Procedure**

  * Delete the singleton `InternalReleaseImage` CR by running the following command: 

```shell-session
$ oc delete internalreleaseimages cluster
```


**Additional resources**

  * [Installing a cluster without an external registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-ove)
