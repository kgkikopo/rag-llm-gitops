# 1.45. com.github.operator-framework.api.pkg.operators.v1alpha1.CustomResourceDefinitions schema

Description
    

CustomResourceDefinitions declares all of the CRDs managed or required by an operator being ran by ClusterServiceVersion. 

If the CRD is present in the Owned list, it is implicitly required. 

Type
     `object`

## 1.45.1. Schema

Property| Type| Description  
---|---|---  
`owned` |  `array (CRDDescription)` |   
`required` |  `array (CRDDescription)` |   
Show more
