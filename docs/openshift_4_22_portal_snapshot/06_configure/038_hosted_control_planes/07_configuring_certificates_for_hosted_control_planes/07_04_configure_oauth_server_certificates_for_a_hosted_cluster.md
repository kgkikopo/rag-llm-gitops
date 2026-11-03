# 7.4. Configure OAuth server certificates for a hosted cluster

If you want to use certificates from a trusted certificate authority (CA) to access a hosted cluster, you can configure OAuth server certificates. 

**Prerequisites**

  * You have a running hosted cluster. 
  * You have `cluster-admin` access to the management cluster. 
  * You have access to modify the `HostedCluster` resource. 
  * You have a TLS secret that contains your signed certificate and private key in the hosted cluster namespace with the following keys: 

    * `tls.crt`
    * `tls.key`




**Procedure**

  1. Identify your hosted cluster namespace: 

     1. Export the namespace where your hosted cluster is running by entering the following command: 

```shell-session
$ export HC_NAMESPACE=<hosted_cluster_namespace>
```


     2. Export the hosted cluster name by entering the following command: 

```shell-session
$ export CLUSTER_NAME=<hosted_cluster_name>
```


  2. Discover the correct OAuth route: 

     1. Use the management cluster `kubeconfig` file to enter the following command: 

```shell-session
$ oc get route oauth -n ${HC_NAMESPACE}-${CLUSTER_NAME}
```


     2. Prepare to extract the OAuth route host by entering the following command: 

```shell-session
$ export OAUTH_HOST=$(oc get route oauth \
  -n ${HC_NAMESPACE}-${CLUSTER_NAME} \
  -o jsonpath='{.spec.host}')
```


     3. Extract the OAuth route host by entering the following command: 

```shell-session
$ echo "${OAUTH_HOST}"
```


**Example output**

```shell-session
oauth-<hosted_cluster_namespace>-<hosted_cluster_name>.apps.<management_cluster_name>.<base_domain>
```


  3. Generate a quick test certificate by entering the following command: 

```shell-session
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key \
  -out tls.crt \
  -subj "/CN=openshift-oauth" \
  -addext "subjectAltName=DNS:${OAUTH_HOST}"
```


  4. Confirm that the file exists by entering the following command: 

```shell-session
$ ls tls.crt tls.key
```


  5. If you have not already created the TLS secret in the hosted cluster namespace, create the secret by entering the following command: 

```shell-session
$ oc create secret tls my-oauth-cert-secret \
  --cert=tls.crt \
  --key=tls.key \
  -n $HC_NAMESPACE
```


**Example output**

```shell-session
secret/my-oauth-cert-secret created
```


Note

Although the OAuth server runs in the hosted control plane namespace, the serving certificate must exist in the hosted cluster namespace. Secrets that are created in the hosted control plane namespace are not picked up. 

  6. Edit the `HostedCluster` resource: 

     1. Open the `HostedCluster` resource for editing by entering the following command: 

```shell-session
$ oc edit hostedcluster $CLUSTER_NAME -n $HC_NAMESPACE
```


     2. In the resource, configure the named certificates by adding the `servingCerts.namedCertificates` stanza to the `spec.configuration.apiServer` section: 

```yaml
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  configuration:
    apiServer:
      audit:
        profile: Default
      servingCerts:
        namedCertificates:
        - names:
          - oauth-<hosted_cluster_namespace>-<hosted_cluster_name>.apps.<management_cluster_name>.<base_domain>
          servingCertificate:
            name: my-oauth-cert-secret
# ...
```


where: 

`spec.configuration.apiServer.servingCerts.namedCertificates.names`
     Specifies the actual host name of your OAuth route. 
`spec.configuration.apiServer.servingCerts.servingCertificate.name`
     Specifies the name of your TLS secret. This secret must exist in the hosted cluster namespace. 

     3. Save and apply the changes. The Control Plane Operator reconciles the changes, the configuration propagates to the control plane, and the OAuth server begins serving the new certificate. 

Important

No separate OAuth certificate configuration field exists for a hosted cluster. 




**Verification**

  * Verify the certificate being served by the route by entering the following command: 

```shell-session
$ echo | openssl s_client \
  -connect "${OAUTH_HOST}:443" \
  -servername "${OAUTH_HOST}" \
  2>/dev/null \
  | openssl x509 -noout -subject -issuer -ext subjectAltName
```


**Example output**

```shell-session
subject=CN=openshift-oauth
issuer=CN=openshift-oauth
X509v3 Subject Alternative Name:
    DNS:oauth-<hosted_cluster_namespace>-<hosted_cluster_name>.apps.<management_cluster_name>.<base_domain>
```


The output shows that the OAuth route is serving the custom certificate and the certificate comes from the `my-oauth-cert-secret` secret.
