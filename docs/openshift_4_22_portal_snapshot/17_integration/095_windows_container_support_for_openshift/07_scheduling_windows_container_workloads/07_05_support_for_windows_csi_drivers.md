# 7.5. Support for Windows CSI drivers

You can use the CSI PROXY plug-in to perform storage operations on the nodes in your cluster. 

Red Hat OpenShift support for Windows Containers installs CSI Proxy, which is a plug-in that enables CSI drivers for performing storage operations, on all Windows nodes in the cluster. For more information, see "CSI Proxy". 

To use persistent storage with Windows workloads, you must deploy a specific Windows CSI driver daemon set, as described in your storage provider’s documentation. By default, the WMCO does not automatically create the Windows CSI driver daemon set. For more information, see the list of production drivers in the Kubernetes CSI Developer Documentation. 

Note

Red Hat does not provide support for the third-party production drivers listed in the Kubernetes CSI Developer Documentation.
