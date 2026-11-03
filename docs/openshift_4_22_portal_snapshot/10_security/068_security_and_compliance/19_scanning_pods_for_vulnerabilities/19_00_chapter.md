# Chapter 19. Scanning pods for vulnerabilities

Important

The Red Hat Quay Container Security Operator has been deprecated and is planned for removal in a future release of OpenShift Container Platform. The official replacement product of the Red Hat Quay Container Security Operator is Red Hat Advanced Cluster Security for Kubernetes. 

Using the Red Hat Quay Container Security Operator, you can access vulnerability scan results from the OpenShift Container Platform web console for container images used in active pods on the cluster. 

The Red Hat Quay Container Security Operator: 

  * Watches containers associated with pods on all or specified namespaces 
  * Queries the container registry where the containers came from for vulnerability information, provided an image’s registry is running image scanning (such as [Quay.io](https://quay.io) or a [Red Hat Quay](https://access.redhat.com/products/red-hat-quay) registry with Clair scanning) 
  * Exposes vulnerabilities via the `ImageManifestVuln` object in the Kubernetes API 



Using the instructions here, the Red Hat Quay Container Security Operator is installed in the `openshift-operators` namespace, so it is available to all namespaces on your OpenShift Container Platform cluster.

- [19.1. Install the Red Hat Quay Container Security Operator](19_01_install_the_red_hat_quay_container_security_operator.md)
- [19.2. Use the Red Hat Quay Container Security Operator](19_02_use_the_red_hat_quay_container_security_operator.md)
- [19.3. Query image vulnerabilities from the CLI](19_03_query_image_vulnerabilities_from_the_cli.md)
- [19.4. Uninstall the Red Hat Quay Container Security Operator](19_04_uninstall_the_red_hat_quay_container_security_operator.md)
- [19.5. Additional resources](19_05_additional_resources.md)
