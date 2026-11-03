# 9.1. Manage CPU overcommitment

Manage CPU overcommitment to optimize infrastructure sizing in a virtualized IBM Z environment. This strategy allocates more resources to virtual machines than are physically available, but requires careful workload planning. 

Depending on your setup, consider the following best practices regarding CPU overcommitment: 

  * Avoid over-allocating physical cores, Integrated Facilities for Linux (IFLs), at the Logical Partition (LPAR) level (PR/SM hypervisor). If your system has 4 physical IFLs, do not configure multiple LPARs with 4 logical IFLs each. 
  * Check and understand LPAR shares and weights. 
  * An excessive number of virtual CPUs can adversely affect performance. Do not define more virtual processors to a guest than logical processors are defined to the LPAR. 
  * Configure the number of virtual processors per guest for peak workload. 
  * Start small and monitor the workload. If required, increase the vCPU number incrementally. 
  * Not all workloads are suitable for high overcommitment ratios. If the workload is CPU intensive, you might experience performance problems with high overcommitment ratios. Workloads that are more I/O intensive can keep consistent performance even with high overcommitment ratios. 



**Additional resources**

  * [z/VM Common Performance Problems and Solutions](https://www.vm.ibm.com/perf/tips/prgcom.html)
  * [z/VM overcommitment considerations](https://www.ibm.com/docs/en/linux-on-systems?topic=overcommitment-considerations)
  * [LPAR CPU management](https://www.ibm.com/docs/en/zos/2.2.0?topic=director-lpar-cpu-management)
