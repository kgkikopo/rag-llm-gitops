# 3.8. Using docker credentials for private registries

You can supply builds with a .`docker/config.json` file with valid credentials for private container registries. This allows you to push the output image into a private container image registry or pull a builder image from the private container image registry that requires authentication. 

You can supply credentials for multiple repositories within the same registry, each with credentials specific to that registry path. 

Note

For the OpenShift Container Platform container image registry, this is not required because secrets are generated automatically for you by OpenShift Container Platform. 

The `.docker/config.json` file is found in your home directory by default and has the following format: 

```yaml
auths:
  index.docker.io/v1/: 
```


1

```yaml
    auth: "YWRfbGzhcGU6R2labnRib21ifTE=" 
```


2

```yaml
    email: "user@example.com" 
```


3

```yaml
  docker.io/my-namespace/my-user/my-image: 
```


4

```yaml
    auth: "GzhYWRGU6R2fbclabnRgbkSp=""
    email: "user@example.com"
  docker.io/my-namespace: 
```


5

```yaml
    auth: "GzhYWRGU6R2deesfrRgbkSp=""
    email: "user@example.com"
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO12-1)
    

URL of the registry. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO12-2)
    

Encrypted password. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO12-3)
    

Email address for the login. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO12-4)
    

URL and credentials for a specific image in a namespace. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO12-5)
    

URL and credentials for a registry namespace. 

You can define multiple container image registries or define multiple repositories in the same registry. Alternatively, you can also add authentication entries to this file by running the `docker login` command. The file will be created if it does not exist. 

Kubernetes provides `Secret` objects, which can be used to store configuration and passwords. 

**Prerequisites**

  * You must have a `.docker/config.json` file. 



**Procedure**

  1. Create the secret from your local `.docker/config.json` file by entering the following command: 

```shell-session
$ oc create secret generic dockerhub \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
```


This generates a JSON specification of the secret named `dockerhub` and creates the object. 

  2. Add a `pushSecret` field into the `output` section of the `BuildConfig` and set it to the name of the `secret` that you created, which in the previous example is `dockerhub`: 

```yaml
spec:
  output:
    to:
      kind: "DockerImage"
      name: "private.registry.com/org/private-image:latest"
    pushSecret:
      name: "dockerhub"
```


You can use the `oc set build-secret` command to set the push secret on the build configuration: 

```shell-session
$ oc set build-secret --push bc/sample-build dockerhub
```


You can also link the push secret to the service account used by the build instead of specifying the `pushSecret` field. By default, builds use the `builder` service account. The push secret is automatically added to the build if the secret contains a credential that matches the repository hosting the build’s output image. 

```shell-session
$ oc secrets link builder dockerhub
```


  3. Pull the builder container image from a private container image registry by specifying the `pullSecret` field, which is part of the build strategy definition: 

```yaml
strategy:
  sourceStrategy:
    from:
      kind: "DockerImage"
      name: "docker.io/user/private_repository"
    pullSecret:
      name: "dockerhub"
```


You can use the `oc set build-secret` command to set the pull secret on the build configuration: 

```shell-session
$ oc set build-secret --pull bc/sample-build dockerhub
```


Note

This example uses `pullSecret` in a Source build, but it is also applicable in Docker and Custom builds. 

You can also link the pull secret to the service account used by the build instead of specifying the `pullSecret` field. By default, builds use the `builder` service account. The pull secret is automatically added to the build if the secret contains a credential that matches the repository hosting the build’s input image. To link the pull secret to the service account used by the build instead of specifying the `pullSecret` field, enter the following command: 

```shell-session
$ oc secrets link builder dockerhub
```


Note

You must specify a `from` image in the `BuildConfig` spec to take advantage of this feature. Docker strategy builds generated by `oc new-build` or `oc new-app` may not do this in some situations.
