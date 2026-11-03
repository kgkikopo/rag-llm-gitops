# Chapter 5. RuntimeClass [node.k8s.io/v1]

Description
     RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod. For more details, see <https://kubernetes.io/docs/concepts/containers/runtime-class/>
Type
     `object`
Required
    

  * `handler`

- [5.1. Specification](05_01_specification.md)
- [5.2. API endpoints](05_02_api_endpoints.md)
