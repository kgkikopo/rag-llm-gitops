# 2.15. Gateway migration

As a network administrator, the preferred method for deploying ingress and egress gateways is with a `Deployment` resource using gateway injection. 

## 2.15.1. About gateway migration

In Red Hat OpenShift Service Mesh 2.x, the Service Mesh Operator creates an ingress and egress gateway in the control plane namespace by default. You can define additional gateways in the `ServiceMeshControlPlane` resource. 

Deploying ingress and egress gateways with a `Deployment` resource using gateway injection provides greater flexibility and control. This deployment approach is a better practice because it allows you to manage gateways alongside the corresponding applications rather than in the control plane resource. Therefore, you should disable the default gateways, move away from the Service Mesh Control Plane declaration, and begin to use gateway injection. 

## 2.15.2. Migrate from SMCP-Defined gateways to gateway injection

This procedure explains how to migrate with zero downtime from gateways defined in the `ServiceMeshControlPlane` resource to gateways that are managed using gateway injection. This migration is achieved by using the existing gateway `Service` object to target a new gateway deployment that is created using gateway injection. 

**Prerequisites**

  * You are logged in to the OpenShift Container Platform web console as `cluster-admin`. 
  * The Red Hat OpenShift Service Mesh Operator must be installed. 
  * The `ServiceMeshControlPlane` resource must be deployed and an ingress gateway exists in the configuration. 



**Procedure**

  1. Create a new ingress gateway that is configured to use gateway injection. 

Note

This procedure migrates away from the default ingress gateway deployment defined in the `ServiceMeshControlPlane` resource to gateway injection. The procedure may be modified to migrate from additional ingress gateways configured in the SMCP. 

**Example ingress gateway resource with gateway injection**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: istio-ingressgateway-canary
  namespace: istio-system 
```


1

```yaml
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
      istio: ingressgateway
  template:
    metadata:
      annotations:
        inject.istio.io/templates: gateway
      labels: 
```


2

```yaml
        app: istio-ingressgateway
        istio: ingressgateway
        sidecar.istio.io/inject: "true"
    spec:
      containers:
        - name: istio-proxy
          image: auto
      serviceAccountName: istio-ingressgateway
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: istio-ingressgateway
  namespace: istio-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secret-reader
  namespace: istio-system
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: istio-ingressgateway-secret-reader
  namespace: istio-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: secret-reader
subjects:
  - kind: ServiceAccount
    name: istio-ingressgateway
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy 
```


3

```yaml
metadata:
  name: gatewayingress
  namespace: istio-system
spec:
  podSelector:
    matchLabels:
      istio: ingressgateway
  ingress:
    - {}
  policyTypes:
    - Ingress
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO22-1)
    

The gateway injection deployment and all supporting resources should be deployed in the same namespace as the SMCP-defined gateway. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO22-2)
    

Ensure that the labels specified in the pod template include all of the label selectors specified in the `Service` object associated with the existing SMCP-defined gateway. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#CO22-3)
    

Grant access to the new gateway from outside the cluster. This access is required whenever the `spec.security.manageNetworkPolicy` of the `ServiceMeshControlPlane` resource is set to `true`, which is the default setting. 

  2. Verify that the new gateway deployment is successfully handling requests. 

If access logging was configured in the `ServiceMeshControlPlane` resource, view the access logs of the new gateway deployment to confirm the behavior. 

  3. Scale down the old deployment and scale up the new deployment. 

Gradually shift traffic from the old gateway deployment to the new gateway deployment by performing the following steps: 

     1. Increase the number of replicas for the new gateway deployment by running the following command: 

```shell-session
$ oc scale -n istio-system deployment/<new_gateway_deployment> --replicas <new_number_of_replicas>
```


     2. Decrease the number of replicas for the old gateway deployment by running the following command: 

```shell-session
$ oc scale -n istio-system deployment/<old_gateway_deployment> --replicas <new_number_of_replicas>
```


     3. Repeat running the previous two commands. Each time, increase the number of replicas for the new gateway deployment and decrease the number of replicas for the old gateway deployment. Continue repeating until the new gateway deployment handles all traffic to the gateway `Service` object. 

  4. Remove the `app.kubernetes.io/managed-by` label from the gateway `Service` object by running the following command: 

```shell-session
$ oc label service -n istio-system istio-ingressgateway app.kubernetes.io/managed-by-
```


Removing the label prevents the service from being deleted when the gateway is disabled in the `ServiceMeshControlPlane` resource. 

  5. Remove the `ownerReferences` object from the gateway `Service` object by running the following command: 

```shell-session
$ oc patch service -n istio-system istio-ingressgateway --type='json' -p='[{"op": "remove", "path": "/metadata/ownerReferences"}]'
```


Removing this object prevents the service from being garbage collected when the `ServiceMeshControlPlane` resource is deleted. 

  6. Disable the old gateway deployment that was managed by the `ServiceMeshControlPlane` resource by running the following command: 

```shell-session
$ oc patch smcp -n istio-system <smcp_name> --type='json' -p='[{"op": "replace", "path": "/spec/gateways/ingress/enabled", "value": false}]'
```


Note

     * When the old ingress gateway `Service` object is disabled it is not deleted. You may save this `Service` object to a file and manage it alongside the new gateway injection resources. 
     * The `/spec/gateways/ingress/enabled` path is available if you explicitly set it for the `ServiceMeshControlPlane` resource. If you are using the default value, you must patch the `/spec/gateways/enabled` path for both ingress and egress gateways. 




## 2.15.3. Additional resources

  * [Enabling gateway injection](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-automatic-gateway-injection_traffic-management "2.14.1.1. Enabling gateway injection")
  * [Deploying automatic gateway injection](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/service-mesh-2-x#ossm-deploying-automatic-gateway-injection_traffic-management "2.14.1.2. Deploying automatic gateway injection")
