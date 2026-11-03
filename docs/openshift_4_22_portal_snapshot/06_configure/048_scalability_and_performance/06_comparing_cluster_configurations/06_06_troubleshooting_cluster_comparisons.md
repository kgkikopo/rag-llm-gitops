# 6.6. Troubleshooting cluster comparisons

When using the `cluster-compare` plugin, you might see unexpected results, such as false positives or conflicts when multiple cluster custom resources (CRs) exist. 

## 6.6.1. Troubleshooting false positives for missing resources

The plugin might report a missing resource even though the cluster custom resource (CR) is present in the cluster. 

**Procedure**

  1. Ensure you are using the latest version of the `cluster-compare` plugin. For more information, see "Installing the cluster-compare plugin". 
  2. Ensure you are using the most up-to-date version of the reference configuration. 
  3. Ensure that template has the same `apiVersion`, `kind`, `name`, and `namespace` fields as the cluster CR. 



## 6.6.2. Troubleshooting multiple template matches for the same CR

In some cases, more than one cluster CR can match a template because they feature the same `apiVersion`, `namespace`, and `kind`. The plugin’s default matching compares the CR that features the least differences. 

You can optionally configure your reference configuration to avoid this situation. 

**Procedure**

  1. Ensure the templates feature distinct `apiVersion`, `namespace`, and `kind` values to ensure no duplicate template matching. 
  2. Use a user configuration file to manually match a template to a CR. For more information, see "Configuring manual matching between CRs and templates". 



## 6.6.3. Additional resources

  * [Installing the cluster-compare plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/comparing-cluster-configurations#installing-cluster-compare_installing-cluster-compare-plugin "6.2.1. Installing the cluster-compare plugin")
  * [Configuring manual matching between CRs and templates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/comparing-cluster-configurations#cluster-compare-manual-match_advanced-ref-config-customization "6.5.1. Configuring manual matching between CRs and templates")
