# 5.2. Expose a secure registry manually

You can gain external access to the OpenShift image registry by exposing it with a route. External access lets you log in from outside the cluster and tag and push images to an existing project by using the route host. 

You can expose the route by using `DefaultRoute` parameter in the `configs.imageregistry.operator.openshift.io` resource or by using custom routes. 

**Prerequisites**

  * The following prerequisites are automatically performed: 

    * Deploy the Registry Operator. 
    * Deploy the Ingress Operator. 

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. To expose the registry using `DefaultRoute` parameter, set `DefaultRoute` to `True`: 

```shell-session
$ oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
```


  2. Log in with `podman` by entering the following command: 

```shell-session
$ HOST=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')
```


```shell-session
$ podman login -u kubeadmin -p $(oc whoami -t) --tls-verify=false $HOST
```


     * `--tls-verify=false`: Set this parameter to `false` if the default certificate of the cluster for routes is untrusted. You can set a custom, trusted certificate as the default certificate with the Ingress Operator. 

  3. To expose the registry using custom routes, create a secret with your route’s TLS keys. This step is optional. If you do not create a secret, the route uses the default TLS configuration from the Ingress Operator. 

```shell-session
$ oc create secret tls public-route-tls \
    -n openshift-image-registry \
    --cert=</path/to/tls.crt> \
    --key=</path/to/tls.key>
```


  4. On the Registry Operator, enter the following command: 

```shell-session
$ oc edit configs.imageregistry.operator.openshift.io/cluster
```


```yaml
spec:
  routes:
    - name: public-routes
      hostname: myregistry.mycorp.organization
      secretName: public-route-tls
...
```


Note

Only set `secretName` if you are providing a custom TLS configuration for the route of the registry. 




**Troubleshooting**

  * [Error creating TLS secret](https://access.redhat.com/solutions/5419501)
