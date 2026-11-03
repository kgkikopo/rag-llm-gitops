# 10.2. Adding subscription entitlements as a build secret

Builds that use Red Hat subscriptions to install content must include the entitlement keys as a build secret. 

**Prerequisites**

  * You must have access to Red Hat Enterprise Linux (RHEL) package repositories through your subscription. The entitlement secret to access these repositories is automatically created by the Insights Operator when your cluster is subscribed. 
  * You must have access to the cluster as a user with the `cluster-admin` role or you have permission to access secrets in the `openshift-config-managed` project. 



**Procedure**

  1. Copy the entitlement secret from the `openshift-config-managed` namespace to the namespace of the build by entering the following commands: 

```shell-session
$ cat << EOF > secret-template.txt
kind: Secret
apiVersion: v1
metadata:
  name: etc-pki-entitlement
type: Opaque
data: {{ range \$key, \$value := .data }}
  {{ \$key }}: {{ \$value }} {{ end }}
EOF
$ oc get secret etc-pki-entitlement -n openshift-config-managed -o=go-template-file --template=secret-template.txt | oc apply -f -
```


  2. Add the etc-pki-entitlement secret as a build volume in the build configuration’s Docker strategy: 

```yaml
strategy:
  dockerStrategy:
    from:
      kind: ImageStreamTag
      name: ubi9:latest
    volumes:
    - name: etc-pki-entitlement
      mounts:
      - destinationPath: /etc/pki/entitlement
      source:
        type: Secret
        secret:
          secretName: etc-pki-entitlement
```
