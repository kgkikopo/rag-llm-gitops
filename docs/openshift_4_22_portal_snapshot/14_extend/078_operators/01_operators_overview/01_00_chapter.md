# Chapter 1. Operators overview

Operators are the foundational control plane extensions of OpenShift Container Platform. Operators are the preferred method to package, deploy, and manage services on the control plane, and to support your applications. 

Operators integrate with Kubernetes APIs and CLI tools such as `kubectl` and the OpenShift CLI (`oc`). They provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, and ensuring that applications remain in your specified state. 

Operators are designed specifically for Kubernetes-native applications to implement and automate common Day 1 operations, such as installation and configuration. Operators can also automate Day 2 operations, such as autoscaling up or down and creating backups. All of these activities are directed by a piece of software running on your cluster. 

While both follow similar Operator concepts and goals, Operators in OpenShift Container Platform are managed by two different systems, depending on their purpose: 

Cluster Operators
     Managed by the Cluster Version Operator (CVO) and installed by default to perform cluster functions. 
Optional add-on Operators
     Managed by Operator Lifecycle Manager (OLM) and can be made accessible for users to run in their applications. Also known as _OLM-based Operators_.

- [1.1. OLM-based Operator tasks](01_01_olm_based_operator_tasks.md)
