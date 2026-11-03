# 4.1. User-provided certificates for the API server

Review user-provided TLS certificates for the API server in OpenShift Container Platform to understand their purpose, location, management, and expiration for external client access. 

## 4.1.1. Purpose

The API server is accessible by clients external to the cluster at `api.<cluster_name>.<base_domain>`. You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients. The administrator must set a custom default certificate to be used by the API server when serving content. 

## 4.1.2. Location

The user-provided certificates must be provided in a `kubernetes.io/tls` type `Secret` in the `openshift-config` namespace. Update the API server cluster configuration, the `apiserver/cluster` resource, to enable the use of the user-provided certificate. 

## 4.1.3. Management

User-provided certificates are managed by the user. 

## 4.1.4. Expiration

API server client certificate expiration is less than five minutes. 

## 4.1.5. Customization

Update the secret containing the user-managed certificate as needed. 

## 4.1.6. Additional resources

  * [Adding API server certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#api-server-certificates "3.2. Adding API server certificates")
