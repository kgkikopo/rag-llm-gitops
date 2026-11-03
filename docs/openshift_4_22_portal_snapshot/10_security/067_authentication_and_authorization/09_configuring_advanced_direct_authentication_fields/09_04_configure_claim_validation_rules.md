# 9.4. Configure claim validation rules

Use Common Expression Language (CEL) expressions to define custom validation rules for JWT token claims and enforce advanced security policies such as maximum token lifetimes. 

Warning

All claim validation rules must pass for authentication to succeed. Incorrectly configured validation rules can lock all users out of the cluster. Ensure you complete the following tasks: 

  * Have a backup authentication method, such as a certificate-based kubeconfig file, before applying these rules 
  * Test validation rules in a non-production environment first 
  * Verify your CEL expressions are correct to avoid blocking valid users from accessing the cluster 



**Prerequisites**

  * You have configured an external OIDC identity provider for direct authentication. 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have access to a long-lived authentication method, such as a certificate-based kubeconfig file. 
  * You are familiar with CEL expression syntax. 



**Procedure**

  1. Create a YAML file named `authentication-claim-validation.yaml` with your claim validation rules: 

```yaml
apiVersion: config.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  type: OIDC
  oidcProviders:
  - name: my-oidc-provider
    issuer:
      issuerURL: https://idp.example.com
      audiences:
      - my-audience
    claimMappings:
      username:
        claim: email
    claimValidationRules:
    - type: CEL
      cel:
        expression: 'claims.exp - claims.nbf <= 86400'
        message: 'Total token lifetime must not exceed 24 hours'
    - type: CEL
      cel:
        expression: 'has(claims.email) && claims.email_verified && claims.email.contains("@example.com")'
        message: 'Email claim must be verified and from example.com domain'
```


where: 

`claimValidationRules`
     Specifies an array of validation rules. All must pass for authentication. 
`type`
     Specifies the validation type. Set to `CEL` for CEL-based validation. 
`cel.expression`
     Specifies the CEL expression that must evaluate to `true`. 
`cel.message`
    

Specifies the error message displayed when validation fails. 

Note

Replace the placeholder values (`my-oidc-provider`, `<https://idp.example.com>`, `my-audience`, `@example.com`) with your actual OIDC provider configuration and validation requirements. 

  2. Apply the configuration: 

```shell-session
$ oc apply -f authentication-claim-validation.yaml
```


**Verification**

  * Verify that the authentication configuration is applied successfully: 

```shell-session
$ oc get authentication.config.openshift.io/cluster -o yaml
```


  * Authenticate with a token that matches your validation rules to confirm they are enforced correctly. 
  * Check the cluster authentication Operator logs for validation errors: 

```shell-session
$ oc logs -n openshift-authentication-operator deployments/authentication-operator
```


When writing CEL expressions for claim validation: 

  * Access claims using `claims` variable (for example, `claims.sub` or `claims.foo.bar` for nested claims) 
  * Expressions must evaluate to boolean values 
  * Use `has()` to check claim existence 
  * Standard CEL operators and functions available: `&&`, `||`, `!`, `contains()`, `startsWith()`, `endsWith()`



Common use cases include: 

Enforce maximum token lifetime
    

```yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.exp - claims.nbf <= 86400'
    message: 'Token lifetime must not exceed 24 hours'
```


Require specific claim values
    

```yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.tenant == "production"'
    message: 'Only production tenant tokens are allowed'
```


Validate email domain
    

```yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'has(claims.email) && claims.email_verified && claims.email.endsWith("@trusted-domain.com")'
    message: 'Email must be verified and from trusted-domain.com'
```


When using the `email` claim, you must also check `email_verified` to ensure the email address has been verified by the identity provider. 

Combine conditions
    

```yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'has(claims.role) && (claims.role == "admin" || claims.role == "developer")'
    message: 'User must have admin or developer role'
```


**Troubleshooting**

If authentication fails after the configuration is applied
    

Even if your claim validation rules pass the configuration validation gates, runtime authentication errors can occur. Check the kube-apiserver logs for detailed error messages explaining why authentication failed: 

```shell-session
$ oc logs -n openshift-kube-apiserver -l app=openshift-kube-apiserver | grep -i auth
```


These log messages will indicate which validation rule failed and include the custom `message` you specified in the CEL expression. 

If you incorrectly configure validation rules and lock users out of the cluster
    

  1. Use your certificate-based kubeconfig to authenticate as `cluster-admin`. 
  2. Edit the Authentication custom resource to remove or fix invalid rules: 

```shell-session
$ oc edit authentication.config.openshift.io/cluster
```


  3. Monitor the cluster authentication Operator to confirm it returns to `Available` status: 

```shell-session
$ oc get clusteroperator authentication
```
