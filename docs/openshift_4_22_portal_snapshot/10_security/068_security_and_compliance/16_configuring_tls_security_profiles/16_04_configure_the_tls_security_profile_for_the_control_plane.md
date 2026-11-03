# 16.4. Configure the TLS security profile for the control plane

To configure a TLS security profile for the control plane, edit the `APIServer` custom resource (CR) to specify a predefined or custom TLS security profile. 

Setting the TLS security profile in the `APIServer` CR propagates the setting to the following control plane components: 

  * Kubernetes API server 
  * Kubernetes controller manager 
  * Kubernetes scheduler 
  * OpenShift API server 
  * OpenShift OAuth API server 
  * OpenShift OAuth server 
  * etcd 
  * Machine Config Operator 
  * Machine Config Server 



Note

The default TLS security profile for the Ingress Controller is based on the TLS security profile set for the API server. 

If a TLS security profile is not configured, the default TLS security profile is `Intermediate`. 

The following YAML is a sample `APIServer` CR that configures the `Old` TLS security profile. 

```yaml
apiVersion: config.openshift.io/v1
kind: APIServer
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
```


The TLS security profile defines the minimum TLS version and the TLS ciphers required to communicate with the control plane components. 

You can see the configured TLS security profile in the `APIServer` custom resource (CR) under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Edit the default `APIServer` CR to configure the TLS security profile: 

```shell-session
$ oc edit APIServer cluster
```


  2. Add the `spec.tlsSecurityProfile` field: 

**Sample`APIServer` CR for a `Custom` profile**

```yaml
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  tlsSecurityProfile:
    type: Custom
    custom:
      ciphers:
      - ECDHE-ECDSA-CHACHA20-POLY1305
      - ECDHE-RSA-CHACHA20-POLY1305
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-ECDSA-AES128-GCM-SHA256
      minTLSVersion: VersionTLS11
```


     * Specify the value for the `spec.tlsSecurityProfile.type` parameter. The TLS security profile types are `Old`, `Intermediate`, or `Custom`. The default type is `Intermediate`. 
     * Specify the appropriate field for the selected `spec.tlsSecurityProfile`. The fields are `old: {}`, `intermediate: {}`, `modern: {}`, or `custom:`. 
     * For the `custom` type, specify a list of TLS ciphers and the minimum accepted TLS version. 

  3. Save the file to apply the changes. 



**Verification**

  1. Verify that the TLS security profile is set in the `APIServer` CR: 

```shell-session
$ oc describe apiserver cluster
```


**Example output**

```shell-session
Name:         cluster
Namespace:
 ...
API Version:  config.openshift.io/v1
Kind:         APIServer
 ...
Spec:
  Audit:
    Profile:  Default
  Tls Security Profile:
    Custom:
      Ciphers:
        ECDHE-ECDSA-CHACHA20-POLY1305
        ECDHE-RSA-CHACHA20-POLY1305
        ECDHE-RSA-AES128-GCM-SHA256
        ECDHE-ECDSA-AES128-GCM-SHA256
      Min TLS Version:  VersionTLS11
    Type:               Custom
 ...
```


  2. Verify that the TLS security profile is set in the `etcd` CR: 

```shell-session
$ oc describe etcd cluster
```


**Example output**

```shell-session
Name:         cluster
Namespace:
 ...
API Version:  operator.openshift.io/v1
Kind:         Etcd
 ...
Spec:
  Log Level:         Normal
  Management State:  Managed
  Observed Config:
    Serving Info:
      Cipher Suites:
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
        TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
      Min TLS Version:           VersionTLS12
 ...
```


  3. Verify that the TLS security profile is set in the Machine Config Server pod: 

```shell-session
$ oc logs machine-config-server-5msdv -n openshift-machine-config-operator
```


**Example output**

```shell-session
# ...
I0905 13:48:36.968688       1 start.go:51] Launching server with tls min version: VersionTLS12 & cipher suites [TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256]
# ...
```
