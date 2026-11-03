# 1.2. Components that manage SR-IOV network devices

The SR-IOV Network Operator creates and manages the components of the SR-IOV stack. The Operator performs the following functions: 

  * Orchestrates discovery and management of SR-IOV network devices 
  * Generates `NetworkAttachmentDefinition` custom resources for the SR-IOV Container Network Interface (CNI) 
  * Creates and updates the configuration of the SR-IOV network device plugin 
  * Creates node specific `SriovNetworkNodeState` custom resources 
  * Updates the `spec.interfaces` field in each `SriovNetworkNodeState` custom resource 



The Operator provisions the following components: 

SR-IOV network configuration daemon
     A daemon set that is deployed on worker nodes when the SR-IOV Network Operator starts. The daemon is responsible for discovering and initializing SR-IOV network devices in the cluster. 
SR-IOV Network Operator webhook
     A dynamic admission controller webhook that validates the Operator custom resource and sets appropriate default values for unset fields. 
SR-IOV Network resources injector
     A dynamic admission controller webhook that provides functionality for patching Kubernetes pod specifications with requests and limits for custom network resources such as SR-IOV VFs. The SR-IOV network resources injector adds the `resource` field to only the first container in a pod automatically. 
SR-IOV network device plugin
     A device plugin that discovers, advertises, and allocates SR-IOV network virtual function (VF) resources. Device plugins are used in Kubernetes to enable the use of limited resources, typically in physical devices. Device plugins give the Kubernetes scheduler awareness of resource availability, so that the scheduler can schedule pods on nodes with sufficient resources. 
SR-IOV CNI plugin
     A CNI plugin that attaches VF interfaces allocated from the SR-IOV network device plugin directly into a pod. 
SR-IOV InfiniBand CNI plugin
     A CNI plugin that attaches InfiniBand (IB) VF interfaces allocated from the SR-IOV network device plugin directly into a pod. 

Note

The SR-IOV Network resources injector and SR-IOV Network Operator webhook are enabled by default and can be disabled by editing the `default` `SriovOperatorConfig` CR. Use caution when disabling the SR-IOV Network Operator Admission Controller webhook. You can disable the webhook under specific circumstances, such as troubleshooting, or if you want to use unsupported devices.
