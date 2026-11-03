# 1.5. Pod operations

Find procedures for reading, managing, and enhancing pods in an OpenShift Container Platform cluster. 

## 1.5.1. Read operations

As an administrator, you can get information about pods in a project through the following tasks: 

  * [List pods associated with a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-viewing-project_nodes-pods-viewing "2.2.1. Viewing pods in a project"), including information such as the number of replicas and restarts, current status, and age. 
  * [View pod usage statistics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-viewing-usage_nodes-pods-viewing "2.2.3. Viewing pod usage statistics") such as CPU, memory, and storage consumption. 



## 1.5.2. Management operations

The following list of tasks provides an overview of how an administrator can manage pods in an OpenShift Container Platform cluster. 

  * Control scheduling of pods using the advanced scheduling features available in OpenShift Container Platform: 

    * Node-to-pod binding rules such as [pod affinity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-pod-affinity-example-affinity_nodes-scheduler-pod-affinity "4.3.4.1. Pod Affinity"), [node affinity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-node-affinity "4.4. Controlling pod placement on nodes using node affinity rules"), and [anti-affinity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-pod-anti-affinity-configuring_nodes-scheduler-pod-affinity "4.3.3. Configure a pod anti-affinity rule"). 
    * [Node labels and selectors](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-node-selectors "4.7. Placing pods on specific nodes using node selectors"). 
    * [Taints and tolerations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-taints-tolerations "4.6. Controlling pod placement using node taints"). 
    * [Pod topology spread constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-scheduler-pod-topology-spread-constraints "4.8. Controlling pod placement by using pod topology spread constraints"). 
    * [Secondary scheduling](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-secondary-scheduler-about "4.10.1. Secondary scheduler overview"). 

  * [Configure the descheduler to evict pods](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/controlling-pod-placement-onto-nodes-scheduling#nodes-descheduler-about "4.9.1. Descheduler overview") based on specific strategies so that the scheduler reschedules the pods to more appropriate nodes. 
  * [Configure how pods behave after a restart using pod controllers and restart policies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-configuring-restart_nodes-pods-configuring "2.3.1. Configure how pods behave after restart"). 
  * [Limit both egress and ingress traffic on a pod](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-configuring-bandwidth_nodes-pods-configuring "2.3.2. Limit the bandwidth available to pods"). 
  * [Add and remove volumes to and from any object that has a pod template](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-containers#nodes-containers-volumes "7.3. Using volumes to persist container data"). A volume is a mounted file system available to all the containers in a pod. Container storage is ephemeral; you can use volumes to persist container data. 



## 1.5.3. Enhancement operations

You can work with pods more easily and efficiently with the help of various tools and features available in OpenShift Container Platform. The following operations involve using those tools and features to better manage pods. 

Operation| User| More information  
---|---|---  
Create and use a horizontal pod autoscaler.  |  Developer  |  You can use a horizontal pod autoscaler to specify the minimum and the maximum number of pods you want to run, as well as the CPU utilization or memory utilization your pods should target. Using a horizontal pod autoscaler, you can [automatically scale pods](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-autoscaling "2.4. Automatically scaling pods with the horizontal pod autoscaler").   
[Install and use a vertical pod autoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-vpa "2.5. Automatically adjust pod resource levels with the vertical pod autoscaler").  |  Administrator and developer  |  As an administrator, use a vertical pod autoscaler to better use cluster resources by monitoring the resources and the resource requirements of workloads.  As a developer, use a vertical pod autoscaler to ensure your pods stay up during periods of high demand by scheduling pods to nodes that have enough resources for each pod.   
Provide access to external resources using device plugins.  |  Administrator  |  A [device plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-device "2.12. Using device plugins to access external resources with pods") is a gRPC service running on nodes (external to the kubelet), which manages specific hardware resources. You can [deploy a device plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#methods-for-deploying-a-device-plugin_nodes-pods-device "2.12.1.2. Methods for deploying a device plugin") to provide a consistent and portable solution to consume hardware devices across clusters.   
Provide sensitive data to pods [using the `Secret` object](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-secrets "2.7. Providing sensitive data to pods by using secrets").  |  Administrator  |  Some applications need sensitive information, such as passwords and usernames. You can use the `Secret` object to provide such information to an application pod.   
Show more
