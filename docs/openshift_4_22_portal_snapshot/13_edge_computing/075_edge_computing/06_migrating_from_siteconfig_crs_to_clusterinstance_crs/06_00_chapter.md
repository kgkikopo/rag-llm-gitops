# Chapter 6. Migrating from SiteConfig CRs to ClusterInstance CRs

You can incrementally migrate single-node OpenShift clusters from `SiteConfig` custom resources (CRs) to `ClusterInstance` CRs. During migration, the existing and new pipelines run in parallel, so you can migrate one or more clusters at a time in a controlled and phased manner. 

Important

  * The `SiteConfig` CR is deprecated from OpenShift Container Platform version 4.18 and removed from OpenShift Container Platform 4.21. 
  * The `ClusterInstance` CR is available from Red Hat Advanced Cluster Management (RHACM) version 2.12 or later.

- [6.1. Overview of migrating from SiteConfig CRs to ClusterInstance CRs](06_01_overview_of_migrating_from_siteconfig_crs_to_clusterinstance_crs.md)
- [6.2. Preparing a parallel Argo CD pipeline for ClusterInstance CRs](06_02_preparing_a_parallel_argo_cd_pipeline_for_clusterinstance_crs.md)
- [6.3. Transitioning the active-ocp-version ClusterImageSet](06_03_transitioning_the_active_ocp_version_clusterimageset.md)
- [6.4. Performing the migration from SiteConfig CR to ClusterInstance CR](06_04_performing_the_migration_from_siteconfig_cr_to_clusterinstance_cr.md)
- [6.5. Deleting the Argo CD pipeline post-migration](06_05_deleting_the_argo_cd_pipeline_post_migration.md)
- [6.6. Troubleshooting the migration to ClusterInstance CRs](06_06_troubleshooting_the_migration_to_clusterinstance_crs.md)
