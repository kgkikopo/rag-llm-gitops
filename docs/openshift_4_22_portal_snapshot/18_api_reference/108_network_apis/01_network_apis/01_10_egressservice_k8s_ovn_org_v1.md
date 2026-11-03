# 1.10. EgressService [k8s.ovn.org/v1]

Description
     EgressService is a CRD that allows the user to request that the source IP of egress packets originating from all of the pods that are endpoints of the corresponding LoadBalancer Service would be its ingress IP. In addition, it allows the user to request that egress packets originating from all of the pods that are endpoints of the LoadBalancer service would use a different network than the main one. 
Type
     `object`
