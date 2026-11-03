# 5.1. Expose a default registry manually

You can gain external access to the default OpenShift image registry by exposing it with a route. External access lets you log in from outside the cluster and tag and push images to an existing project by using the route host. 

**Prerequisites**

  * The following prerequisites are automatically performed: 

    * Deploy the Registry Operator. 
    * Deploy the Ingress Operator. 

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. To expose the registry by using the `defaultRoute` parameter that exists in the `configs.imageregistry.operator.openshift.io` resource, set `defaultRoute` to `true` by running the following command: 

```shell-session
$ oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
```


  2. Get the default registry route by running the following command: 

```shell-session
$ HOST=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')
```


  3. Get the certificate of the Ingress Operator by running the following command: 

```shell-session
$ oc extract secret/$(oc get ingresscontroller -n openshift-ingress-operator default -o json | jq '.spec.defaultCertificate.name // "router-certs-default"' -r) -n openshift-ingress --confirm
```


  4. Move the extracted certificate to the trusted CA directory of the system by running the following command: 

```shell-session
$ sudo mv tls.crt /etc/pki/ca-trust/source/anchors/
```


  5. Enable the default certificate of the cluster to trust the route by running the following command: 

```shell-session
$ sudo update-ca-trust enable
```


  6. Log in with podman with the default route by running the following command: 

```shell-session
$ sudo podman login -u kubeadmin -p $(oc whoami -t) $HOST
```
