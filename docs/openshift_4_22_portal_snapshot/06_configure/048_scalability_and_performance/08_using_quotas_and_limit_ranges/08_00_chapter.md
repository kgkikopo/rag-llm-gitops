# Chapter 8. Using quotas and limit ranges

As a cluster administrator, you can use quotas and limit ranges to set constraints. These constraints limit the number of objects or the amount of compute resources that are used in your project. 

By using quotes and limits, you can better manage and allocate resources across all projects. You can also ensure that no projects use more resources than is appropriate for the cluster size. 

A resource quota, defined by a `ResourceQuota` object, provides constraints that limit aggregate resource consumption per project. The quota can limit the quantity of objects that can be created in a project by type. Additionally, the quota can limit the total amount of compute resources and storage that might be consumed by resources in that project. 

Important

Quotas are set by cluster administrators and are scoped to a given project. OpenShift Container Platform project owners can change quotas for their project, but not limit ranges. OpenShift Container Platform users cannot modify quotas or limit ranges.

- [8.1. Resources managed by quota](08_01_resources_managed_by_quota.md)
- [8.2. Setting resource quota for extended resources](08_02_setting_resource_quota_for_extended_resources.md)
- [8.3. Quota scopes](08_03_quota_scopes.md)
- [8.4. Additional resources](08_04_additional_resources.md)
- [8.5. Admin quota usage](08_05_admin_quota_usage.md)
- [8.6. Additional resources](08_06_additional_resources.md)
- [8.7. Limit ranges in a LimitRange object](08_07_limit_ranges_in_a_limitrange_object.md)
- [8.8. Additional resources](08_08_additional_resources.md)
- [8.9. Limit range operations](08_09_limit_range_operations.md)
- [8.10. Additional resources](08_10_additional_resources.md)
