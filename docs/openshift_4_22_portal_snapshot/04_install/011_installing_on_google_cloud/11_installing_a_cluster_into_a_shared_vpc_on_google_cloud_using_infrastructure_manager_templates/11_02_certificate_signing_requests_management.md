# 11.2. Certificate signing requests management

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management. 

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.
