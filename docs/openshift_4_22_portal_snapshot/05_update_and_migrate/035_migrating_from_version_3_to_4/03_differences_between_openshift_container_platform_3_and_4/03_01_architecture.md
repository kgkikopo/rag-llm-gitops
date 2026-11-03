# 3.1. Architecture

With OpenShift Container Platform 3, administrators individually deployed Red Hat Enterprise Linux (RHEL) hosts, and then installed OpenShift Container Platform on top of these hosts to form a cluster. Administrators were responsible for properly configuring these hosts and performing updates. 

OpenShift Container Platform 4 represents a significant change in the way that OpenShift Container Platform clusters are deployed and managed. OpenShift Container Platform 4 includes new technologies and functionality, such as Operators, machine sets, and Red Hat Enterprise Linux CoreOS (RHCOS), which are core to the operation of the cluster. This technology shift enables clusters to self-manage some functions previously performed by administrators. This also ensures platform stability and consistency, and simplifies installation and scaling. 

Beginning with OpenShift Container Platform 4.13, RHCOS now uses Red Hat Enterprise Linux (RHEL) 9.2 packages. This enhancement enables the latest fixes and features as well as the latest hardware support and driver updates. For more information about how this upgrade to RHEL 9.2 might affect your options configuration and services as well as driver and container support, see the [RHCOS now uses RHEL 9.2](https://docs.openshift.com/container-platform/4.13/release_notes/ocp-4-13-release-notes.html#ocp-4-13-rhel-9-considerations) in the _OpenShift Container Platform 4.13 release notes_. 

For more information, see [OpenShift Container Platform architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture). 

## 3.1.1. Immutable infrastructure

OpenShift Container Platform 4 uses Red Hat Enterprise Linux CoreOS (RHCOS), which is designed to run containerized applications, and provides efficient installation, Operator-based management, and simplified upgrades. RHCOS is an immutable container host, rather than a customizable operating system like RHEL. RHCOS enables OpenShift Container Platform 4 to manage and automate the deployment of the underlying container host. RHCOS is a part of OpenShift Container Platform, which means that everything runs inside a container and is deployed using OpenShift Container Platform. 

In OpenShift Container Platform 4, control plane nodes must run RHCOS, ensuring that full-stack automation is maintained for the control plane. This makes rolling out updates and upgrades a much easier process than in OpenShift Container Platform 3. 

For more information, see [Red Hat Enterprise Linux CoreOS (RHCOS)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-rhcos). 

## 3.1.2. Operators

Operators are a method of packaging, deploying, and managing a Kubernetes application. Operators ease the operational complexity of running another piece of software. They watch over your environment and use the current state to make decisions in real time. Advanced Operators are designed to upgrade and react to failures automatically. 

For more information, see [Understanding Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-what-operators-are).
