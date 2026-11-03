# 16.3. Configure the TLS security profile for the Ingress Controller

To configure a TLS security profile for an Ingress Controller, edit the `IngressController` custom resource (CR) to specify a predefined or custom TLS security profile. 

If a TLS security profile is not configured, the default value is based on the TLS security profile set for the API server, as shown in the following example: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
```


The TLS security profile defines the minimum TLS version and the TLS ciphers for TLS connections for Ingress Controllers. 

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `IngressController` custom resource (CR) under `Status.Tls Profile` and the configured TLS security profile under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed under both parameters. 

Note

The HAProxy Ingress Controller image supports TLS `1.3` and the `Modern` profile. 

The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Edit the `IngressController` CR in the `openshift-ingress-operator` project to configure the TLS security profile: 

```shell-session
$ oc edit IngressController default -n openshift-ingress-operator.
```


  2. Add the `spec.tlsSecurityProfile` field: 

**Sample`IngressController` CR for a `Custom` profile**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
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
 ...
```


     * Specify the value for the `spec.tlsSecurityProfile` parameter. The TLS security profile types are `Old`, `Intermediate`, or `Custom`. The default type is `Intermediate`. 
     * Specify the appropriate field for the selected `spec.tlsSecurityProfile.type`. The fields are `old: {}`, `intermediate: {}`, `modern: {}`, or `custom:`. 
     * For the `custom` type, specify a list of TLS ciphers and the minimum accepted TLS version. 

  3. Save the file to apply the changes. 



**Verification**

  * Verify that the profile is set in the `IngressController` CR: 

```shell-session
$ oc describe IngressController default -n openshift-ingress-operator
```


**Example output**

```shell-session
Name:         default
Namespace:    openshift-ingress-operator
Labels:       <none>
Annotations:  <none>
API Version:  operator.openshift.io/v1
Kind:         IngressController
 ...
Spec:
 ...
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
