# 7.5. Create pods that have IPv6 connectivity on RHOSP

After you enable and add IPv6 connectivity to pods, you can create pods that have secondary IPv6 connections. 

**Procedure**

  1. Define pods that use your IPv6 namespace and the annotation `k8s.v1.cni.cncf.io/networks: <additional_network_name>`, where `<additional_network_name>` is the name of the additional network. For example, as part of a `Deployment` object: 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-openshift
  namespace: ipv6
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
         - labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - hello-openshift
  replicas: 2
  selector:
    matchLabels:
      app: hello-openshift
  template:
    metadata:
      labels:
        app: hello-openshift
      annotations:
        k8s.v1.cni.cncf.io/networks: ipv6
    spec:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: hello-openshift
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
        image: quay.io/openshift/origin-hello-openshift
        ports:
        - containerPort: 8080
```


  2. Create the pod. For example, on a command line, enter the following command: 

```shell-session
$ oc create -f <ipv6_enabled_resource>
```


Replace `<ipv6_enabled_resource>` with the file that contains your resource definition.
