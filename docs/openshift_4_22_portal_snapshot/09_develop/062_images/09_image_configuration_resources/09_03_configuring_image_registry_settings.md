# 9.3. Configuring image registry settings

You can configure image registry settings by editing the `image.config.openshift.io/cluster` custom resource (CR). 

**Procedure**

  * Edit the `image.config.openshift.io/cluster` CR by running the following command: 

```shell-session
$ oc edit image.config.openshift.io/cluster
```


The following is an example `image.config.openshift.io/cluster` CR: 

```yaml
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2019-05-17T13:44:26Z"
  generation: 1
  name: cluster
  resourceVersion: "8302"
  selfLink: /apis/config.openshift.io/v1/images/cluster
  uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
spec:
  allowedRegistriesForImport:
    - domainName: quay.io
      insecure: false
  additionalTrustedCA:
    name: myconfigmap
  registrySources:
    allowedRegistries:
    - example.com
    - quay.io
    - registry.redhat.io
    - image-registry.openshift-image-registry.svc:5000
    - reg1.io/myrepo/myapp:latest
    insecureRegistries:
    - insecure.com
status:
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
```


Note

When you use the `allowedRegistries`, `blockedRegistries`, or `insecureRegistries` parameter, you can specify an individual repository within a registry. For example: `reg1.io/myrepo/myapp:latest`. 

Avoid insecure external registries to reduce possible security risks. 




**Verification**

  * To verify your changes, list your nodes by running the following command: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                                         STATUS                     ROLES                  AGE   VERSION
ip-10-0-137-182.us-east-2.compute.internal   Ready,SchedulingDisabled   worker                 65m   v1.35.4
ip-10-0-139-120.us-east-2.compute.internal   Ready,SchedulingDisabled   control-plane          74m   v1.35.4
ip-10-0-176-102.us-east-2.compute.internal   Ready                      control-plane          75m   v1.35.4
ip-10-0-188-96.us-east-2.compute.internal    Ready                      worker                 65m   v1.35.4
ip-10-0-200-59.us-east-2.compute.internal    Ready                      worker                 63m   v1.35.4
ip-10-0-223-123.us-east-2.compute.internal   Ready                      control-plane          73m   v1.35.4
```


## 9.3.1. Adding specific registries to an allowlist

You can add an allowlist of registries, or an individual repository, within a registry for image pull and push actions by editing the `image.config.openshift.io/cluster` custom resource (CR). 

OpenShift Container Platform applies the changes to this CR to all nodes in the cluster. 

When pulling or pushing images, the container runtime searches the registries listed under the `registrySources` parameter in the `image.config.openshift.io/cluster` CR. If you created a list of registries under the `allowedRegistries` parameter, the container runtime searches only those registries. Registries not in your allowlist are blocked. 

Warning

When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure. 

**Procedure**

  * Edit the `image.config.openshift.io/cluster` custom resource by running the following command: 

```shell-session
$ oc edit image.config.openshift.io/cluster
```


The following is an example `image.config.openshift.io/cluster` CR with an allowed list: 

```yaml
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2019-05-17T13:44:26Z"
  generation: 1
  name: cluster
  resourceVersion: "8302"
  selfLink: /apis/config.openshift.io/v1/images/cluster
  uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
spec:
  registrySources:
    allowedRegistries:
    - example.com
    - quay.io
    - registry.redhat.io
    - reg1.io/myrepo/myapp:latest
    - image-registry.openshift-image-registry.svc:5000
status:
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
```


    1. After you make your configuration updates, list your nodes by running the following command: 

```shell-session
$ oc get nodes
```


Example output 

```shell-session
NAME               STATUS   ROLES                  AGE   VERSION
<node_name>        Ready    control-plane,master   37m   v1.27.8+4fab27b
```


    2. Enter debug mode on the node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


Replace <node_name> with the name of your node. 

    3. When prompted, enter `chroot /host` into the terminal: 

```shell-session
sh-4.4# chroot /host
```


**Verification**

  1. Check that the registries are in the policy file by running the following command: 

```shell-session
sh-5.1# cat /etc/containers/policy.json | jq '.'
```


The following policy indicates that only images from the `example.com`, `quay.io`, and `registry.redhat.io` registries are accessible for image pulls and pushes: 

**Example image signature policy file**

```plaintext
{
   "default":[
      {
         "type":"reject"
      }
   ],
   "transports":{
      "atomic":{
         "example.com":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "image-registry.openshift-image-registry.svc:5000":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "insecure.com":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "quay.io":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "reg4.io/myrepo/myapp:latest":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "registry.redhat.io":[
            {
               "type":"insecureAcceptAnything"
            }
         ]
      },
      "docker":{
         "example.com":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "image-registry.openshift-image-registry.svc:5000":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "insecure.com":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "quay.io":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "reg4.io/myrepo/myapp:latest":[
            {
               "type":"insecureAcceptAnything"
            }
         ],
         "registry.redhat.io":[
            {
               "type":"insecureAcceptAnything"
            }
         ]
      },
      "docker-daemon":{
         "":[
            {
               "type":"insecureAcceptAnything"
            }
         ]
      }
   }
}
```


Note

If your cluster uses the `registrySources.insecureRegistries` parameter, ensure that any insecure registries are included in the allowed list. 

For example: 

```yaml
spec:
  registrySources:
    insecureRegistries:
    - insecure.com
    allowedRegistries:
    - example.com
    - quay.io
    - registry.redhat.io
    - insecure.com
    - image-registry.openshift-image-registry.svc:5000
