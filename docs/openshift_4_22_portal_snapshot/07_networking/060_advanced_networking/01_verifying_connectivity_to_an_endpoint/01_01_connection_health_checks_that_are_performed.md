# 1.1. Connection health checks that are performed

Establish TCP connections to target services, endpoints, and load balancers to verify that control plane components, routing layers, and node services can communicate without interruption. 

To verify that cluster resources are reachable, a TCP connection is made to each of the following cluster API services: 

  * Kubernetes API server service 
  * Kubernetes API server endpoints 
  * OpenShift API server service 
  * OpenShift API server endpoints 
  * Load balancers 



To verify that services and service endpoints are reachable on every node in the cluster, a TCP connection is made to each of the following targets: 

  * Health check target service 
  * Health check target endpoints
