# 1.2. Identity [user.openshift.io/v1]

Description
    

Identity records a successful authentication of a user with an identity provider. The information about the source of authentication is stored on the identity, and the identity is then associated with a single user object. Multiple identities can reference a single user. Information retrieved from the authentication provider is stored in the extra field using a schema determined by the provider. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
