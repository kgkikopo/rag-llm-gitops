# 3.9. Build environments

As with pod environment variables, build environment variables can be defined in terms of references to other resources or variables using the Downward API. There are some exceptions, which are noted. 

You can also manage environment variables defined in the `BuildConfig` with the `oc set env` command. 

Note

Referencing container resources using `valueFrom` in build environment variables is not supported as the references are resolved before the container is created. 

## 3.9.1. Using build fields as environment variables

You can inject information about the build object by setting the `fieldPath` environment variable source to the `JsonPath` of the field from which you are interested in obtaining the value. 

Note

Jenkins Pipeline strategy does not support `valueFrom` syntax for environment variables. 

**Procedure**

  * Set the `fieldPath` environment variable source to the `JsonPath` of the field from which you are interested in obtaining the value: 

```yaml
env:
  - name: FIELDREF_ENV
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
```


## 3.9.2. Using secrets as environment variables

You can make key values from secrets available as environment variables using the `valueFrom` syntax. 

Important

This method shows the secrets as plain text in the output of the build pod console. To avoid this, use input secrets and config maps instead. 

**Procedure**

  * To use a secret as an environment variable, set the `valueFrom` syntax: 

```yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: secret-example-bc
spec:
  strategy:
    sourceStrategy:
      env:
      - name: MYVAL
        valueFrom:
          secretKeyRef:
            key: myval
            name: mysecret
```


**Additional resources**

  * [Input secrets and config maps](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#builds-input-secrets-configmaps_creating-build-inputs "3.6. Input secrets and config maps")
