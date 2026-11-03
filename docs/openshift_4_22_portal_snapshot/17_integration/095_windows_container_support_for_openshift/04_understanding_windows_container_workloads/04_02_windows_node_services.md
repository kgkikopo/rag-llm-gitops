# 4.2. Windows node services

By default, the installation process installs several Windows-specific services on each Windows node. 

Service| Description  
---|---  
kubelet  |  Registers the Windows node and manages its status.   
Container Network Interface (CNI) plugins  |  Exposes [networking](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#networking) for Windows nodes.   
Windows Instance Config Daemon (WICD)  |  Maintains the state of all services running on the Windows instance to ensure the instance functions as a worker node.   
[Windows Exporter](https://github.com/openshift/prometheus-community-windows_exporter) |  Exports Prometheus metrics from Windows nodes   
[Kubernetes Cloud Controller Manager (CCM)](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) |  Interacts with the underlying Azure cloud platform.   
hybrid-overlay  |  Creates the OpenShift Container Platform [Host Network Service (HNS)](https://docs.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture#container-network-management-with-host-network-service).   
kube-proxy  |  Maintains network rules on nodes allowing outside communication.   
containerd container runtime  |  Manages the complete container lifecycle.   
CSI Proxy  |  Enables CSI drivers to perform storage operations on the node, which allows containerized CSI drivers to run on Windows nodes.   
Show more
