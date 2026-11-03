# 4.4. FIPS validation in OpenShift Container Platform

OpenShift Container Platform uses certain FIPS validated or Modules In Process modules within RHEL and RHCOS for the operating system components that it uses. 

For more information, see "RHEL core crypto components" in the _Additional resources_ section. For example, when users use SSH to connect to OpenShift Container Platform clusters and containers, those connections are properly encrypted. 

OpenShift Container Platform components are written in Go and built with Red Hat’s golang compiler. When you enable FIPS mode for your cluster, all OpenShift Container Platform components that require cryptographic signing call RHEL and RHCOS cryptographic libraries. 

Table 4.1. FIPS mode attributes and limitations in OpenShift Container Platform 4.22Attributes| Limitations  
---|---  
FIPS support in RHEL 9 and RHCOS operating systems.  |  The FIPS implementation does not use a function that performs hash computation and signature generation or validation in a single step. This limitation will continue to be evaluated and improved in future OpenShift Container Platform releases.   
FIPS support in CRI-O runtimes.   
FIPS support in OpenShift Container Platform services.   
FIPS validated or Modules In Process cryptographic module and algorithms that are obtained from RHEL 9 and RHCOS binaries and images.   
Use of FIPS compatible golang compiler.  |  TLS FIPS support is not complete but is planned for future OpenShift Container Platform releases.   
FIPS support across multiple architectures.  |  FIPS is currently only supported on OpenShift Container Platform deployments using `x86_64`, `ppc64le`, and `s390x` architectures.   
Show more

**Additional resources**

  * [RHEL core crypto components](https://access.redhat.com/articles/3655361)
