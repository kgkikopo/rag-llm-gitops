# 1.14. IngressController [operator.openshift.io/v1]

Description
    

IngressController describes a managed ingress controller for the cluster. The controller can service OpenShift Route and Kubernetes Ingress resources. 

When an IngressController is created, a new ingress controller deployment is created to allow external traffic to reach the services that expose Ingress or Route resources. Updating this resource may lead to disruption for public facing network connections as a new ingress controller revision may be rolled out. 

<https://kubernetes.io/docs/concepts/services-networking/ingress-controllers>

Whenever possible, sensible defaults for the platform are used. See each field for more details. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
