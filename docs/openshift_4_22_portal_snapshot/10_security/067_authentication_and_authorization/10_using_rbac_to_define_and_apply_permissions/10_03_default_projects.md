# 10.3. Default projects

Default projects host critical cluster and infrastructure components. By understanding their purpose, you can avoid making changes that could disrupt essential cluster services. 

OpenShift Container Platform includes several default projects, and projects starting with `openshift-` are the most essential to users. These projects host master components that run as pods and other infrastructure components. The pods created in these namespaces that have a critical pod annotation are considered critical, and they have guaranteed admission by kubelet. Pods created for master components in these namespaces are already marked as critical. 

Important

Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components. 

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects. 

**Additional resources**

  * [Guaranteed Scheduling For Critical Add-On Pods (Kubernetes documentation)](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#rescheduler-guaranteed-scheduling-of-critical-add-ons)
