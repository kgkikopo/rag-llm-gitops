# 16.2. View TLS security profile details

To check the minimum TLS version and ciphers that a security profile applies in OpenShift Container Platform, you can inspect the profile configuration for the Ingress Controller, control plane, or kubelet. Use the `oc explain` command to display settings for a predefined or custom profile. 

Important

The effective configuration of minimum TLS version and list of ciphers for a profile might differ between components. 

**Procedure**

  * View details for a specific TLS security profile: 

```shell-session
$ oc explain <component>.spec.tlsSecurityProfile.<profile>
```


  * For `<component>`, specify `ingresscontroller`, `apiserver`, or `kubeletconfig`. For `<profile>`, specify `old`, `intermediate`, or `custom`. 

For example, to check the ciphers included for the `intermediate` profile for the control plane: 

```shell-session
$ oc explain apiserver.spec.tlsSecurityProfile.intermediate
```


**Example output**

```shell-session
KIND:     APIServer
VERSION:  config.openshift.io/v1

DESCRIPTION:
    intermediate is a TLS security profile based on:
    https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29
    and looks like this (yaml):
    ciphers: - TLS_AES_128_GCM_SHA256 - TLS_AES_256_GCM_SHA384 -
    TLS_CHACHA20_POLY1305_SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 -
    ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES256-GCM-SHA384 -
    ECDHE-RSA-AES256-GCM-SHA384 - ECDHE-ECDSA-CHACHA20-POLY1305 -
    ECDHE-RSA-CHACHA20-POLY1305 - DHE-RSA-AES128-GCM-SHA256 -
    DHE-RSA-AES256-GCM-SHA384 minTLSVersion: TLSv1.2
```


  * View all details for the `tlsSecurityProfile` field of a component: 

```shell-session
$ oc explain <component>.spec.tlsSecurityProfile
```


  * For `<component>`, specify `ingresscontroller`, `apiserver`, or `kubeletconfig`. 

For example, to check all details for the `tlsSecurityProfile` field for the Ingress Controller: 

```shell-session
$ oc explain ingresscontroller.spec.tlsSecurityProfile
```


**Example output**

```shell-session
KIND:     IngressController
VERSION:  operator.openshift.io/v1

RESOURCE: tlsSecurityProfile <Object>

DESCRIPTION:
     ...

FIELDS:
   custom	<>
     custom is a user-defined TLS security profile. Be extremely careful using a
     custom profile as invalid configurations can be catastrophic. An example
     custom profile looks like this:
     ciphers: - ECDHE-ECDSA-CHACHA20-POLY1305 - ECDHE-RSA-CHACHA20-POLY1305 -
     ECDHE-RSA-AES128-GCM-SHA256 - ECDHE-ECDSA-AES128-GCM-SHA256 minTLSVersion:
     TLSv1.1

   intermediate	<>
     intermediate is a TLS security profile based on:
     https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29
     and looks like this (yaml):
     (A list of ciphers and the minimum version for the intermediate profile opens here.)

   modern	<>
     modern is a TLS security profile based on:
     https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility and
     looks like this (yaml):
     (A list of ciphers and the minimum version for the modern profile opens here.)
     NOTE: Currently unsupported.

   old	<>
     old is a TLS security profile based on:
     https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility
     and looks like this (yaml):
     (A list of ciphers and the minimum version for the old profile opens here.)

   type	<string>
     ...
```
