# 7.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object metadata; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>.   
`spec` |  `object` |  ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.   
Show more

## 7.1.1. .spec

Description
     ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchResources` |  `object` |  MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)   
`paramRef` |  `object` |  ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding.   
`policyName` |  `string` |  PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required.   
`validationActions` |  `array (string)` |  validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.  Failures defined by the ValidatingAdmissionPolicy’s FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.  validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.  The supported actions values are:  "Deny" specifies that a validation failure results in a denied request.  "Warn" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.  "Audit" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: `"validation.policy.admission.k8s.io/validation_failure": "[{\"message\": \"Invalid value\", {\"policy\": \"policy.example.com\", {\"binding\": \"policybinding.example.com\", {\"expressionIndex\": \"1\", {\"validationActions\": [\"Audit\"]}]"` Clients should expect to handle additional values by ignoring any values not recognized.  "Deny" and "Warn" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.  Required.   
Show more

## 7.1.2. .spec.matchResources

Description
     MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded) 
Type
     `object`

Property| Type| Description  
---|---|---  
`excludeResourceRules` |  `array` |  ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)   
`excludeResourceRules[]` |  `object` |  NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.   
`matchPolicy` |  `string` |  matchPolicy defines how the "MatchResources" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".  \- Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.  \- Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.  Defaults to "Equivalent"  Possible enum values: - `"Equivalent"` means requests should be sent to the webhook if they modify a resource listed in rules via another API group or version. - `"Exact"` means requests should only be sent to the webhook if they exactly match a given rule.   
`namespaceSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  NamespaceSelector decides whether to run the admission control policy on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the policy.  For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1"; you will set the selector as follows: "namespaceSelector": { "matchExpressions": [ { "key": "runlevel", "operator": "NotIn", "values": [ "0", "1" ] } ] }  If instead you want to only run the policy on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": { "matchExpressions": [ { "key": "environment", "operator": "In", "values": [ "prod", "staging" ] } ] }  See <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/> for more examples of label selectors.  Default to the empty LabelSelector, which matches everything.   
`objectSelector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  ObjectSelector decides whether to run the validation based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the cel validation, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything.   
`resourceRules` |  `array` |  ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule.   
`resourceRules[]` |  `object` |  NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.   
Show more

## 7.1.3. .spec.matchResources.excludeResourceRules

Description
     ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded) 
Type
     `array`

## 7.1.4. .spec.matchResources.excludeResourceRules[]

Description
     NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiGroups` |  `array (string)` |  APIGroups is the API groups the resources belong to. '**' is all groups. If '** ' is present, the length of the slice must be one. Required.   
`apiVersions` |  `array (string)` |  APIVersions is the API versions the resources belong to. '**' is all versions. If '** ' is present, the length of the slice must be one. Required.   
`operations` |  `array (string)` |  Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.   
`resourceNames` |  `array (string)` |  ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed.   
`resources` |  `array (string)` |  Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '**' means all resources, but not subresources. 'pods/** ' means all subresources of pods. '**/scale' means all scale subresources. '** /*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.   
`scope` |  `string` |  scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "\\*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*".  Possible enum values: - `"*"` means that all scopes are included. - `"Cluster"` means that scope is limited to cluster-scoped objects. Namespace objects are cluster-scoped. - `"Namespaced"` means that scope is limited to namespaced objects.   
Show more

## 7.1.5. .spec.matchResources.resourceRules

Description
     ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule. 
Type
     `array`

## 7.1.6. .spec.matchResources.resourceRules[]

Description
     NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiGroups` |  `array (string)` |  APIGroups is the API groups the resources belong to. '**' is all groups. If '** ' is present, the length of the slice must be one. Required.   
`apiVersions` |  `array (string)` |  APIVersions is the API versions the resources belong to. '**' is all versions. If '** ' is present, the length of the slice must be one. Required.   
`operations` |  `array (string)` |  Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.   
`resourceNames` |  `array (string)` |  ResourceNames is an optional white list of names that the rule applies to. An empty set means that everything is allowed.   
`resources` |  `array (string)` |  Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '**' means all resources, but not subresources. 'pods/** ' means all subresources of pods. '**/scale' means all scale subresources. '** /*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.   
`scope` |  `string` |  scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "\\*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*".  Possible enum values: - `"*"` means that all scopes are included. - `"Cluster"` means that scope is limited to cluster-scoped objects. Namespace objects are cluster-scoped. - `"Namespaced"` means that scope is limited to namespaced objects.   
Show more

## 7.1.7. .spec.paramRef

Description
     ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the resource being referenced.  One of `name` or `selector` must be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset.  A single parameter used for all admission requests can be configured by setting the `name` field, leaving `selector` blank, and setting namespace if `paramKind` is namespace-scoped.   
`namespace` |  `string` |  namespace is the namespace of the referenced resource. Allows limiting the search for params to a specific namespace. Applies to both `name` and `selector` fields.  A per-namespace parameter may be used by specifying a namespace-scoped `paramKind` in the policy and leaving this field empty.  \- If `paramKind` is cluster-scoped, this field MUST be unset. Setting this field results in a configuration error.  \- If `paramKind` is namespace-scoped, the namespace of the object being evaluated for admission will be used when this field is left unset. Take care that if this is left empty the binding must not match any cluster-scoped resources, which will result in an error.   
`parameterNotFoundAction` |  `string` |  `parameterNotFoundAction` controls the behavior of the binding when the resource exists, and name or selector is valid, but there are no parameters matched by the binding. If the value is set to `Allow`, then no matched parameters will be treated as successful validation by the binding. If set to `Deny`, then no matched parameters will be subject to the `failurePolicy` of the policy.  Allowed values are `Allow` or `Deny` Required   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector can be used to match multiple param objects based on their labels. Supply selector: {} to match all resources of the ParamKind.  If multiple params are found, they are all evaluated with the policy expressions and the results are ANDed together.  One of `name` or `selector` must be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset.   
Show more
