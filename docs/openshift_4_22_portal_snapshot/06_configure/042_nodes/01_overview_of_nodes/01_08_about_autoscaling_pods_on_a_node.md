# 1.8. About autoscaling pods on a node

OpenShift Container Platform offers three tools that you can use to automatically scale the number of pods on your nodes and the resources allocated to pods. 

Horizontal Pod Autoscaler
     The Horizontal Pod Autoscaler (HPA) can automatically increase or decrease the scale of a replication controller or deployment, based on metrics collected from the pods that belong to that replication controller or deployment. 
Custom Metrics Autoscaler
     The Custom Metrics Autoscaler can automatically increase or decrease the number of pods for a deployment, stateful set, custom resource, or job based on custom metrics that are not based only on CPU or memory. 
Vertical Pod Autoscaler
     The Vertical Pod Autoscaler (VPA) can automatically review the historic and current CPU and memory resources for containers in pods and can update the resource limits and requests based on the usage values it learns. 

**Additional resources**

  * [Automatically scaling pods with the horizontal pod autoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-autoscaling "2.4. Automatically scaling pods with the horizontal pod autoscaler")
  * [Custom Metrics Autoscaler Operator overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator#nodes-cma-autoscaling-custom "3.2. Custom Metrics Autoscaler Operator overview")
  * [Automatically adjust pod resource levels with the vertical pod autoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#nodes-pods-vpa "2.5. Automatically adjust pod resource levels with the vertical pod autoscaler")
