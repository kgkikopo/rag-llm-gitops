# 21.7. Running latency tests in a disconnected cluster

The CNF tests image can run tests in a disconnected cluster that is not able to reach external registries. This requires two steps: 

  1. Mirroring the `cnf-tests` image to the custom disconnected registry. 
  2. Instructing the tests to consume the images from the custom disconnected registry. 



## 21.7.1. Mirroring the images to a custom registry accessible from the cluster

To make required images accessible from your cluster, mirror them to a custom registry. Performing this synchronization ensures that your deployment has the necessary container files, which is particularly useful in restricted or disconnected network environments. 

A `mirror` executable is shipped in the image to provide the input required by `oc` to mirror the test image to a local registry. 

**Procedure**

  1. Run the following command from an intermediate machine that has access to the cluster and registry.redhat.io: 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -e KUBECONFIG=/kubeconfig/kubeconfig \
registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22 \
/usr/bin/mirror -registry <disconnected_registry> | oc image mirror -f -
```


where: 

`<disconnected_registry>`
     Specifies the disconnected mirror registry you have configured, such as `my.local.registry:5000/`. 

  2. When you have mirrored the `cnf-tests` image into the disconnected registry, you must override the original registry used to fetch the images when running the tests by a command similar to the following example: 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -e KUBECONFIG=/kubeconfig/kubeconfig \
-e IMAGE_REGISTRY="<disconnected_registry>" \
-e CNF_TESTS_IMAGE="cnf-tests-rhel9:v4.22" \
-e LATENCY_TEST_RUNTIME=<time_in_seconds> \
<disconnected_registry>/cnf-tests-rhel9:v4.22 /usr/bin/test-run.sh --ginkgo.v --ginkgo.timeout="24h"
```


**Additional resources**

  * [registry.redhat.io](https://catalog.redhat.com/software/containers/explore)



## 21.7.2. Configuring the tests to consume images from a custom registry

You can run the latency tests by using a custom test image and image registry using `CNF_TESTS_IMAGE` and `IMAGE_REGISTRY` variables. 

**Procedure**

  * To configure the latency tests to use a custom test image and image registry, run a command similar to the following example: 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -e KUBECONFIG=/kubeconfig/kubeconfig \
-e IMAGE_REGISTRY="<custom_image_registry>" \
-e CNF_TESTS_IMAGE="<custom_cnf-tests_image>" \
-e LATENCY_TEST_RUNTIME=<time_in_seconds> \
registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22 /usr/bin/test-run.sh --ginkgo.v --ginkgo.timeout="24h"
```


where: 

`<custom_image_registry>`
     Specifies the custom image registry, for example, `custom.registry:5000/`. 
`<custom_cnf-tests_image>`
     Specifies the custom cnf-tests image, for example, `custom-cnf-tests-image:latest`. 




## 21.7.3. Mirroring images to the cluster OpenShift image registry

To make container images locally available for your deployment, mirror them to the built-in OpenShift image registry. This integrated component runs as a standard workload on your OpenShift Container Platform cluster to ensure continuous access to required files. 

**Procedure**

  1. Gain external access to the registry by exposing the registry with a route. You can do this task by running a command similar to the following example: 

```shell-session
$ oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
```


  2. Fetch the registry endpoint by running a command similar to the following example: 

```shell-session
$ REGISTRY=$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')
```


  3. Create a namespace for exposing the images by running a command similar to the following example: 

```shell-session
$ oc create ns cnftests
```


  4. Make the image stream available to all the namespaces used for tests. This is required to allow the tests namespaces to fetch the images from the `cnf-tests` image stream. Run commands similar to the following examples: 

```shell-session
$ oc policy add-role-to-user system:image-puller system:serviceaccount:cnf-features-testing:default --namespace=cnftests
```


```shell-session
$ oc policy add-role-to-user system:image-puller system:serviceaccount:performance-addon-operators-testing:default --namespace=cnftests
```


  5. Retrieve the docker secret name by running a command similar to the following example: 

```shell-session
$ SECRET=$(oc -n cnftests get secret | grep builder-docker | awk {'print $1'}
```


  6. Retrieve the docker auth token by running a command similar to the following example: 

```shell-session
$ TOKEN=$(oc -n cnftests get secret $SECRET -o jsonpath="{.data['\.dockercfg']}" | base64 --decode | jq '.["image-registry.openshift-image-registry.svc:5000"].auth')
```


  7. Create a `dockerauth.json` file, for example: 

```bash
$ echo "{\"auths\": { \"$REGISTRY\": { \"auth\": $TOKEN } }}" > dockerauth.json
```


  8. Mirror the image by running a command similar to the following example: 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -e KUBECONFIG=/kubeconfig/kubeconfig \
registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22 \
/usr/bin/mirror -registry $REGISTRY/cnftests |  oc image mirror --insecure=true \
-a=$(pwd)/dockerauth.json -f -
```


  9. Run the tests by running a command similar to the following example: 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -e KUBECONFIG=/kubeconfig/kubeconfig \
-e LATENCY_TEST_RUNTIME=<time_in_seconds> \
-e IMAGE_REGISTRY=image-registry.openshift-image-registry.svc:5000/cnftests cnf-tests-local:latest /usr/bin/test-run.sh --ginkgo.v --ginkgo.timeout="24h"
```


## 21.7.4. Mirroring a different set of test images

You can optionally change the default upstream images that are mirrored for the latency tests. 

**Procedure**

  1. The `mirror` command tries to mirror the upstream images by default. This can be overridden by passing a file with the following format to the image: 

```yaml
[
    {
        "registry": "public.registry.io:5000",
        "image": "imageforcnftests:4.22"
    }
]
```


  2. Pass the file to the `mirror` command, for example saving it locally as `images.json`. With the following command, the local path is mounted in `/kubeconfig` inside the container and that can be passed to the mirror command. 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -e KUBECONFIG=/kubeconfig/kubeconfig \
registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22 /usr/bin/mirror \
--registry "my.local.registry:5000/" --images "/kubeconfig/images.json" \
|  oc image mirror -f -
```
