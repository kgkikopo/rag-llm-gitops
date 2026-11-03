# Chapter 2. Configuring the node port service range

To meet your cluster node port requirements in OpenShift Container Platform, you can configure the node port service range during installation or expand it after installation. You can expand the default range of `30000-32768` on either side while preserving this default range within your new configuration. 

Important

Red Hat has not performed testing outside the default port range of `30000-32768`. For ranges outside the default port range, ensure that you test to verify the expanding node port range does not impact your cluster. In particular, ensure that there is: 

  * No overlap with any ports already in use by host processes 
  * No overlap with any ports already in use by pods that are configured with host networking 



If you expanded the range and a port allocation issue occurs, create a new cluster and set the required range for it. 

If you expand the node port range and OpenShift CLI (`oc`) stops working because of a port conflict with the OpenShift Container Platform API server, you must create a new cluster.

- [2.1. Expand the node port range](02_01_expand_the_node_port_range.md)
- [2.2. Additional resources](02_02_additional_resources.md)
