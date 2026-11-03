# 16.1. Understand TLS security profiles

You can use a TLS (Transport Layer Security) security profile, as described in this section, to define which TLS ciphers are required by various OpenShift Container Platform components. 

The OpenShift Container Platform TLS security profiles are based on [Mozilla recommended configurations](https://wiki.mozilla.org/Security/Server_Side_TLS). 

You can specify one of the following TLS security profiles for each component: 

Table 16.1. TLS security profilesProfile| Description  
---|---  
`Old` |  This profile is intended for use with legacy clients or libraries. The profile is based on the [Old backward compatibility](https://wiki.mozilla.org/Security/Server_Side_TLS#Old_backward_compatibility) recommended configuration.  The `Old` profile requires a minimum TLS version of 1.0.  Note For the Ingress Controller, the minimum TLS version is converted from 1.0 to 1.1.   
`Intermediate` |  This profile is the default TLS security profile for the Ingress Controller, kubelet, and control plane. The profile is based on the [Intermediate compatibility](https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28recommended.29) recommended configuration.  The `Intermediate` profile requires a minimum TLS version of 1.2.  Note This profile is the recommended configuration for the majority of clients.   
`Modern` |  This profile is intended for use with modern clients that have no need for backwards compatibility. This profile is based on the [Modern compatibility](https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility) recommended configuration.  The `Modern` profile requires a minimum TLS version of 1.3.   
`Custom` |  This profile allows you to define the TLS version and ciphers to use.  Warning Use caution when using a `Custom` profile, because invalid configurations can cause problems.   
Show more

Note

When using one of the predefined profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 might cause a new profile configuration to be applied, resulting in a rollout.
