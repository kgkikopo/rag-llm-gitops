# 8.2. Recommended configurable storage technology

Review the recommended and configurable storage technologies for the given OpenShift Container Platform cluster application. 

Table 8.1. Recommended and configurable storage technologyStorage type| Block| File| Object  
---|---|---|---  
ROX  |  Yes  |  Yes  |  Yes   
RWX  |  No  |  Yes  |  Yes   
Registry  |  Configurable  |  Configurable  |  Recommended   
Scaled registry  |  Not configurable  |  Configurable  |  Recommended   
Metrics  |  Recommended  |  Configurable  |  Not configurable   
Elasticsearch Logging  |  Recommended  |  Configurable  |  Not supported   
Loki Logging  |  Not configurable  |  Not configurable  |  Recommended   
Apps  |  Recommended  |  Recommended  |  Not configurable   
Show more

where: 

`ROX`
     Specifies `ReadOnlyMany` access mode. 
`ROX.Yes`
     Specifies that this access mode 
`RWX`
     Specifies `ReadWriteMany` access mode. 
`Metrics`
     Specifies Prometheus as the underlying technology used for metrics. 
`Metrics.Configurable`
     For metrics, using file storage with the `ReadWriteMany` (RWX) access mode is unreliable. If you use file storage, do not configure the RWX access mode on any persistent volume claims (PVCs) that are configured for use with metrics. 
`Elasticsearch Logging.Configurable`
     For logging, review the recommended storage solution in Configuring persistent storage for the log store section. Using NFS storage as a persistent volume or through NAS, such as Gluster, can corrupt the data. Therefore, NFS is not supported for Elasticsearch storage and LokiStack log store in OpenShift Container Platform Logging. You must use one persistent volume type per log store. 
`Apps.Not configurable`
     Specifies that object storage is not consumed through PVs or PVCs of OpenShift Container Platform. Apps must integrate with the object storage REST API. 

Note

A scaled registry is an OpenShift image registry where two or more pod replicas are running.
