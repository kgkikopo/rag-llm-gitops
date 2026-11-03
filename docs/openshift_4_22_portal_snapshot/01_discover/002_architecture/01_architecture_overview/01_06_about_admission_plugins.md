# 1.6. About admission plugins

Admission plugins process resource requests to the control plane API to validate requests and enforce security policies, resource limitations, and configuration requirements. 

You can use admission plugins to regulate how OpenShift Container Platform functions. After a resource request is authenticated and authorized, admission plugins intercept the resource request to the master API to validate resource requests and to ensure that scaling policies are adhered to. Admission plugins are used to enforce security policies, resource limitations, configuration requirements, and other settings.
