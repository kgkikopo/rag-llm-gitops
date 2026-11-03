# 6.6. Cluster CAPI Operator

The Cluster CAPI Operator maintains the lifecycle of Cluster API resources. This Operator is responsible for all administrative tasks related to deploying the Cluster API project within an OpenShift Container Platform cluster. 

Note

This Operator is available as a [Technology Preview](https://access.redhat.com/support/offerings/techpreview) for Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Red Hat OpenStack Platform (RHOSP), and VMware vSphere clusters. 

## 6.6.1. CRDs

  * `awsmachines.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `awsmachine`

  * `gcpmachines.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `gcpmachine`

  * `azuremachines.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `azuremachine`

  * `openstackmachines.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `openstackmachine`

  * `vspheremachines.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `vspheremachine`

  * `metal3machines.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `metal3machine`

  * `awsmachinetemplates.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `awsmachinetemplate`

  * `gcpmachinetemplates.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `gcpmachinetemplate`

  * `azuremachinetemplates.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `azuremachinetemplate`

  * `openstackmachinetemplates.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `openstackmachinetemplate`

  * `vspheremachinetemplates.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `vspheremachinetemplate`

  * `metal3machinetemplates.infrastructure.cluster.x-k8s.io`

    * Scope: Namespaced 
    * CR: `metal3machinetemplate`




**Additional resources**

  * [cluster-capi-operator](https://github.com/openshift/cluster-capi-operator)
