# Chapter 1. Understanding API tiers

Important

This guidance does not cover layered OpenShift Container Platform offerings. 

API tiers for bare-metal configurations also apply to virtualized configurations except for any feature that directly interacts with hardware. Those features directly related to hardware have no application operating environment (AOE) compatibility level beyond that which is provided by the hardware vendor. For example, applications that rely on Graphics Processing Units (GPU) features are subject to the AOE compatibility provided by the GPU vendor driver. 

API tiers in a cloud environment for cloud specific integration points have no API or AOE compatibility level beyond that which is provided by the hosting cloud vendor. For example, APIs that exercise dynamic management of compute, ingress, or storage are dependent upon the underlying API capabilities exposed by the cloud platform. Where a cloud vendor modifies a prerequisite API, Red Hat will provide commercially reasonable efforts to maintain support for the API with the capability presently offered by the cloud infrastructure vendor. 

Red Hat requests that application developers validate that any behavior they depend on is explicitly defined in the formal API documentation to prevent introducing dependencies on unspecified implementation-specific behavior or dependencies on bugs in a particular implementation of an API. For example, new releases of an ingress router may not be compatible with older releases if an application uses an undocumented API or relies on undefined behavior.

- [1.1. API tiers](01_01_api_tiers.md)
- [1.2. Mapping API tiers to API groups](01_02_mapping_api_tiers_to_api_groups.md)
- [1.3. API deprecation policy](01_03_api_deprecation_policy.md)
