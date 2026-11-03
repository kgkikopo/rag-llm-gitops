# 1.81. io.k8s.api.core.v1.NodeSelector schema

Description
     A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms. 
Type
     `object`
Required
    

  * `nodeSelectorTerms`



## 1.81.1. Schema

Property| Type| Description  
---|---|---  
`nodeSelectorTerms` |  `array (NodeSelectorTerm)` |  Required. A list of node selector terms. The terms are ORed.   
Show more
