# 7.3. Site recommendations for multisite clusters

Plan control plane placement across data centers so your cluster maintains quorum when one site becomes unavailable. 

Assuming that each site gets one control plane member, you theoretically define three sites, which is what Red Hat recommends. As a result, one data center can go into an inactive state and the cluster still maintains quorum and operational consistency. 

When this assumption is not met, give attention to the needed and actual fault tolerance state of the cluster, as it often outlines or dictates the uptime and stability of the deployment.
