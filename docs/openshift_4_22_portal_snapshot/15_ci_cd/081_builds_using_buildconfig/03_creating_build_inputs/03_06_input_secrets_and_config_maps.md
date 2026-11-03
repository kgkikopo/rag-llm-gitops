# 3.6. Input secrets and config maps

Important

To prevent the contents of input secrets and config maps from appearing in build output container images, use build volumes in your [Docker build](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#builds-using-build-volumes_build-strategies-docker "5.1.6. Using build volumes") and [source-to-image build](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#builds-using-build-volumes_build-strategies-s2i "5.2.6. Using build volumes") strategies. 

In some scenarios, build operations require credentials or other configuration data to access dependent resources, but it is undesirable for that information to be placed in source control. You can define input secrets and input config maps for this purpose. 

For example, when building a Java application with Maven, you can set up a private mirror of Maven Central or JCenter that is accessed by private keys. To download libraries from that private mirror, you have to supply the following: 

  1. A `settings.xml` file configured with the mirror’s URL and connection settings. 
  2. A private key referenced in the settings file, such as `~/.ssh/id_rsa`. 



For security reasons, you do not want to expose your credentials in the application image. 

This example describes a Java application, but you can use the same approach for adding SSL certificates into the `/etc/ssl/certs` directory, API keys or tokens, license files, and more. 

## 3.6.1. What is a secret?

The `Secret` object type provides a mechanism to hold sensitive information such as passwords, OpenShift Container Platform client configuration files, `dockercfg` files, private source repository credentials, and so on. Secrets decouple sensitive content from the pods. You can mount secrets into containers using a volume plugin or the system can use secrets to perform actions on behalf of a pod. 

**YAML Secret Object Definition**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
  namespace: my-namespace
type: Opaque 
```


1

```yaml
data: 
```


2

```yaml
  username: <username> 
```


3

```yaml
  password: <password>
stringData: 
```


4

```yaml
  hostname: myapp.mydomain.com 
```


5

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO8-1)
    

Indicates the structure of the secret’s key names and values. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO8-2)
    

The allowable format for the keys in the `data` field must meet the guidelines in the `DNS_SUBDOMAIN` value in the Kubernetes identifiers glossary. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO8-3)
    

The value associated with keys in the `data` map must be base64 encoded. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO8-4)
    

Entries in the `stringData` map are converted to base64 and the entry are then moved to the `data` map automatically. This field is write-only. The value is only be returned by the `data` field. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO8-5)
    

The value associated with keys in the `stringData` map is made up of plain text strings. 

### 3.6.1.1. Properties of secrets

Key properties include: 

  * Secret data can be referenced independently from its definition. 
  * Secret data volumes are backed by temporary file-storage facilities (tmpfs) and never come to rest on a node. 
  * Secret data can be shared within a namespace. 



### 3.6.1.2. Types of Secrets

The value in the `type` field indicates the structure of the secret’s key names and values. The type can be used to enforce the presence of user names and keys in the secret object. If you do not want validation, use the `opaque` type, which is the default. 

Specify one of the following types to trigger minimal server-side validation to ensure the presence of specific key names in the secret data: 

  * `kubernetes.io/service-account-token`. Uses a service account token. 
  * `kubernetes.io/dockercfg`. Uses the `.dockercfg` file for required Docker credentials. 
  * `kubernetes.io/dockerconfigjson`. Uses the `.docker/config.json` file for required Docker credentials. 
  * `kubernetes.io/basic-auth`. Use with basic authentication. 
  * `kubernetes.io/ssh-auth`. Use with SSH key authentication. 
  * `kubernetes.io/tls`. Use with TLS certificate authorities. 



Specify `type= Opaque` if you do not want validation, which means the secret does not claim to conform to any convention for key names or values. An `opaque` secret, allows for unstructured `key:value` pairs that can contain arbitrary values. 

Note

You can specify other arbitrary types, such as `example.com/my-secret-type`. These types are not enforced server-side, but indicate that the creator of the secret intended to conform to the key/value requirements of that type. 

### 3.6.1.3. Updates to secrets

When you modify the value of a secret, the value used by an already running pod does not dynamically change. To change a secret, you must delete the original pod and create a new pod, in some cases with an identical `PodSpec`. 

Updating a secret follows the same workflow as deploying a new container image. You can use the `kubectl rolling-update` command. 

The `resourceVersion` value in a secret is not specified when it is referenced. Therefore, if a secret is updated at the same time as pods are starting, the version of the secret that is used for the pod is not defined. 

Note

Currently, it is not possible to check the resource version of a secret object that was used when a pod was created. It is planned that pods report this information, so that a controller could restart ones using an old `resourceVersion`. In the interim, do not update the data of existing secrets, but create new ones with distinct names. 

## 3.6.2. Creating secrets

You must create a secret before creating the pods that depend on that secret. 

When creating secrets: 

  * Create a secret object with secret data. 
  * Update the pod service account to allow the reference to the secret. 
  * Create a pod, which consumes the secret as an environment variable or as a file using a `secret` volume. 



**Procedure**

  * To create a secret object from a JSON or YAML file, enter the following command: 

```shell-session
$ oc create -f <filename>
```


For example, you can create a secret from your local `.docker/config.json` file: 

```shell-session
$ oc create secret generic dockerhub \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
```


This command generates a JSON specification of the secret named `dockerhub` and creates the object. 

**YAML Opaque Secret Object Definition**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque 
```


1

```yaml
data:
  username: <username>
  password: <password>
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO9-1)
    

Specifies an _opaque_ secret. 

**Docker Configuration JSON File Secret Object Definition**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: aregistrykey
  namespace: myapps
type: kubernetes.io/dockerconfigjson 
```


1

```yaml
data:
  .dockerconfigjson:bm5ubm5ubm5ubm5ubm5ubm5ubm5ubmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cgYXV0aCBrZXlzCg== 
```


2

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO10-1)
    

