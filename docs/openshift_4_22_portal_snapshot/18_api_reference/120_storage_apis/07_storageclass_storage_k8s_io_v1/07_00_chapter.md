# Chapter 7. StorageClass [storage.k8s.io/v1]

Description
    

StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned. 

StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name. 

Type
     `object`
Required
    

  * `provisioner`

- [7.1. Specification](07_01_specification.md)
- [7.2. API endpoints](07_02_api_endpoints.md)
