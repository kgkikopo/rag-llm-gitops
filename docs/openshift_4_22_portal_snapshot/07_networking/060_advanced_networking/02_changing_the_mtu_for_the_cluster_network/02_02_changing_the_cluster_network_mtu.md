# 2.2. Changing the cluster network MTU

As a cluster administrator, you can increase or decrease the maximum transmission unit (MTU) for your cluster. 

Important

You cannot roll back an MTU value for nodes during the MTU migration process, but you can roll back the value after the MTU migration process completes. 

The migration is disruptive and nodes in your cluster might be temporarily unavailable as the MTU update takes effect. 

The following procedures describe how to change the cluster network MTU by using machine configs, Dynamic Host Configuration Protocol (DHCP), or an ISO image. If you use either the DHCP or ISO approaches, you must refer to configuration artifacts that you kept after installing your cluster to complete the procedure.
