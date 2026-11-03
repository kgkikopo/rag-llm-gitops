# Chapter 7. ValidatingAdmissionPolicyBinding [admissionregistration.k8s.io/v1]

Description
    

ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters. 

For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don’t use params, otherwise N is the number of parameters selected by the binding. 

The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget. 

Type
     `object`

- [7.1. Specification](07_01_specification.md)
- [7.2. API endpoints](07_02_api_endpoints.md)
