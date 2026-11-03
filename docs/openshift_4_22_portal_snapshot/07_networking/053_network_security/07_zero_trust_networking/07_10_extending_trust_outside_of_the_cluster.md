# 7.10. Extending trust outside of the cluster

You might want to extend trust outside of the cluster by allowing a cluster to mint CAs for a subdomain. Alternatively, you might want to attest to workload identity in the cluster to a remote endpoint. 

Leverage: 

  * [OpenShift cert-manager Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#cert-manager-operator-about): You can use cert-manager to manage delegated CAs so that you can distribute trust across different clusters, or through your organization. 
  * [Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-about): Can use SPIFFE to provide remote attestation of workloads to endpoints running in remote or local clusters.
