# 3.1. Leader election and log replication of etcd

etcd uses Raft leader election and log replication so the cluster stays consistent during writes. Understanding how the leader handles quorum requests helps you diagnose control plane latency and write failures. 

etcd is a consistent, distributed key-value store that operates as a cluster of replicated nodes. Following the Raft algorithm, etcd operates by electing one node as the leader and the others as followers. The leader maintains the system’s current state and ensures that the followers are up-to-date. 

The leader node is responsible for log replication. It handles incoming write transactions from the client and writes a Raft log entry that it then broadcasts to the followers. 

When an etcd client such as `kube-apiserver` connects to an etcd member that is requesting an action that requires a quorum, such as writing a value, if the etcd member is a follower, it returns a message indicating the transaction should be sent to the leader. 

When the etcd client requests an action that requires a quorum from the leader, the leader keeps the client connection open while it writes the local Raft log, broadcasts the log to the followers, and waits for the majority of the followers to acknowledge to have committed the log without failures. Only then does the leader send the acknowledgment to the etcd client and close the session. If failure notifications are received from the followers and the majority fails to reach a consensus, the leader returns the error message to the client and closes the session. 

**Additional resources**

  * [The etcd learner design](https://etcd.io/docs/v3.5/learning/design-learner/)
  * [Failure modes](https://etcd.io/docs/v3.5/op-guide/failures/)
