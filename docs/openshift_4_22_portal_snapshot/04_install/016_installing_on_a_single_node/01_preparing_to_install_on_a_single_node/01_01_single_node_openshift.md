# 1.1. Single-node OpenShift

You can create a single-node cluster with standard installation methods. OpenShift Container Platform on a single node is a specialized installation that requires the creation of a special Ignition configuration file. 

Important

After cluster installation, no configuration option exists to change a single-node cluster to a high availability (HA) cluster or a two-node cluster. The architecture topology you choose at installation time sets the architecture topology for the lifecycle of the cluster. 

The primary use case is for edge computing workloads, including intermittent connectivity, portable clouds, and 5G radio access networks (RAN) close to a base station. The major tradeoff with an installation on a single node is the lack of high availability. 

Important

The use of OpenShiftSDN with single-node OpenShift is not supported. OVN-Kubernetes is the default network plugin for single-node OpenShift deployments.
