# 1.73. io.k8s.api.core.v1.EnvVar schema

Description
     EnvVar represents an environment variable present in a Container. 
Type
     `object`
Required
    

  * `name`



## 1.73.1. Schema

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the environment variable. May consist of any printable ASCII characters except '='.   
`value` |  `string` |  Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".   
`valueFrom` |  `EnvVarSource` |  Source for the environment variable’s value. Cannot be used if value is not empty.   
Show more
