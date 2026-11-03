# 1.9. EgressQoS [k8s.ovn.org/v1]

Description
     EgressQoS is a CRD that allows the user to define a DSCP value for pods egress traffic on its namespace to specified CIDRs. Traffic from these pods will be checked against each EgressQoSRule in the namespace’s EgressQoS, and if there is a match the traffic is marked with the relevant DSCP value. 
Type
     `object`
