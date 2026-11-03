# 1.1. Configure system controls by using the tuning CNI

To configure interface-level network sysctls in OpenShift Container Platform, you can use the tuning CNI meta plugin in a network attachment definition. Configure the `net.ipv4.conf.IFNAME.accept_redirects` sysctl to enable accepting and sending ICMP-redirected packets. 

**Procedure**

  1. Create a network attachment definition, such as `tuning-example.yaml`, with the following content: 

```yaml
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: <name>
  namespace: default
spec:
  config: '{
    "cniVersion": "0.4.0",
    "name": "<name>",
    "plugins": [{
       "type": "<main_CNI_plugin>"
      },
      {
       "type": "tuning",
       "sysctl": {
            "net.ipv4.conf.IFNAME.accept_redirects": "1"
        }
      }
     ]
}
```


where: 

`metadata.name`
     Specifies the name for the additional network attachment to create. The name must be unique within the specified namespace. 
`metadata.namespace`
     Specifies the namespace that the object is associated with. 
`spec.config.cniVersion`
     Specifies the CNI specification version. 
`spec.config.name`
     Specifies the name for the configuration. It is recommended to match the configuration name to the name value of the network attachment definition. 
`spec.config.plugins.type`
     Specifies the name of the main CNI plugin to configure. 
`spec.config.plugins.tuning.sysctl`
     Specifies the sysctl to set. The interface name is represented by the `IFNAME` token and is replaced with the actual name of the interface at runtime. 

**Example network attachment definition**

```yaml
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: tuningnad
  namespace: default
spec:
  config: '{
    "cniVersion": "0.4.0",
    "name": "tuningnad",
    "plugins": [{
      "type": "bridge"
      },
      {
      "type": "tuning",
      "sysctl": {
         "net.ipv4.conf.IFNAME.accept_redirects": "1"
        }
    }
  ]
}'
```


  2. Apply the YAML by running the following command: 

```shell-session
$ oc apply -f tuning-example.yaml
```


**Example output**

```shell-session
networkattachmentdefinition.k8.cni.cncf.io/tuningnad created
```


  3. Create a pod such as `examplepod.yaml` with the network attachment definition similar to the following: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tunepod
  namespace: default
  annotations:
    k8s.v1.cni.cncf.io/networks: tuningnad
spec:
  containers:
  - name: podexample
    image: centos
    command: ["/bin/bash", "-c", "sleep INF"]
    securityContext:
      runAsUser: 2000
      runAsGroup: 3000
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
```


where: 

`metadata.annotations.k8s.v1.cni.cncf.io/networks`
     Specifies the name of the configured `NetworkAttachmentDefinition`. 
`spec.containers.securityContext.runAsUser`
     Specifies which user ID the container is run with. 
`spec.containers.securityContext.runAsGroup`
     Specifies which primary group ID the containers is run with. 
`spec.containers.securityContext.allowPrivilegeEscalation`
     Specifies if a pod can request to allow privilege escalation. If unspecified, it defaults to true. This boolean directly controls whether the `no_new_privs` flag gets set on the container process. 
`spec.containers.securityContext.capabilities`
     Specifies privileged actions without giving full root access. This policy ensures all capabilities are dropped from the pod. 
`spec.securityContext.runAsNonRoot: true`
     Specifies that the container will run with a user with any UID other than 0. 
`spec.securityContext.seccompProfile`
     Specifies the default seccomp profile for a pod or container workload. 

  4. Apply the yaml by running the following command: 

```shell-session
$ oc apply -f examplepod.yaml
```


  5. Verify that the pod is created by running the following command: 

```shell-session
$ oc get pod
```


**Example output**

```shell-session
NAME      READY   STATUS    RESTARTS   AGE
tunepod   1/1     Running   0          47s
```


  6. Log in to the pod by running the following command: 

```shell-session
$ oc rsh tunepod
```


  7. Verify the values of the configured sysctl flags. For example, find the value `net.ipv4.conf.net1.accept_redirects` by running the following command: 

```shell-session
sh-4.4# sysctl net.ipv4.conf.net1.accept_redirects
```


**Expected output**

```shell-session
net.ipv4.conf.net1.accept_redirects = 1
```
