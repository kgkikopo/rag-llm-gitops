# Chapter 16. Configuring TLS security profiles

To enforce secure cryptographic libraries for the OpenShift Container Platform components, cluster administrators can configure TLS security profiles to control cipher usage when the client connects to the Ingress Controller, the control plane, or the kubelet. 

The control plane includes the following components: 

  * Kubernetes API server 
  * Kubernetes controller manager 
  * Kubernetes scheduler 
  * OpenShift API server 
  * OpenShift OAuth API server 
  * OpenShift OAuth server 
  * etcd 
  * Machine Config Operator 
  * Machine Config Server.

- [16.1. Understand TLS security profiles](16_01_understand_tls_security_profiles.md)
- [16.2. View TLS security profile details](16_02_view_tls_security_profile_details.md)
- [16.3. Configure the TLS security profile for the Ingress Controller](16_03_configure_the_tls_security_profile_for_the_ingress_controller.md)
- [16.4. Configure the TLS security profile for the control plane](16_04_configure_the_tls_security_profile_for_the_control_plane.md)
- [16.5. Configure the TLS security profile for the kubelet](16_05_configure_the_tls_security_profile_for_the_kubelet.md)
