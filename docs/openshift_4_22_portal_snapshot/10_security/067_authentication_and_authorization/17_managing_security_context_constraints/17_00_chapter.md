# Chapter 17. Managing security context constraints

In OpenShift Container Platform, you can use security context constraints (SCCs) to control permissions for the pods in your cluster. 

Default SCCs are created during installation and when you install some Operators or other components. As a cluster administrator, you can also create your own SCCs by using the OpenShift CLI (`oc`). 

Important

Do not modify the default SCCs. Customizing the default SCCs can lead to issues when some of the platform pods deploy or OpenShift Container Platform is upgraded. Additionally, the default SCC values are reset to the defaults during some cluster upgrades, which discards all customizations to those SCCs. 

Instead of modifying the default SCCs, create and modify your own SCCs as needed. For detailed steps, see [Creating security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-pod-security-policies#security-context-constraints-creating_configuring-internal-oauth "17.4. Create security context constraints").

- [17.1. About security context constraints](17_01_about_security_context_constraints.md)
- [17.2. About pre-allocated security context constraints values](17_02_about_pre_allocated_security_context_constraints_values.md)
- [17.3. Example security context constraints](17_03_example_security_context_constraints.md)
- [17.4. Create security context constraints](17_04_create_security_context_constraints.md)
- [17.5. Configure a workload to require a specific SCC](17_05_configure_a_workload_to_require_a_specific_scc.md)
- [17.6. Role-based access to security context constraints](17_06_role_based_access_to_security_context_constraints.md)
- [17.7. Reference of security context constraints commands](17_07_reference_of_security_context_constraints_commands.md)
- [17.8. Additional resources](17_08_additional_resources.md)
