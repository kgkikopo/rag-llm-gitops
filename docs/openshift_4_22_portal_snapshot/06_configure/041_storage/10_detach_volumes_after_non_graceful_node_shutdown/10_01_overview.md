# 10.1. Overview

Non-graceful node shutdowns from hardware failures or system crashes leave volumes attached to failed nodes, blocking pod rescheduling. Applying an out-of-service taint triggers automatic volume detachment from failed nodes, enabling workload recovery without manual volume management. 

A graceful node shutdown occurs when the kubelet’s node shutdown manager detects the upcoming node shutdown action. Non-graceful shutdowns occur when the kubelet does not detect a node shutdown action, which can occur because of system or hardware failures. Also, the kubelet might not detect a node shutdown action when the shutdown command does not trigger the Inhibitor Locks mechanism used by the kubelet on Linux, or because of a user error, for example, if the shutdownGracePeriod and shutdownGracePeriodCriticalPods details are not configured correctly for that node.
