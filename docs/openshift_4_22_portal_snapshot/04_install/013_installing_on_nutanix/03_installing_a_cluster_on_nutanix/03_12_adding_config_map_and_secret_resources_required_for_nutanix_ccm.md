# 3.12. Adding config map and secret resources required for Nutanix CCM

Installations on Nutanix require additional `ConfigMap` and `Secret` resources to integrate with the Nutanix Cloud Controller Manager (CCM). 

**Prerequisites**

  * You have created a `manifests` directory within your installation directory. 



**Procedure**

  1. Navigate to the `manifests` directory: 

```shell-session
$ cd <path_to_installation_directory>/manifests
```


  2. Create the `cloud-conf` `ConfigMap` file with the name `openshift-cloud-controller-manager-cloud-config.yaml` and add the following information: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cloud-conf
  namespace: openshift-cloud-controller-manager
data:
  cloud.conf: "{
      \"prismCentral\": {
          \"address\": \"<prism_central_FQDN/IP>\",
          \"port\": 9440,
            \"credentialRef\": {
                \"kind\": \"Secret\",
                \"name\": \"nutanix-credentials\",
                \"namespace\": \"openshift-cloud-controller-manager\"
            }
       },
       \"topologyDiscovery\": {
           \"type\": \"Prism\",
           \"topologyCategories\": null
       },
       \"enableCustomLabeling\": true
     }"
```


For `<prism_central_FQDN/IP>`, specify the Prism Central FQDN or IP address. 

  3. Verify that the file `cluster-infrastructure-02-config.yml` exists and has the following information: 

```yaml
spec:
  cloudConfig:
    key: config
    name: cloud-provider-config
```
