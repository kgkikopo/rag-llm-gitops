# 1.7. SelfSubjectReview [authentication.k8s.io/v1]

Description
     SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated. If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase. 
Type
     `object`
