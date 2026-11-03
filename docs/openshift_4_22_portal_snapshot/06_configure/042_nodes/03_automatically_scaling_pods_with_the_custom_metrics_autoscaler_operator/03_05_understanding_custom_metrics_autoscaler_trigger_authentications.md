# 3.5. Understanding custom metrics autoscaler trigger authentications

A trigger authentication allows you to include authentication information in a scaled object or a scaled job that can be used by the associated containers. You can use trigger authentications to pass OpenShift Container Platform secrets, platform-native pod authentication mechanisms, environment variables, and so on. 

You define a `TriggerAuthentication` object in the same namespace as the object that you want to scale. That trigger authentication can be used only by objects in that namespace. 

Alternatively, to share credentials between objects in multiple namespaces, you can create a `ClusterTriggerAuthentication` object that can be used across all namespaces. 

Trigger authentications and cluster trigger authentication use the same configuration. However, a cluster trigger authentication requires an additional `kind` parameter in the authentication reference of the scaled object. 

**Example trigger authentication that uses a bound service account token**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace 
```


1

```yaml
spec:
  boundServiceAccountToken: 
```


2

```yaml
    - parameter: bearerToken
      serviceAccountName: thanos 
```


3

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-1) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-2) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-3) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-5) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-7) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-8) [1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-9)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-4) [2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-6) [2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-10)
    

Specifies that this trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO1-11)
    

Specifies the name of the service account to use. 

**Example cluster trigger authentication that uses a bound service account token**

```yaml
kind: ClusterTriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: bound-service-account-token-triggerauthentication 
```


1

```yaml
spec:
  boundServiceAccountToken: 
```


2

```yaml
    - parameter: bearerToken
      serviceAccountName: thanos 
```


3

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO2-1)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO2-2)
    

Specifies that this cluster trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO2-3)
    

Specifies the name of the service account to use. 

**Example trigger authentication that uses a secret for Basic authentication**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace 
```


1

```yaml
spec:
  secretTargetRef: 
```


2

```yaml
  - parameter: username 
```


3

```yaml
    name: my-basic-secret 
```


4

```yaml
    key: username 
```


5

```yaml
  - parameter: password
    name: my-basic-secret
    key: password
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO3-1)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO3-2)
    

Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO3-3)
    

Specifies the authentication parameter to supply by using the secret. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO3-4)
    

Specifies the name of the secret to use. See the following example secret for Basic authentication. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO3-5)
    

Specifies the key in the secret to use with the specified parameter. 

**Example secret for Basic authentication**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-basic-secret
  namespace: default
data:
  username: "dXNlcm5hbWU=" 
```


1

```yaml
  password: "cGFzc3dvcmQ="
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO4-1)
    

User name and password to supply to the trigger authentication. The values in the `data` stanza must be base-64 encoded. 

**Example trigger authentication that uses a secret for CA details**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace 
```


1

```yaml
spec:
  secretTargetRef: 
```


2

```yaml
    - parameter: key 
```


3

```yaml
      name: my-secret 
```


4

```yaml
      key: client-key.pem 
```


5

```yaml
    - parameter: ca 
```


6

```yaml
      name: my-secret 
```


7

```yaml
      key: ca-cert.pem 
```


8

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-1)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-2)
    

Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-3)
    

Specifies the type of authentication to use. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-4)
    

Specifies the name of the secret to use. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-5)
    

Specifies the key in the secret to use with the specified parameter. 

[6](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-6)
    

Specifies the authentication parameter for a custom CA when connecting to the metrics endpoint. 

[7](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-7)
    

Specifies the name of the secret to use. See the following example secret with certificate authority (CA) details. 

[8](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO5-8)
    

Specifies the key in the secret to use with the specified parameter. 

**Example secret with certificate authority (CA) details**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-namespace
data:
  ca-cert.pem: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0... 
```


1

```yaml
  client-cert.pem: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0... 
```


2

```yaml
  client-key.pem: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0t...
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO6-1)
    

Specifies the TLS CA Certificate for authentication of the metrics endpoint. The value must be base-64 encoded. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO6-2)
    

Specifies the TLS certificates and key for TLS client authentication. The values must be base-64 encoded. 

**Example trigger authentication that uses a bearer token**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: token-triggerauthentication
  namespace: my-namespace 
```


1

```yaml
spec:
  secretTargetRef: 
```


2

```yaml
  - parameter: bearerToken 
```


3

```yaml
    name: my-secret 
```


4

```yaml
    key: bearerToken 
```


5

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO7-1)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO7-2)
    

Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO7-3)
    

Specifies the type of authentication to use. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO7-4)
    

Specifies the name of the secret to use. See the following example secret for a bearer token. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO7-5)
    

Specifies the key in the token to use with the specified parameter. 

**Example secret for a bearer token**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-namespace
data:
  bearerToken: "<bearer_token>" 
```


1

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO8-1)
    

