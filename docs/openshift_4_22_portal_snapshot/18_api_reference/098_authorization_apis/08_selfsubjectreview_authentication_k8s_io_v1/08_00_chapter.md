# Chapter 8. SelfSubjectReview [authentication.k8s.io/v1]

Description
     SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated. If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase. 
Type
     `object`

- [8.1. Specification](08_01_specification.md)
- [8.2. API endpoints](08_02_api_endpoints.md)
