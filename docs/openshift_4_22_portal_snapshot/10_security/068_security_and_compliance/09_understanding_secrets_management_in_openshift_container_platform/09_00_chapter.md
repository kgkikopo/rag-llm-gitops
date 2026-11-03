# Chapter 9. Understanding secrets management in OpenShift Container Platform

Secret management tools can be used to automate the lifecycle of sensitive data, such as passwords, private files, and certificates, by providing a centralized system to control and monitor access. This approach enhances security by limiting the uncontrolled spread of secrets and enables automation for the entire secret lifecycle, including updates, expiration, and removal. 

OpenShift Container Platform uses a flexible Operator and plugin design to decouple your workloads from external secret managers, ensuring you are not locked into a single vendor. In this model, the Operator acts as an intermediary, while a vendor-specific plugin manages communication between the cluster and the external storage. This allows applications to access secrets without needing to know the details of where or how they are stored.

- [9.1. Secrets management Operators in OpenShift Container Platform](09_01_secrets_management_operators_in_openshift_container_platform.md)
- [9.2. Secrets management use cases](09_02_secrets_management_use_cases.md)
