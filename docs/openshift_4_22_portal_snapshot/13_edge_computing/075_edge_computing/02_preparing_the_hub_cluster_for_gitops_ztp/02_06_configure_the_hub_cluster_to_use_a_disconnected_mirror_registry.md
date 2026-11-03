# 2.6. Configure the hub cluster to use a disconnected mirror registry

You can configure the hub cluster to use a disconnected mirror registry for a disconnected environment. 

**Prerequisites**

  * You have a disconnected hub cluster installation with Red Hat Advanced Cluster Management (RHACM) 2.17 installed. 
  * You have hosted the `rootfs` and `iso` images on an HTTP server. See the _Additional resources_ section for guidance about _Mirroring the OpenShift Container Platform image repository_. 



Warning

If you enable TLS for the HTTP server, you must confirm the root certificate is signed by an authority trusted by the client and verify the trusted certificate chain between your OpenShift Container Platform hub and managed clusters and the HTTP server. Using a server configured with an untrusted certificate prevents the images from being downloaded to the image creation service. Using untrusted HTTPS servers is not supported. 

**Procedure**

  1. Create a `ConfigMap` containing the mirror registry config: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: assisted-installer-mirror-config
  namespace: multicluster-engine
  labels:
    app: assisted-service
data:
  ca-bundle.crt: |
    -----BEGIN CERTIFICATE-----
    <certificate_contents>
    -----END CERTIFICATE-----

  registries.conf: |
    unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

    [[registry]]
       prefix = ""
       location = "quay.io/example-repository"
       mirror-by-digest-only = true

       [[registry.mirror]]
       location = "mirror1.registry.corp.com:5000/example-repository"
```


where: 

`namespace: multicluster-engine`
     The `ConfigMap` namespace must be set to `multicluster-engine`. 
`ca-bundle.crt`
     The mirror registry’s certificate that is used when creating the mirror registry. 
`registries.conf`
     The configuration file for the mirror registry. The mirror registry configuration adds mirror information to the `/etc/containers/registries.conf` file in the discovery image. The mirror information is stored in the `imageContentSources` section of the `install-config.yaml` file when the information is passed to the installation program. The Assisted Service pod that runs on the hub cluster fetches the container images from the configured mirror registry. 
`location = "quay.io/example-repository"`
     The URL of the mirror registry. You must use the URL from the `imageContentSources` section by running the `oc adm release mirror` command when you configure the mirror registry. For more information, see the _Mirroring the OpenShift Container Platform image repository_ section. 
`location = "mirror1.registry.corp.com:5000/example-repository"`
     The registries defined in the `registries.conf` file must be scoped by repository, not by registry. In this example, both the `quay.io/example-repository` and the `mirror1.registry.corp.com:5000/example-repository` repositories are scoped by the `example-repository` repository. 

This updates `mirrorRegistryRef` in the `AgentServiceConfig` custom resource, as shown in this example output: 

```yaml
apiVersion: agent-install.openshift.io/v1beta1
kind: AgentServiceConfig
metadata:
  name: agent
  namespace: multicluster-engine
spec:
  databaseStorage:
    volumeName: <db_pv_name>
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: <db_storage_size>
  filesystemStorage:
    volumeName: <fs_pv_name>
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: <fs_storage_size>
  mirrorRegistryRef:
    name: assisted-installer-mirror-config
  osImages:
    - openshiftVersion: <ocp_version>
      url: <iso_url>
```


where: 

`namespace: multicluster-engine`
     Set the `AgentServiceConfig` namespace to `multicluster-engine` to match the `ConfigMap` namespace. 
`assisted-installer-mirror-config`
     Set `mirrorRegistryRef.name` to match the definition specified in the related `ConfigMap` CR. 
`<ocp_version>`
     Set the OpenShift Container Platform version to either the x.y or x.y.z format. 
`<iso_url>`
     Set the URL for the ISO hosted on the `httpd` server. 

Important

A valid NTP server is required during cluster installation. Ensure that a suitable NTP server is available and can be reached from the installed clusters through the disconnected network. 




**Additional resources**

  * [Mirroring the OpenShift Container Platform repository](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installation-mirror-repository_installing-mirroring-installation-images)
