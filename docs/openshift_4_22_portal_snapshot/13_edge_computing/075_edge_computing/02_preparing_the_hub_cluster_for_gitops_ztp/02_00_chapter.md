# Chapter 2. Preparing the hub cluster for GitOps ZTP

To use RHACM in a disconnected environment, create a mirror registry that mirrors the OpenShift Container Platform release images and Operator Lifecycle Manager (OLM) catalog that contains the required Operator images. OLM manages, installs, and upgrades Operators and their dependencies in the cluster. You can also use a disconnected mirror host to serve the RHCOS ISO and RootFS disk images that are used to provision the bare-metal hosts.

- [2.1. Telco RAN DU 4.22 validated software components](02_01_telco_ran_du_4_22_validated_software_components.md)
- [2.2. Recommended hub cluster specifications and managed cluster limits for GitOps ZTP](02_02_recommended_hub_cluster_specifications_and_managed_cluster_limits_for_gitops_ztp.md)
- [2.3. Install GitOps ZTP in a disconnected environment](02_03_install_gitops_ztp_in_a_disconnected_environment.md)
- [2.4. Add RHCOS ISO and RootFS images to the disconnected mirror host](02_04_add_rhcos_iso_and_rootfs_images_to_the_disconnected_mirror_host.md)
- [2.5. Enable the assisted service](02_05_enable_the_assisted_service.md)
- [2.6. Configure the hub cluster to use a disconnected mirror registry](02_06_configure_the_hub_cluster_to_use_a_disconnected_mirror_registry.md)
- [2.7. Configure the hub cluster to use unauthenticated registries](02_07_configure_the_hub_cluster_to_use_unauthenticated_registries.md)
- [2.8. Configure the hub cluster with ArgoCD](02_08_configure_the_hub_cluster_with_argocd.md)
- [2.9. Prepare the GitOps ZTP site configuration repository](02_09_prepare_the_gitops_ztp_site_configuration_repository.md)
- [2.10. Prepare the GitOps ZTP site configuration repository for version independence](02_10_prepare_the_gitops_ztp_site_configuration_repository_for_version_independence.md)
- [2.11. Configure the hub cluster for backup and restore](02_11_configure_the_hub_cluster_for_backup_and_restore.md)
