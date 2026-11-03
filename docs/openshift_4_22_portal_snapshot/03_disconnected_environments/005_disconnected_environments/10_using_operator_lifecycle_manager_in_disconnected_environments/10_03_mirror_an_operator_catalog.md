# 10.3. Mirror an Operator catalog

For instructions about mirroring Operator catalogs for use with disconnected clusters, see "Mirroring Operator catalogs for use with disconnected clusters". 

Important

As of OpenShift Container Platform 4.11, the default Red Hat-provided Operator catalog releases in the file-based catalog format. The default Red Hat-provided Operator catalogs for OpenShift Container Platform 4.6 through 4.10 released in the deprecated SQLite database format. 

The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format. 

Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format. For more information about working with file-based catalogs, see "Operator Framework packaging format", "Managing custom catalogs", and "Mirroring images for a disconnected installation by using the oc-mirror plugin v2". 

**Additional resources**

  * [Mirroring Operator catalogs for use with disconnected clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-installation-images#olm-mirror-catalog_installing-mirroring-installation-images "8.7. Mirror Operator catalogs for use with disconnected clusters")
  * [Operator Framework packaging format](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-file-based-catalogs_olm-packaging-format)
  * [Managing custom catalogs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-managing-custom-catalogs-fb)
  * [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/about-installing-oc-mirror-v2 "Chapter 5. Mirroring images for a disconnected installation by using the oc-mirror plugin v2")
