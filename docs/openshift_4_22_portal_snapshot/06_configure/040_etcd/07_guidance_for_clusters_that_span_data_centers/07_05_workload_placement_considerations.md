# 7.5. Workload placement considerations

Place critical workloads across sites in a multisite cluster so you avoid single points of failure during a data center outage. 

With multisite clusters, administrators and developers must take special considerations into account to ensure that critical workloads are scheduled or placed based on the proper hardware or hosts within the topology of the cluster. This planning ensures that the applications and services are highly available and fault-tolerant based on the topology of the cluster deployment. 

Without this planning, OpenShift Container Platform might schedule workloads on hosts within the cluster so that a single point of failure (SPoF) exists for OpenShift Container Platform infrastructure services and other application services if a data center outage occurs.
