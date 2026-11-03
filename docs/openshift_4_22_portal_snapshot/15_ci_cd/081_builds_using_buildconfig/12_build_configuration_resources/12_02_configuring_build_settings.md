# 12.2. Configuring build settings

You can configure build settings by editing the `build.config.openshift.io/cluster` resource. 

**Procedure**

  * Edit the `build.config.openshift.io/cluster` resource by entering the following command: 

```shell-session
$ oc edit build.config.openshift.io/cluster
```


The following is an example `build.config.openshift.io/cluster` resource: 

```yaml
apiVersion: config.openshift.io/v1
kind: Build 
```


1

```yaml
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2019-05-17T13:44:26Z"
  generation: 2
  name: cluster
  resourceVersion: "107233"
  selfLink: /apis/config.openshift.io/v1/builds/cluster
  uid: e2e9cc14-78a9-11e9-b92b-06d6c7da38dc
spec:
  buildDefaults: 
```


2

```yaml
    defaultProxy: 
```


3

```yaml
      httpProxy: http://proxy.com
      httpsProxy: https://proxy.com
      noProxy: internal.com
    env: 
```


4

```yaml
    - name: envkey
      value: envvalue
    gitProxy: 
```


5

```yaml
      httpProxy: http://gitproxy.com
      httpsProxy: https://gitproxy.com
      noProxy: internalgit.com
    imageLabels: 
```


6

```yaml
    - name: labelkey
      value: labelvalue
    resources: 
```


7

```yaml
      limits:
        cpu: 100m
        memory: 50Mi
      requests:
        cpu: 10m
        memory: 10Mi
  buildOverrides: 
```


8

```yaml
    imageLabels: 
```


9

```yaml
    - name: labelkey
      value: labelvalue
    nodeSelector: 
```


10

```yaml
      selectorkey: selectorvalue
    tolerations: 
```


11

```yaml
    - effect: NoSchedule
      key: node-role.kubernetes.io/builds
operator: Exists
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-1)
    

`Build`: Holds cluster-wide information on how to handle builds. The canonical, and only valid name is `cluster`. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-2)
    

`buildDefaults`: Controls the default information for builds. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-3)
    

`defaultProxy`: Contains the default proxy settings for all build operations, including image pull or push and source download. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-4)
    

`env`: A set of default environment variables that are applied to the build if the specified variables do not exist on the build. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-5)
    

`gitProxy`: Contains the proxy settings for Git operations only. If set, this overrides any Proxy settings for all Git commands, such as `git clone`. 

[6](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-6)
    

`imageLabels`: A list of labels that are applied to the resulting image. You can override a default label by providing a label with the same name in the `BuildConfig`. 

[7](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-7)
    

`resources`: Defines resource requirements to execute the build. 

[8](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-8)
    

`buildOverrides`: Controls override settings for builds. 

[9](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-9)
    

`imageLabels`: A list of labels that are applied to the resulting image. If you provided a label in the `BuildConfig` with the same name as one in this table, your label will be overwritten. 

[10](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-10)
    

`nodeSelector`: A selector which must be true for the build pod to fit on a node. 

[11](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-configuration#CO30-11)
    

`tolerations`: A list of tolerations that overrides any existing tolerations set on a build pod.
