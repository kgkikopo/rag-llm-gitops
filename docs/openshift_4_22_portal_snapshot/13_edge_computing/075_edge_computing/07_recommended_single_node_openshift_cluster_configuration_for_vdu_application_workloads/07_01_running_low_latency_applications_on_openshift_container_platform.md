# 7.1. Running low latency applications on OpenShift Container Platform

OpenShift Container Platform enables low latency processing for applications running on commercial off-the-shelf (COTS) hardware by using several technologies and specialized hardware devices: 

Real-time kernel for RHCOS
     Ensures workloads are handled with a high degree of process determinism. 
CPU isolation
     Avoids CPU scheduling delays and ensures CPU capacity is available consistently. 
NUMA-aware topology management
     Aligns memory and huge pages with CPU and PCI devices to pin guaranteed container memory and huge pages to the non-uniform memory access (NUMA) node. Pod resources for all Quality of Service (QoS) classes stay on the same NUMA node. This decreases latency and improves performance of the node. 
Huge pages memory management
     Using huge page sizes improves system performance by reducing the amount of system resources required to access page tables. 
Precision timing synchronization using PTP
     Allows synchronization between nodes in the network with sub-microsecond accuracy.
