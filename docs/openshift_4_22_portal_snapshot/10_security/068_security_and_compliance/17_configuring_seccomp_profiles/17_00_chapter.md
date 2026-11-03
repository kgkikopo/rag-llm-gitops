# Chapter 17. Configuring seccomp profiles

An OpenShift Container Platform container or a pod runs a single application that performs one or more well-defined tasks. The application usually requires only a small subset of the underlying operating system kernel APIs. Secure computing mode, seccomp, is a Linux kernel feature that can be used to limit the process running in a container to only using a subset of the available system calls. 

The `restricted-v2` SCC applies to all newly created pods in 4.22. The default seccomp profile `runtime/default` is applied to these pods. 

Seccomp profiles are stored as JSON files on the disk. 

Important

Seccomp profiles cannot be applied to privileged containers.

- [17.1. Verify the default seccomp profile applied to a pod](17_01_verify_the_default_seccomp_profile_applied_to_a_pod.md)
- [17.2. Configuring a custom seccomp profile](17_02_configuring_a_custom_seccomp_profile.md)
- [17.3. Additional resources](17_03_additional_resources.md)
