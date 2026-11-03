# 8.1. OpenShift Container Platform Ingress Operator

When you create your OpenShift Container Platform cluster, pods and services running on the cluster are each allocated their own IP addresses. The IP addresses are accessible to other pods and services running nearby but are not accessible to outside clients. 

The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) to handle routing. You can use the Ingress Operator to route traffic by specifying OpenShift Container Platform `Route` and Kubernetes `Ingress` resources. Configurations within the Ingress Controller, such as the ability to define `endpointPublishingStrategy` type and internal load balancing, provide ways to publish Ingress Controller endpoints.
