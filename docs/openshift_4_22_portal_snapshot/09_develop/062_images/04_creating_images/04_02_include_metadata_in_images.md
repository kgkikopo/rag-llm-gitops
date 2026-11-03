# 4.2. Include metadata in images

Define comprehensive image metadata during creation to ensure OpenShift Container Platform correctly configures image runtime settings and tracks image lineage and compliance. This helps to provide a better experience for developers using your image. 

For example, you can add metadata to provide helpful descriptions of your image, or offer suggestions on other images that may also be needed. 

This topic only defines the metadata needed by the current set of use cases. Additional metadata or use cases may be added in the future. 

## 4.2.1. Defining image metadata

You can use the `LABEL` instruction in a `Dockerfile` to define image metadata. Labels are similar to environment variables in that they are key value pairs attached to an image or a container. Labels are different from environment variable in that they are not visible to the running application and they can also be used for fast look-up of images and containers. 

For more information on the `LABEL` instruction, see "LABEL - Docker documentation". 

The label names are typically namespaced. The namespace is set accordingly to reflect the project that is going to pick up the labels and use them. For OpenShift Container Platform the namespace is set to `io.openshift` and for Kubernetes the namespace is `io.k8s`. 

See the "Docker custom metadata" documentation for details about the format. 

Table 4.1. Supported MetadataVariable| Description  
---|---  
`io.openshift.tags` |  This label contains a list of tags represented as a list of comma-separated string values. The tags are the way to categorize the container images into broad areas of functionality. Tags help UI and generation tools to suggest relevant container images during the application creation process.  `LABEL io.openshift.tags mongodb,mongodb24,nosql`  
`io.openshift.wants` |  Specifies a list of tags that the generation tools and the UI uses to provide relevant suggestions if you do not have the container images with specified tags already. For example, if the container image wants `mysql` and `redis` and you do not have the container image with `redis` tag, then UI can suggest you to add this image into your deployment.  `LABEL io.openshift.wants mongodb,redis`  
`io.k8s.description` |  This label can be used to give the container image consumers more detailed information about the service or functionality this image provides. The UI can then use this description together with the container image name to provide more human friendly information to end users.  `LABEL io.k8s.description The MySQL 5.5 Server with master-slave replication support`  
`io.openshift.non-scalable` |  An image can use this variable to suggest that it does not support scaling. The UI then communicates this to consumers of that image. Being not-scalable means that the value of `replicas` should initially not be set higher than `1`.  `LABEL io.openshift.non-scalable true`  
`io.openshift.min-memory` and `io.openshift.min-cpu` |  This label suggests how much resources the container image needs to work properly. The UI can warn the user that deploying this container image may exceed their user quota. The values must be compatible with Kubernetes quantity.  `LABEL io.openshift.min-memory 16Gi LABEL io.openshift.min-cpu 4`  
Show more

## 4.2.2. Additional resources

  * [LABEL - Docker documentation](https://docs.docker.com/engine/reference/builder/#label)
  * [Docker custom metadata](https://docs.docker.com/engine/userguide/labels-custom-metadata)
