# 5.24. Container registry reference CRs

The following custom resources (CRs) configure the container registry for the telco hub cluster. 

Table 5.10. Container registry CRsComponent| Reference CR| Description| Optional  
---|---|---|---  
Registry  |  `catalog-source.yaml` |  Defines a `CatalogSource` CR for mirrored Operator catalogs.  |  No   
Registry  |  `idms-operator.yaml` |  Defines an image digest `MirrorSet` Operator CR for mirrored Operator images.  |  No   
Registry  |  `idms-release.yaml` |  Defines an image digest `MirrorSet` CR for OpenShift Container Platform release images.  |  No   
Registry  |  `image-config.yaml` |  Defines an image configuration CR to manage image registries and policies.  |  No   
Registry  |  `itms-generic.yaml` |  Defines an image tag `MirrorSet` CR for mirrored images in a disconnected registry.  |  No   
Registry  |  `itms-release.yaml` |  Defines an image tag `MirrorSet` CR for OpenShift Container Platform release images.  |  No   
Registry  |  `kustomization.yaml` |  Defines a `Kustomization` manifest for registry-related CRs.  |  No   
Registry  |  `operator-hub.yaml` |  Configures the `OperatorHub` CR for offline catalog sources.  |  No   
Registry  |  `registry-ca.yaml` |  Defines a `ConfigMap` CR containing registry CA certificates.  |  No   
Show more
