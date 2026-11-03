# 2.3. Set the Ingress Controller to private

You can configure the default Ingress Controller to use an internal endpoint so that application routes are published only in the private DNS zone. 

After you deploy a cluster, you can modify its Ingress Controller to use only a private zone. 

**Procedure**

  1. Modify the default Ingress Controller to use only an internal endpoint: 

```shell-session
$ oc replace --force --wait --filename - <<EOF
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: default
spec:
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
EOF
```


**Example output**

```shell-session
ingresscontroller.operator.openshift.io "default" deleted
ingresscontroller.operator.openshift.io/default replaced
```


The public DNS entry is removed, and the private zone entry is updated.