```


## 9.3.2. Blocking specific registries

You can block any registry, or an individual repository, within a registry by editing the `image.config.openshift.io/cluster` custom resource (CR). 

OpenShift Container Platform applies the changes to this CR to all nodes in the cluster. 

When pulling or pushing images, the container runtime searches the registries listed under the `registrySources` parameter in the `image.config.openshift.io/cluster` CR. If you created a list of registries under the `blockedRegistries` parameter, the container runtime does not search those registries. All other registries are allowed. 

Warning

To prevent pod failure, do not add the `registry.redhat.io` and `quay.io` registries to the `blockedRegistries` list. Payload images within your environment require access to these registries. 

**Procedure**

  * Edit the `image.config.openshift.io/cluster` custom resource by running the following command: 

```shell-session
$ oc edit image.config.openshift.io/cluster
```


The following is an example `image.config.openshift.io/cluster` CR with a blocked list: 

```yaml
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2019-05-17T13:44:26Z"
  generation: 1
  name: cluster
  resourceVersion: "8302"
  selfLink: /apis/config.openshift.io/v1/images/cluster
  uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
spec:
  registrySources:
    blockedRegistries:
    - untrusted.com
    - reg1.io/myrepo/myapp:latest
status:
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
```


You cannot set both the `blockedRegistries` and `allowedRegistries` parameters. You must select one or the other. 

    1. Get a list of your nodes by running the following command: 

```shell-session
$ oc get nodes
```


Example output 

```shell-session
NAME                STATUS   ROLES                  AGE   VERSION
<node_name>         Ready    control-plane,master   37m   v1.27.8+4fab27b
```


    2. Run the following command to enter debug mode on the node: 

```shell-session
$ oc debug node/<node_name>
```


Replace <node_name> with the name of the node you want details about. 

    3. When prompted, enter `chroot /host` into the terminal: 

```shell-session
sh-4.4# chroot /host
```


**Verification**

  1. Verify that the registries are in the policy file by running the following command: 

```shell-session
sh-5.1# cat etc/containers/registries.conf
```


The following example indicates that images from the `untrusted.com` registry are blocked for image pulls and pushes: 

**Example output**

```plaintext
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

[[registry]]
  prefix = ""
  location = "untrusted.com"
  blocked = true
```


## 9.3.3. Blocking a payload registry

In a mirroring configuration, you can block upstream payload registries in a disconnected environment by using a `ImageContentSourcePolicy` (ICSP) object. The following example procedure demonstrates how to block the `quay.io/openshift-payload` payload registry. 

**Procedure**

  1. Create the mirror configuration using an `ImageContentSourcePolicy` (ICSP) object to mirror the payload to a registry in your instance. The following example ICSP file mirrors the payload `internal-mirror.io/openshift-payload`: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  name: my-icsp
spec:
  repositoryDigestMirrors:
  - mirrors:
    - internal-mirror.io/openshift-payload
    source: quay.io/openshift-payload
```


  2. After the object deploys onto your nodes, verify that the mirror configuration is set by checking the `/etc/containers/registries.conf` custom resource (CR): 

**Example output**

```shell-session
[[registry]]
  prefix = ""
  location = "quay.io/openshift-payload"
  mirror-by-digest-only = true

[[registry.mirror]]
  location = "internal-mirror.io/openshift-payload"
```


  3. Use the following command to edit the `image.config.openshift.io` CR: 

```shell-session
$ oc edit image.config.openshift.io cluster
```


  4. To block the payload registry, add the following configuration to the `image.config.openshift.io` CR: 

```yaml
spec:
  registrySources:
    blockedRegistries:
     - quay.io/openshift-payload
```


**Verification**

  * Verify that the upstream payload registry is blocked by checking the `/etc/containers/registries.conf` file on the node. 

**Example`/etc/containers/registries.conf` file**

```shell-session
[[registry]]
  prefix = ""
  location = "quay.io/openshift-payload"
  blocked = true
  mirror-by-digest-only = true

[[registry.mirror]]
  location = "internal-mirror.io/openshift-payload"
```


## 9.3.4. Allowing insecure registries

You can add insecure registries, or an individual repository, within a registry by editing the `image.config.openshift.io/cluster` custom resource (CR). 

OpenShift Container Platform applies the changes to this CR to all nodes in the cluster. Registries that do not use valid SSL certificates or do not require HTTPS connections are considered insecure. 

Important

Avoid insecure external registries to reduce possible security risks. 

Warning

When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure. 

**Procedure**

  * Edit the `image.config.openshift.io/cluster` custom resource (CR) by running the following command: 

```shell-session
$ oc edit image.config.openshift.io/cluster
```


The following is an example `image.config.openshift.io/cluster` CR with an insecure registries list: 

```yaml
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2019-05-17T13:44:26Z"
  generation: 1
  name: cluster
  resourceVersion: "8302"
  selfLink: /apis/config.openshift.io/v1/images/cluster
  uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
spec:
  registrySources:
    insecureRegistries:
    - insecure.com
    - reg4.io/myrepo/myapp:latest
    allowedRegistries:
    - example.com
    - quay.io
    - registry.redhat.io
    - insecure.com
    - reg4.io/myrepo/myapp:latest
    - image-registry.openshift-image-registry.svc:5000
status:
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
```


**Verification**

  * Check that the registries are added to the policy file by running the following command on a node: 

```shell-session
$ cat /etc/containers/registries.conf
```


The following example indicates that images from the `insecure.com` registry is insecure and are allowed for image pulls and pushes. 

**Example output**

```shell-session
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

[[registry]]
  prefix = ""
  location = "insecure.com"
  insecure = true
```
