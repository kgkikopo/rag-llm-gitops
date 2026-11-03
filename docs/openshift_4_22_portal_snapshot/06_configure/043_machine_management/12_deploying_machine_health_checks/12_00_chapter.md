# Chapter 12. Deploying machine health checks

You can configure and deploy a machine health check to automatically repair damaged machines in a machine pool. 

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API. 

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation. 

To view the platform type for your cluster, run the following command: 

```shell-session
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

- [12.1. About machine health checks](12_01_about_machine_health_checks.md)
- [12.2. About the MachineHealthCheck custom resource](12_02_about_the_machinehealthcheck_custom_resource.md)
- [12.3. Creating a machine health check resource](12_03_creating_a_machine_health_check_resource.md)
- [12.4. About power-based remediation of bare metal](12_04_about_power_based_remediation_of_bare_metal.md)
