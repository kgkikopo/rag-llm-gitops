# 4.5. Telco RAN DU application workloads

Develop RAN DU applications that are subject to the following requirements and limitations. 

Description and limits
    

  * Develop cloud-native network functions (CNFs) that conform to the latest version of [Red Hat best practices for Kubernetes](https://redhat-best-practices-for-k8s.github.io/guide/). 
  * Use SR-IOV for high performance networking. 
  * For information on the decrease in the default maximum open files soft limit for containers, see the OpenShift Container Platform 4.21 release notes. 
  * Use exec probes sparingly and only when no other suitable options are available. 

    * Do not use exec probes if a CNF uses CPU pinning. Use other probe implementations, for example, `httpGet` or `tcpSocket`. 
    * When you need to use exec probes, limit the exec probe frequency and quantity. The maximum number of exec probes must be kept below 10, and frequency must not be set to less than 10 seconds. Exec probes cause much higher CPU usage on management cores compared to other probe types because they require process forking. 

Note

Startup probes require minimal resources during steady-state operation. The limitation on exec probes applies primarily to liveness and readiness probes. 




Note

A test workload that conforms to the dimensions of the reference DU application workload described in this specification can be found at [openshift-kni/du-test-workloads](https://github.com/openshift-kni/du-test-workloads/tree/v1.0).
