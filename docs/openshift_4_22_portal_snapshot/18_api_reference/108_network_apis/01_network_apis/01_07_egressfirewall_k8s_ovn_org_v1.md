# 1.7. EgressFirewall [k8s.ovn.org/v1]

Description
     EgressFirewall describes the current egress firewall for a Namespace. Traffic from a pod to an IP address outside the cluster will be checked against each EgressFirewallRule in the pod’s namespace’s EgressFirewall, in order. If no rule matches (or no EgressFirewall is present) then the traffic will be allowed by default. 
Type
     `object`
