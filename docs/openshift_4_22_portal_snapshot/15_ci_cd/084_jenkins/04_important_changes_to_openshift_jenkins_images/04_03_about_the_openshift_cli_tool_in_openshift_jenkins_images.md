# 4.3. About the OpenShift CLI tool in OpenShift Jenkins images

If your Jenkins pipelines require a **specific** OpenShift CLI (`oc`) version for compatibility or reproducibility, you must explicitly configure the desired client version in the Jenkins pipeline DSL. 

Starting with 4.12, the OpenShift Jenkins container images ship with the **latest available version** of the `oc` CLI tool bundled inside the image, rather than the client version matching the cluster release. 

If your Jenkins pipelines require a **specific** `oc` client version for compatibility or reproducibility, you must explicitly configure the desired client version in the Jenkins pipeline DSL.
