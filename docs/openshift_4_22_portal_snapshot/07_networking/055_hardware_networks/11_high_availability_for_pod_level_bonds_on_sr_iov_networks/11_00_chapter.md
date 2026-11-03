# Chapter 11. High availability for pod-level bonds on SR-IOV networks

For workloads by using pod-level bonding with SR-IOV virtual functions (VFs), despite an upstream switch failure, an underlying physical function (PF) might still report an `up` state. This creates a silent failure, as attached VFs remain up and pods continue to send traffic to a dead endpoint, causing packet loss. 

The PF Status Relay Operator solves this issue by using Link Aggregation Control Protocol (LACP) as an active health check. In this configuration, each physical function (PF) is in its own single-member LACP bond with the upstream switch. When the Operator detects an LACP failure on a PF bond, it changes the link state of the attached VFs from `auto` to `disabled`. This action triggers the pod’s `active-backup` bond to fail over to its backup network path, maintaining high availability. 

Important

Configuring LACP state monitoring for SR-IOV networks is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

- [11.1. Install the PF Status Relay Operator using the CLI](11_01_install_the_pf_status_relay_operator_using_the_cli.md)
- [11.2. Installing the PF Status Relay Operator using the web console](11_02_installing_the_pf_status_relay_operator_using_the_web_console.md)
- [11.3. Configure the PF Status Relay Operator for LACP state monitoring on SR-IOV networks](11_03_configure_the_pf_status_relay_operator_for_lacp_state_monitoring_on_sr_iov_networks.md)
