# 4.2. Access the registry directly from the cluster

You can access the registry from inside the cluster by using internal routes. 

**Procedure**

  1. Access the node by getting its name: 

```shell-session
$ oc get nodes
```


```shell-session
$ oc debug nodes/<node_name>
```


  2. To enable access to tools such as `oc` and `podman` on the node, change your root directory to `/host`. Successful output on running the commands states `Login Succeeded!`. 

```shell-session
sh-4.2# chroot /host
```


  3. Log in to the container image registry by using your access token: 

```shell-session
sh-4.2# oc login -u kubeadmin -p <password_from_install_log> https://api-int.<cluster_name>.<base_domain>:6443
```


```shell-session
sh-4.2# podman login -u kubeadmin -p $(oc whoami -t) image-registry.openshift-image-registry.svc:5000
```


Note

You can pass almost any value for the user name. The token contains all necessary information. Passing a user name that contains colons results in a login failure. 

The Image Registry Operator creates the route, such as `default-route-openshift-image-registry.<cluster_name>`. 

  4. Perform `podman pull` and `podman push` operations against your registry. The following example commands demonstrate these operations. 

     1. Pull an arbitrary image: 

```shell-session
sh-4.2# podman pull <name.io>/<image>
```


Important

You can pull arbitrary images, but if you have the **system:registry** role added, you can only push images to the registry in your project. 

     2. Tag the new image with the form `<registry_ip>:<port>/<project>/<image>`. For example, `172.30.124.220:5000/openshift/image`. The project name must show in the pull specification for OpenShift Container Platform to correctly place and later access the image in the registry. 

```shell-session
sh-4.2# podman tag <name.io>/<image> image-registry.openshift-image-registry.svc:5000/openshift/<image>
```


Note

You must have the `system:image-builder` role for the specified project, which allows the user to write or push an image. Otherwise, the `podman push` in the next step will fail. To test, you can create a new project to push the image. 

     3. Push the newly tagged image to your registry: 

```shell-session
sh-4.2# podman push image-registry.openshift-image-registry.svc:5000/openshift/<image>
```


Note

When pushing images to the internal registry, the repository name must use the `<project>/<name>` format. Using multiple project levels in the repository name results in an authentication error.
