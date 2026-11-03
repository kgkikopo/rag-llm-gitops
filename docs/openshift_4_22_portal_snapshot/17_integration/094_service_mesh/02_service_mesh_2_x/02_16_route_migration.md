# 2.16. Route migration

Automatic route creation, also known as Istio OpenShift Routing (IOR), is a deprecated feature that is disabled by default for any `ServiceMeshControlPlane` resource that was created using Red Hat OpenShift Service Mesh 2.5 and later. Migrating from IOR to explicitly-managed routes provides a more flexible way to manage and configure ingress gateways. When route resources are explicitly created they can be managed alongside the other gateway and application resources as part of a GitOps management model. 

## 2.16.1. Migrating from Istio OpenShift Routing to explicitly-managed routes

This procedure explains how to disable Istio OpenShift Routing (IOR) in Red Hat OpenShift Service Mesh, and how to continue to use and manage Routes that were originally created using IOR. This procedure also provides an example of how to explicitly create a new Route targeting an existing gateway `Service` object. 

**Prerequisites**

  * Before migrating to explicitly-managed routes, export the existing route configurations managed by Istio OpenShift Routing (IOR) to files. Save the files so that in the future you can recreate the route configurations without requiring IOR. 



**Procedure**

  * Modify the `ServiceMeshControlPlane` resource to disable IOR: 

```yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
spec:
  gateways:
    openshiftRoute:
      enabled: false
```


You can continue to use the old routes that were previously created using IOR or you can create routes that explicitly target the ingress gateway `Service` object. The following example specifies how to create routes that explicitly target the ingress gateway `Service` object: 

```yaml
kind: Route
apiVersion: route.openshift.io/v1
metadata:
  name: example-gateway
  namespace: istio-system 
```


1

```yaml
spec:
  host: www.example.com
  to:
    kind: Service
    name: istio-ingressgateway 
```


2

```yaml
    weight: 100
  port:
    targetPort: http2
  wildcardPolicy: None
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO23-1)
    

Specify new routes in the same namespace as the ingress gateway `Service` object. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO23-2)
    

Use the name of ingress gateway `Service` object that is the target. 




## 2.16.2. Additional resources

  * [Creating an HTTP-based Route](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-creating-a-route_route-configuration)
  * [Understanding automatic routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-auto-route_traffic-management "2.14.2. Understanding automatic routes")
