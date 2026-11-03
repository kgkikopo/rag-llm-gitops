# Chapter 5. User [user.openshift.io/v1]

Description
    

Upon log in, every user of the system receives a User and Identity resource. Administrators may directly manipulate the attributes of the users for their own tracking, or set groups via the API. The user name is unique and is chosen based on the value provided by the identity provider - if a user already exists with the incoming name, the user name may have a number appended to it depending on the configuration of the system. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `groups`

- [5.1. Specification](05_01_specification.md)
- [5.2. API endpoints](05_02_api_endpoints.md)
