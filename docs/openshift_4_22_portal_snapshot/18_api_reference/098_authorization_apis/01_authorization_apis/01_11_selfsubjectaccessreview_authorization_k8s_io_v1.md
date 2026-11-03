# 1.11. SelfSubjectAccessReview [authorization.k8s.io/v1]

Description
     SelfSubjectAccessReview checks whether or the current user can perform an action. Not filling in a spec.namespace means "in all namespaces". Self is a special case, because users should always be able to check whether they can perform an action 
Type
     `object`
