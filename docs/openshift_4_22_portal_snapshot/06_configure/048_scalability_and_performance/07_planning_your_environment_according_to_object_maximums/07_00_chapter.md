# Chapter 7. Planning your environment according to object maximums

To ensure your cluster meets performance and scalability requirements, plan your environment according to tested object maximums. By reviewing these limits, you can design a OpenShift Container Platform deployment that operates reliably within supported boundaries. 

The example guidelines are based on the largest possible cluster. For smaller clusters, the maximums are lower. There are many factors that influence the stated thresholds, including the etcd version or storage data format. In most cases, exceeding these numbers results in lower overall performance but might not cause your cluster to fail. 

Warning

Clusters that experience rapid change, such as those with many starting and stopping pods, can have a lower practical maximum size than documented.

- [7.1. OpenShift Container Platform tested cluster maximums for major releases](07_01_openshift_container_platform_tested_cluster_maximums_for_major_releases.md)
- [7.2. OpenShift Container Platform environment and configuration on which the cluster maximums are tested](07_02_openshift_container_platform_environment_and_configuration_on_which_the_cluster_maximums_are_tested.md)
- [7.3. How to plan your environment according to tested cluster maximums](07_03_how_to_plan_your_environment_according_to_tested_cluster_maximums.md)
- [7.4. How to plan your environment according to application requirements](07_04_how_to_plan_your_environment_according_to_application_requirements.md)
