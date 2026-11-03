# 10.5. Running builds using SharedSecret objects

You can use a `SharedSecret` object to securely access the entitlement keys of a cluster in builds. 

The `SharedSecret` object allows you to share and synchronize secrets across namespaces. 

Important

The Shared Resource CSI Driver feature is now generally available in [Builds for Red Hat OpenShift 1.1](https://docs.redhat.com/en/documentation/builds_for_red_hat_openshift/1.1). This feature is now removed in OpenShift Container Platform 4.18 and later. To use this feature, ensure that you are using Builds for Red Hat OpenShift 1.1 or later. 

**Prerequisites**

  * You have enabled the `TechPreviewNoUpgrade` feature set by using the feature gates. For more information, see [Enabling features using feature gates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling). 
  * You must have permission to perform the following actions: 

    * Create build configs and start builds. 
    * Discover which `SharedSecret` CR instances are available by entering the `oc get sharedsecrets` command and getting a non-empty list back. 
    * Determine if the `builder` service account available to you in your namespace is allowed to use the given `SharedSecret` CR instance. In other words, you can run `oc adm policy who-can use <identifier of specific SharedSecret>` to see if the `builder` service account in your namespace is listed. 




Note

If neither of the last two prerequisites in this list are met, establish, or ask someone to establish, the necessary role-based access control (RBAC) so that you can discover `SharedSecret` CR instances and enable service accounts to use `SharedSecret` CR instances. 

**Procedure**

  1. Use `oc apply` to create a `SharedSecret` object instance with the cluster’s entitlement secret. 

Important

You must have cluster administrator permissions to create `SharedSecret` objects. 

**Example`oc apply -f` command with YAML `Role` object definition**

```shell-session
$ oc apply -f - <<EOF
kind: SharedSecret
apiVersion: sharedresource.openshift.io/v1alpha1
metadata:
  name: etc-pki-entitlement
spec:
  secretRef:
    name: etc-pki-entitlement
    namespace: openshift-config-managed
EOF
```


  2. Create a role to grant the `builder` service account permission to access the `SharedSecret` object: 

**Example`oc apply -f` command**

```shell-session
$ oc apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: builder-etc-pki-entitlement
  namespace: build-namespace
rules:
  - apiGroups:
      - sharedresource.openshift.io
    resources:
      - sharedsecrets
    resourceNames:
      - etc-pki-entitlement
    verbs:
      - use
EOF
```


  3. Create a `RoleBinding` object that grants the `builder` service account permission to access the `SharedSecret` object by running the following command: 

**Example`oc create rolebinding` command**

```shell-session
$ oc create rolebinding builder-etc-pki-entitlement --role=builder-etc-pki-entitlement --serviceaccount=build-namespace:builder
```


  4. Add the entitlement secret to your `BuildConfig` object by using a CSI volume mount: 

**Example YAML`BuildConfig` object definition**

```yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: uid-wrapper-rhel9
  namespace: build-namespace
spec:
  runPolicy: Serial
  source:
    dockerfile: |
      FROM registry.redhat.io/ubi9/ubi:latest
      RUN rm -rf /etc/rhsm-host 
```


1

```yaml
      RUN yum --enablerepo=codeready-builder-for-rhel-9-x86_64-rpms install \ 
```


2

```yaml
          nss_wrapper \
          uid_wrapper -y && \
          yum clean all -y
      RUN ln -s /run/secrets/rhsm /etc/rhsm-host 
```


3

```yaml
  strategy:
    type: Docker
    dockerStrategy:
      volumes:
        - mounts:
            - destinationPath: "/etc/pki/entitlement"
          name: etc-pki-entitlement
          source:
            csi:
              driver: csi.sharedresource.openshift.io
              readOnly: true 
```


4

```yaml
              volumeAttributes:
                sharedSecret: etc-pki-entitlement 
```


5

```yaml
            type: CSI
```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO29-1)
    

You must include the command to remove the `/etc/rhsm-host` directory and all its contents in the Dockerfile before executing any `yum` or `dnf` commands. 

[2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO29-2)
    

Use the [Red Hat Package Browser](https://access.redhat.com/downloads/content/package-browser) to find the correct repositories for your installed packages. 

[3](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO29-3)
    

You must restore the `/etc/rhsm-host` symbolic link to keep your image compatible with other Red Hat container images. 

[4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO29-4)
    

You must set `readOnly` to `true` to mount the shared resource in the build. 

[5](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/running-entitled-builds#CO29-5)
    

Reference the name of the `SharedSecret` object to include it in the build. 

  5. Start a build from the `BuildConfig` object and follow the logs using the `oc` command. 

```shell-session
$ oc start-build uid-wrapper-rhel9 -n build-namespace -F
```
