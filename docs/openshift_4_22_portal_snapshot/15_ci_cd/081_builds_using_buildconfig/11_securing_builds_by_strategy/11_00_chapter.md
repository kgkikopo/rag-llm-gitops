# Chapter 11. Securing builds by strategy

Builds in OpenShift Container Platform are run in privileged containers. Depending on the build strategy used, if you have privileges, you can run builds to escalate their permissions on the cluster and host nodes. And as a security measure, it limits who can run builds and the strategy that is used for those builds. Custom builds are inherently less safe than source builds, because they can execute any code within a privileged container, and are disabled by default. Grant docker build permissions with caution, because a vulnerability in the Dockerfile processing logic could result in a privileges being granted on the host node. 

By default, all users that can create builds are granted permission to use the docker and Source-to-image (S2I) build strategies. Users with cluster administrator privileges can enable the custom build strategy, as referenced in the restricting build strategies to a user globally section. 

You can control who can build and which build strategies they can use by using an authorization policy. Each build strategy has a corresponding build subresource. A user must have permission to create a build and permission to create on the build strategy subresource to create builds using that strategy. Default roles are provided that grant the create permission on the build strategy subresource. 

Table 11.1. Build Strategy Subresources and RolesStrategy| Subresource| Role  
---|---|---  
Docker  |  builds/docker  |  system:build-strategy-docker   
Source-to-Image  |  builds/source  |  system:build-strategy-source   
Custom  |  builds/custom  |  system:build-strategy-custom   
JenkinsPipeline  |  builds/jenkinspipeline  |  system:build-strategy-jenkinspipeline   
Show more

- [11.1. Disabling access to a build strategy globally](11_01_disabling_access_to_a_build_strategy_globally.md)
- [11.2. Restricting build strategies to users globally](11_02_restricting_build_strategies_to_users_globally.md)
- [11.3. Restricting build strategies to a user within a project](11_03_restricting_build_strategies_to_a_user_within_a_project.md)