Specifies that the secret is using a docker configuration JSON file. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO10-2)
    

The output of a base64-encoded docker configuration JSON file. 




## 3.6.3. Using secrets

After creating secrets, you can create a pod to reference your secret, get logs, and delete the pod. 

**Procedure**

  1. Create the pod to reference your secret by entering the following command: 

```shell-session
$ oc create -f <your_yaml_file>.yaml
```


  2. Get the logs by entering the following command: 

```shell-session
$ oc logs secret-example-pod
```


  3. Delete the pod by entering the following command: 

```shell-session
$ oc delete pod secret-example-pod
```


**Additional resources**

  * Example YAML files with secret data: 

**YAML file of a secret that will create four files**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
data:
  username: <username> 
```


1

```yaml
  password: <password> 
```


2

```yaml
stringData:
  hostname: myapp.mydomain.com 
```


3

```yaml
  secret.properties: |- 
```


4

```yaml
    property1=valueA
    property2=valueB
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO11-1)
    

File contains decoded values. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO11-2)
    

File contains decoded values. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO11-3)
    

File contains the provided string. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO11-4)
    

File contains the provided data. 

**YAML file of a pod populating files in a volume with secret data**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-example-pod
spec:
  containers:
    - name: secret-test-container
      image: busybox
      command: [ "/bin/sh", "-c", "cat /etc/secret-volume/*" ]
      volumeMounts:
          # name must match the volume name below
          - name: secret-volume
            mountPath: /etc/secret-volume
            readOnly: true
  volumes:
    - name: secret-volume
      secret:
        secretName: test-secret
  restartPolicy: Never
```


**YAML file of a pod populating environment variables with secret data**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-example-pod
spec:
  containers:
    - name: secret-test-container
      image: busybox
      command: [ "/bin/sh", "-c", "export" ]
      env:
        - name: TEST_SECRET_USERNAME_ENV_VAR
          valueFrom:
            secretKeyRef:
              name: test-secret
              key: username
  restartPolicy: Never
```


**YAML file of a`BuildConfig` object that populates environment variables with secret data**

```yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: secret-example-bc
spec:
  strategy:
    sourceStrategy:
      env:
      - name: TEST_SECRET_USERNAME_ENV_VAR
        valueFrom:
          secretKeyRef:
            name: test-secret
            key: username
```


## 3.6.4. Adding input secrets and config maps

To provide credentials and other configuration data to a build without placing them in source control, you can define input secrets and input config maps. 

In some scenarios, build operations require credentials or other configuration data to access dependent resources. To make that information available without placing it in source control, you can define input secrets and input config maps. 

**Procedure**

To add an input secret, config maps, or both to an existing `BuildConfig` object: 

  1. If the `ConfigMap` object does not exist, create it by entering the following command: 

```shell-session
$ oc create configmap settings-mvn \
    --from-file=settings.xml=<path/to/settings.xml>
```


This creates a new config map named `settings-mvn`, which contains the plain text content of the `settings.xml` file. 

Tip

You can alternatively apply the following YAML to create the config map: 

```yaml
apiVersion: core/v1
kind: ConfigMap
metadata:
  name: settings-mvn
data:
  settings.xml: |
    <settings>
    … # Insert maven settings here
    </settings>
```


  2. If the `Secret` object does not exist, create it by entering the following command: 

```shell-session
$ oc create secret generic secret-mvn \
    --from-file=ssh-privatekey=<path/to/.ssh/id_rsa> \
    --type=kubernetes.io/ssh-auth
```


This creates a new secret named `secret-mvn`, which contains the base64 encoded content of the `id_rsa` private key. 

Tip

You can alternatively apply the following YAML to create the input secret: 

