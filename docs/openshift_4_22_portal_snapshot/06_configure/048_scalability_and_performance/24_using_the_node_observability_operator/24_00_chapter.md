# Chapter 24. Using the Node Observability Operator

The Node Observability Operator collects and stores CRI-O and Kubelet profiling or metrics from scripts of compute nodes. 

With the Node Observability Operator, you can query the profiling data, enabling analysis of performance trends in CRI-O and Kubelet. It supports debugging performance-related issues and executing embedded scripts for network metrics by using the `run` field in the custom resource definition. To enable CRI-O and Kubelet profiling or scripting, you can configure the `type` field in the custom resource definition. 

Important

The Node Observability Operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

- [24.1. Workflow of the Node Observability Operator](24_01_workflow_of_the_node_observability_operator.md)
- [24.2. Installing the Node Observability Operator](24_02_installing_the_node_observability_operator.md)
- [24.3. Requesting CRI-O and Kubelet profiling data using the Node Observability Operator](24_03_requesting_cri_o_and_kubelet_profiling_data_using_the_node_observability_operator.md)
- [24.4. Node Observability Operator scripting](24_04_node_observability_operator_scripting.md)
- [24.5. Additional resources](24_05_additional_resources.md)
