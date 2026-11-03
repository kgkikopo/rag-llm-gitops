# 3.9. OpenShift Container Platform timer tunables for etcd

OpenShift Container Platform sets platform-specific etcd election timeout and heartbeat interval values. Knowing these tunables helps you align network and disk requirements with expected cluster behavior. 

OpenShift Container Platform maintains etcd timers that are optimized for each platform. OpenShift Container Platform has prescribed validated values that are optimized for each platform provider. The default etcd timers with `platform=none` or `platform=metal` are as follows: 

```shell-session
- name: ETCD_ELECTION_TIMEOUT
  value: "1000"
  ...
- name: ETCD_HEARTBEAT_INTERVAL
  value: "100"
```


From an etcd perspective, the two key values are election timeout and heartbeat interval: 

Heartbeat interval
     The frequency with which the leader notifies followers that it is still the leader. 
Election timeout
     This timeout is how long a follower node will go without hearing a heartbeat before it attempts to become leader itself. 

These values do not provide the whole story for the control plane or even etcd. An etcd cluster is sensitive to disk latencies. Because etcd must persist proposals to its log, disk activity from other processes might cause long fsync latencies. The consequence is that etcd might miss heartbeats, causing request timeouts and temporary leader loss. During a leader loss and reelection, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.
