# 1.2. Storage types

OpenShift Container Platform storage is broadly classified into two categories, namely ephemeral storage and persistent storage. 

## 1.2.1. Ephemeral storage

Pods and containers are ephemeral or transient in nature and designed for stateless applications. Ephemeral storage allows administrators and developers to better manage the local storage for some of their operations. 

## 1.2.2. Persistent storage

Stateful applications deployed in containers require persistent storage. OpenShift Container Platform uses a pre-provisioned storage framework called persistent volumes (PV) to allow cluster administrators to provision persistent storage. The data inside these volumes can exist beyond the lifecycle of an individual pod. Developers can use persistent volume claims (PVCs) to request storage requirements. 

**Additional resources**

  * [Understanding ephemeral storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-ephemeral-storage "Chapter 2. Understanding ephemeral storage")
  * [Understanding persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-persistent-storage "Chapter 3. Understanding persistent storage")
