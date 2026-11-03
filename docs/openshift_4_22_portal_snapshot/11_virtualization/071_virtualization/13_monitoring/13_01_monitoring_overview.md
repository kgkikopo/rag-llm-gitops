# 13.1. Monitoring overview

Monitor the health of your cluster and virtual machines (VMs) to have a unified operational view of your environment. This ensures high availability and optimal resource performance. 

You can monitor the health of your cluster and VMs with the following tools: 

Monitoring OpenShift Virtualization VM health status
     View the overall health of your OpenShift Virtualization environment in the web console by navigating to the **Home** **Overview** page in the OpenShift Container Platform web console. The **Status** card displays the overall health of OpenShift Virtualization based on the alerts and conditions. 
[OpenShift Container Platform cluster checkup framework](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-running-cluster-checkups "13.2. OpenShift Virtualization cluster checkup framework")
     Run automated tests with the OpenShift Container Platform cluster checkup framework to ensure that your cluster, including cluster storage, is optimally configured for OpenShift Virtualization. 
[Prometheus queries for virtual resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-prometheus-queries "13.4. Prometheus queries for virtual resources")
     Query vCPU, network, storage, and guest memory swapping usage and live migration progress. 
[VM custom metrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-exposing-custom-metrics-for-vms "13.5. Exposing custom metrics for virtual machines")
     Configure the `node-exporter` service to expose internal VM metrics and processes. 
[VM health checks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-monitoring-vm-health "13.7. Virtual machine health checks")
     Configure readiness, liveness, and guest agent ping probes and a watchdog for VMs. 
[Runbooks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-runbooks "13.8. OpenShift Virtualization runbooks")
     Diagnose and resolve issues that trigger OpenShift Virtualization [alerts](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/monitoring_key_concepts/key-concepts#about-managing-alerts_key-concepts) in the OpenShift Container Platform web console.