```yaml
apiVersion: core/v1
kind: Secret
metadata:
  name: secret-mvn
type: kubernetes.io/ssh-auth
data:
  ssh-privatekey: |
    # Insert ssh private key, base64 encoded
```


  3. Add the config map and secret to the `source` section in the existing `BuildConfig` object: 

```yaml
source:
  git:
    uri: https://github.com/wildfly/quickstart.git
  contextDir: helloworld
  configMaps:
    - configMap:
        name: settings-mvn
  secrets:
    - secret:
        name: secret-mvn
```


  4. To include the secret and config map in a new `BuildConfig` object, enter the following command: 

```shell-session
$ oc new-build \
    openshift/wildfly-101-centos7~https://github.com/wildfly/quickstart.git \
    --context-dir helloworld --build-secret “secret-mvn” \
    --build-config-map "settings-mvn"
```


During the build, the build process copies the `settings.xml` and `id_rsa` files into the directory where the source code is located. In OpenShift Container Platform S2I builder images, this is the image working directory, which is set using the `WORKDIR` instruction in the `Dockerfile`. If you want to specify another directory, add a `destinationDir` to the definition: 

```yaml
source:
  git:
    uri: https://github.com/wildfly/quickstart.git
  contextDir: helloworld
  configMaps:
    - configMap:
        name: settings-mvn
      destinationDir: ".m2"
  secrets:
    - secret:
        name: secret-mvn
      destinationDir: ".ssh"
```


You can also specify the destination directory when creating a new `BuildConfig` object by entering the following command: 

```shell-session
$ oc new-build \
    openshift/wildfly-101-centos7~https://github.com/wildfly/quickstart.git \
    --context-dir helloworld --build-secret “secret-mvn:.ssh” \
    --build-config-map "settings-mvn:.m2"
```


In both cases, the `settings.xml` file is added to the `./.m2` directory of the build environment, and the `id_rsa` key is added to the `./.ssh` directory. 




## 3.6.5. Source-to-image strategy

When using a `Source` strategy, all defined input secrets are copied to their respective `destinationDir`. If you left `destinationDir` empty, then the secrets are placed in the working directory of the builder image. 

The same rule is used when a `destinationDir` is a relative path. The secrets are placed in the paths that are relative to the working directory of the image. The final directory in the `destinationDir` path is created if it does not exist in the builder image. All preceding directories in the `destinationDir` must exist, or an error will occur. 

Note

Input secrets are added as world-writable, have `0666` permissions, and are truncated to size zero after executing the `assemble` script. This means that the secret files exist in the resulting image, but they are empty for security reasons. 

Input config maps are not truncated after the `assemble` script completes. 

## 3.6.6. Docker strategy

When using a docker strategy, you can add all defined input secrets into your container image using the [`ADD`](https://docs.docker.com/engine/reference/builder/#add) and [`COPY` instructions](https://docs.docker.com/engine/reference/builder/#copy) in your Dockerfile. 

If you do not specify the `destinationDir` for a secret, then the files are copied into the same directory in which the Dockerfile is located. If you specify a relative path as `destinationDir`, then the secrets are copied into that directory, relative to your Dockerfile location. This makes the secret files available to the Docker build operation as part of the context directory used during the build. 

**Example of a Dockerfile referencing secret and config map data**

```plaintext
FROM centos/ruby-22-centos7

USER root
COPY ./secret-dir /secrets
COPY ./config /

# Create a shell script that will output secrets and ConfigMaps when the image is run
RUN echo '#!/bin/sh' > /input_report.sh
RUN echo '(test -f /secrets/secret1 && echo -n "secret1=" && cat /secrets/secret1)' >> /input_report.sh
RUN echo '(test -f /config && echo -n "relative-configMap=" && cat /config)' >> /input_report.sh
RUN chmod 755 /input_report.sh

CMD ["/bin/sh", "-c", "/input_report.sh"]
```


Important

Users normally remove their input secrets from the final application image so that the secrets are not present in the container running from that image. However, the secrets still exist in the image itself in the layer where they were added. This removal is part of the Dockerfile itself. 

To prevent the contents of input secrets and config maps from appearing in the build output container images and avoid this removal process altogether, [use build volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/build-strategies#builds-using-build-volumes_build-strategies-docker "5.1.6. Using build volumes") in your Docker build strategy instead. 

## 3.6.7. Custom strategy

When using a Custom strategy, all the defined input secrets and config maps are available in the builder container in the `/var/run/secrets/openshift.io/build` directory. The custom build image must use these secrets and config maps appropriately. With the Custom strategy, you can define secrets as described in Custom strategy options. 

There is no technical difference between existing strategy secrets and the input secrets. However, your builder image can distinguish between them and use them differently, based on your build use case. 

The input secrets are always mounted into the `/var/run/secrets/openshift.io/build` directory, or your builder can parse the `$BUILD` environment variable, which includes the full build object. 

Important

If a pull secret for the registry exists in both the namespace and the node, builds default to using the pull secret in the namespace.