Specifies a bearer token to use with bearer authentication. The value must be base-64 encoded. 

**Example trigger authentication that uses an environment variable**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: env-var-triggerauthentication
  namespace: my-namespace 
```


1

```yaml
spec:
  env: 
```


2

```yaml
  - parameter: access_key 
```


3

```yaml
    name: ACCESS_KEY 
```


4

```yaml
    containerName: my-container 
```


5

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO9-1)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO9-2)
    

Specifies that this trigger authentication uses environment variables for authorization when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO9-3)
    

Specify the parameter to set with this variable. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO9-4)
    

Specify the name of the environment variable. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO9-5)
    

Optional: Specify a container that requires authentication. The container must be in the same resource as referenced by `scaleTargetRef` in the scaled object. 

**Example trigger authentication that uses pod authentication providers**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: pod-id-triggerauthentication
  namespace: my-namespace 
```


1

```yaml
spec:
  podIdentity: 
```


2

```yaml
    provider: aws-eks 
```


3

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO10-1)
    

Specifies the namespace of the object you want to scale. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO10-2)
    

Specifies that this trigger authentication uses a platform-native pod authentication when connecting to the metrics endpoint. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#CO10-3)
    

Specifies a pod identity. Supported values are `none`, `azure`, `gcp`, `aws-eks`, or `aws-kiam`. The default is `none`. 

**Additional resources**

  * [Understanding and creating service accounts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-service-accounts)
  * [Providing sensitive data to pods](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-secrets "2.7. Providing sensitive data to pods by using secrets"). 



## 3.5.1. Use trigger authentications

You use trigger authentications and cluster trigger authentications by using a custom resource to create the authentication, then add a reference to a scaled object or scaled job. 

**Prerequisites**

  * The Custom Metrics Autoscaler Operator must be installed. 
  * If you are using a bound service account token, the service account must exist. 
  * If you are using a bound service account token, a role-based access control (RBAC) object that enables the Custom Metrics Autoscaler Operator to request service account tokens from the service account must exist. 

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: keda-operator-token-creator
  namespace: <namespace_name>
rules:
- apiGroups:
  - ""
  resources:
  - serviceaccounts/token
  verbs:
  - create
  resourceNames:
  - thanos
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: keda-operator-token-creator-binding
  namespace: <namespace_name>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: keda-operator-token-creator
subjects:
- kind: ServiceAccount
  name: keda-operator
  namespace: openshift-keda
```


where: 

`metadata.namespace`
     Specifies the namespace of the service account. 
`rules[].resourceNames[]`
     Specifies the name of the service account. 

  * If you are using a secret, the `Secret` object must exist. 



**Procedure**

  1. Create the `TriggerAuthentication` or `ClusterTriggerAuthentication` object. 

     1. Create a YAML file that defines the object: 

**Example trigger authentication with a bound service account token**

```yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: prom-triggerauthentication
  namespace: my-namespace
  spec:
  boundServiceAccountToken:
    - parameter: token
      serviceAccountName: thanos
```


where: 

`metadata.namespace`
     Specifies the namespace of the object you want to scale. 
`spec.boundServiceAccountToken`
     Specifies that this trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint. 
`spec.boundServiceAccountToken[].serviceAccountName`
     Specifies the name of the service account to use. 

     2. Create the `TriggerAuthentication` object: 

```shell-session
$ oc create -f <filename>.yaml
```


  2. Create or edit a `ScaledObject` YAML file that uses the trigger authentication: 

     1. Create a YAML file that defines the object by running the following command: 

**Example scaled object with a trigger authentication**

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: scaledobject
  namespace: my-namespace
spec:
  scaleTargetRef:
    name: example-deployment
  maxReplicaCount: 100
  minReplicaCount: 0
  pollingInterval: 30
  triggers:
  - type: prometheus
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest # replace <NAMESPACE>
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "basic"
    authenticationRef:
      name: prom-triggerauthentication
      kind: TriggerAuthentication
```


where: 

`spec.triggers[].authenticationRef.name`
     Specifies the name of your trigger authentication object. 
`spec.triggers[].authenticationRef.kind`
    

Specifies `TriggerAuthentication`. `TriggerAuthentication` is the default. 

**Example scaled object with a cluster trigger authentication**

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: scaledobject
  namespace: my-namespace
spec:
  scaleTargetRef:
    name: example-deployment
  maxReplicaCount: 100
  minReplicaCount: 0
  pollingInterval: 30
  triggers:
  - type: prometheus
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest # replace <NAMESPACE>
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "basic"
    authenticationRef:
      name: prom-cluster-triggerauthentication
      kind: ClusterTriggerAuthentication
```


where: 

`spec.triggers[].authenticationRef.name`
     Specifies the name of your trigger authentication object. 
`spec.triggers[].authenticationRef.kind`
     Specifies `ClusterTriggerAuthentication`. 

     2. Create the scaled object by running the following command: 

```shell-session
$ oc apply -f <filename>
```
