# 2.5. Configure the cluster for the mirror registry

After creating and mirroring the images to the mirror registry, you must modify your cluster so that pods can pull images from the mirror registry. 

You must: 

  * Add the mirror registry credentials to the global pull secret. 
  * Add the mirror registry server certificate to the cluster. 
  * Create an `ImageContentSourcePolicy` custom resource (ICSP), which associates the mirror registry with the source registry. 



**Procedure**

  1. Add mirror registry credential to the cluster global pull-secret: 

```shell-session
$ oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=<pull_secret_location>
```


For `<pull_secret_location>`, provide the path to the new pull secret file. 

For example: 

```shell-session
$ oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=.mirrorsecretconfigjson
```


  2. Add the CA-signed mirror registry server certificate to the nodes in the cluster: 

     1. Create a config map that includes the server certificate for the mirror registry: 

```shell-session
$ oc create configmap <config_map_name> --from-file=<mirror_address_host>..<port>=$path/ca.crt -n openshift-config
```


For example: 

```shell-session
$ oc create configmap registry-config --from-file=mirror.registry.com..443=/root/certs/ca-chain.cert.pem -n openshift-config
```


     2. Use the config map to update the `image.config.openshift.io/cluster` custom resource (CR). OpenShift Container Platform applies the changes to this CR to all nodes in the cluster: 

```shell-session
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"<config_map_name>"}}}' --type=merge
```


For example: 

```shell-session
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
```


  3. Create an ICSP to redirect container pull requests from the online registries to the mirror registry: 

     1. Create the `ImageContentSourcePolicy` custom resource: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  name: mirror-ocp
spec:
  repositoryDigestMirrors:
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-release
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```


where: 

`spec.mirrors`
     Specifies the name of the mirror image registry and repository. 
`spec.source`
     Specifies the online registry and repository containing the content that is mirrored. 

     2. Create the ICSP object: 

```shell-session
$ oc create -f registryrepomirror.yaml
```


**Example output**

```shell-session
imagecontentsourcepolicy.operator.openshift.io/mirror-ocp created
```


OpenShift Container Platform applies the changes to this CR to all nodes in the cluster. 

  4. Verify that the credentials, CA, and ICSP for mirror registry are added: 

     1. Log in to a node: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell: 

```shell-session
sh-4.4# chroot /host
```


     3. Check the `config.json` file for the credentials: 

```shell-session
sh-4.4# cat /var/lib/kubelet/config.json
```


**Example output**

```shell-session
{"auths":{"brew.registry.redhat.io":{"xx=="},"brewregistry.stage.redhat.io":{"auth":"xxx=="},"mirror.registry.com:443":{"auth":"xx="}}}
```


Ensure that the mirror registry and credentials are present. 

     4. Change to the `certs.d` directory: 

```shell-session
sh-4.4# cd /etc/docker/certs.d/
```


     5. List the certificates in the `certs.d` directory: 

```shell-session
sh-4.4# ls
```


**Example output**

```shell-session
image-registry.openshift-image-registry.svc.cluster.local:5000
image-registry.openshift-image-registry.svc:5000
mirror.registry.com:443
```


For `mirror.registry.com:443`, ensure that the mirror registry is in the list. 

     6. Check that the ICSP added the mirror registry to the `registries.conf` file: 

```shell-session
sh-4.4# cat /etc/containers/registries.conf
```


**Example output**

```shell-session
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

[[registry]]
  prefix = ""
  location = "quay.io/openshift-release-dev/ocp-release"
  mirror-by-digest-only = true

  [[registry.mirror]]
    location = "mirror.registry.com:443/ocp/release"

[[registry]]
  prefix = ""
  location = "quay.io/openshift-release-dev/ocp-v4.0-art-dev"
  mirror-by-digest-only = true

  [[registry.mirror]]
    location = "mirror.registry.com:443/ocp/release"
```


The `registry.mirror` parameters indicate that the mirror registry is searched before the original registry. 

     7. Exit the node. 

```shell-session
sh-4.4# exit
```
