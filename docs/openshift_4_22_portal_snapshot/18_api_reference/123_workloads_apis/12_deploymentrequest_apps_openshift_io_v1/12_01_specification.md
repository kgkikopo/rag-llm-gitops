# 12.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`excludeTriggers` |  `array (string)` |  excludeTriggers instructs the instantiator to avoid processing the specified triggers. This field overrides the triggers from latest and allows clients to control specific logic. This field is ignored if not specified.   
`force` |  `boolean` |  force will try to force a new deployment to run. If the deployment config is paused, then setting this to true will return an Invalid error.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`latest` |  `boolean` |  latest will update the deployment config with the latest state from all triggers.   
`name` |  `string` |  name of the deployment config for requesting a new deployment.   
Show more
