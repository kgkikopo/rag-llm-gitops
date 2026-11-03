# 6.1. Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user. 

Note

OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported.
