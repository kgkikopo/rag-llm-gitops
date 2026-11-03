# 1.3. Install managed clusters with ClusterInstance resources and RHACM

GitOps Zero Touch Provisioning (ZTP) uses `ClusterInstance` custom resources (CRs) in a Git repository to manage the installation of OpenShift Container Platform clusters. The `ClusterInstance` CR contains cluster-specific parameters and options for applying configuration CRs during installation. 

The GitOps ZTP plugin processes `ClusterInstance` CRs to generate a collection of CRs on the hub cluster. This triggers the assisted service in Red Hat Advanced Cluster Management (RHACM) to install OpenShift Container Platform on the bare-metal host. You can find installation status and error messages in these CRs on the hub cluster. You can provision single clusters manually or in batches with GitOps ZTP: 

Provisioning a single cluster
     Create a single `ClusterInstance` CR and related configuration CRs for the cluster, and apply them in the hub cluster to begin cluster provisioning. This is a good way to test your CRs before deploying on a larger scale. 
Provisioning many clusters
     Install managed clusters in batches of up to 500 by defining `ClusterInstance` and related CRs in a Git repository. ArgoCD uses the `ClusterInstance` CRs to deploy the clusters. The RHACM policy generator creates the manifests and applies them to the hub cluster. This starts the cluster provisioning process.
