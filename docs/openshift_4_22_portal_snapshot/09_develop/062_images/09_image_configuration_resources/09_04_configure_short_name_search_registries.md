# 9.4. Configure short-name search registries

With an image short name, you can search for images without including the fully qualified domain name in the pull `spec` parameter. 

For example, you could use `rhel7/etcd` instead of `registry.access.redhat.com/rhe7/etcd`. You can add registries to search for an image short name by editing the `image.config.openshift.io/cluster` custom resource (CR). 

You might use short names in situations where using the full path is not practical. For example, if your cluster references multiple internal registries whose DNS changes often, you would need to update the fully qualified domain names in your pull specs with each change. In this case, using an image short name might be beneficial. 

When pulling or pushing images, the container runtime searches the registries listed under the `registrySources` parameter in the `image.config.openshift.io/cluster` CR. If you created a list of registries under the `containerRuntimeSearchRegistries` parameter, when pulling an image with a short name, the container runtime searches those registries. 

## 9.4.1. When not to use image short names

To avoid deployment failures and security risks in OpenShift Container Platform, use fully-qualified image names instead of short names. Short names work with Red Hat internal registries, but public registries that require authentication might fail to deploy them. 

You cannot list multiple public registries under the `containerRuntimeSearchRegistries` parameter if each public registry requires different credentials and a cluster does not list the public registry in the global pull secret. 

For a public registry that requires authentication, you can use an image short name only if the registry has its credentials stored in the global pull secret. 

Warning

If you list public registries under the `containerRuntimeSearchRegistries` parameter (including the `registry.redhat.io`, `docker.io`, and `quay.io` registries), you expose your credentials to all the registries on the list, and you risk network and registry attacks. Because you can only have one pull secret for pulling images, as defined by the global pull secret, that secret is used to authenticate against every registry in that list. Therefore, if you include public registries in the list, you introduce a security risk. 

## 9.4.2. Adding registries that allow image short names

You can add registries to search for an image short name by editing the `image.config.openshift.io/cluster` custom resource (CR). OpenShift Container Platform applies the changes to this CR to all nodes in the cluster. 

Warning

When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure. 

**Procedure**

  * Edit the `image.config.openshift.io/cluster` custom resource: 

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
    containerRuntimeSearchRegistries:
    - reg1.io
    - reg2.io
    - reg3.io
    allowedRegistries:
    - example.com
    - quay.io
    - registry.redhat.io
    - reg1.io
    - reg2.io
    - reg3.io
    - image-registry.openshift-image-registry.svc:5000
...
status:
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
```


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


    3. When prompted, enter `chroot /host` into the terminal: 

```shell-session
sh-4.4# chroot /host
```


**Verification**

  1. Verify that registries are added to the policy file by running the following command: 

```shell-session
sh-5.1# cat /etc/containers/registries.conf.d/01-image-searchRegistries.conf
```


**Example output**

```plaintext
unqualified-search-registries = ['reg1.io', 'reg2.io', 'reg3.io']
```


## 9.4.3. Configure additional trust stores for image registry access

You can add references to a config map that has additional certificate authorities (CAs) to be trusted during image registry access to the `image.config.openshift.io/cluster` custom resource (CR). 

**Prerequisites**

  * The certificate authorities (CAs) must be PEM-encoded. 



**Procedure**

  1. Create a config map in the `openshift-config` namespace, then and use the config map name in the `AdditionalTrustedCA` parameter of the `image.config.openshift.io` CR. This adds CAs that should be trusted when the cluster contacts external image registries. 

**Image registry CA config map example**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-registry-ca
data:
  registry.example.com: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
  registry-with-port.example.com..5000: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
```


where: 

`data:registry.example.com:`
     An example hostname of a registry for which this CA is to be trusted. 
`data:registry-with-port.example.com..5000:`
    

An example hostname of a registry with the port for which this CA is to be trusted. If the registry has a port, such as `registry-with-port.example.com:5000`, `:` must be replaced with `..`. 

The PEM certificate content is the value for each additional registry CA to trust. 

  2. Optional. Configure an additional CA by running the following command: 

```shell-session
$ oc create configmap registry-config --from-file=<external_registry_address>=ca.crt -n openshift-config
```


```shell-session
$ oc edit image.config.openshift.io cluster
```


```yaml
spec:
  additionalTrustedCA:
    name: registry-config
```
