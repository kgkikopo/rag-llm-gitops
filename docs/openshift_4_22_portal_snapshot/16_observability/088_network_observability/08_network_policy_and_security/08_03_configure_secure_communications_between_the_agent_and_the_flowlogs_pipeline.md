# 8.3. Configure secure communications between the agent and the FlowLogs Pipeline

Configure Transport Layer Security (TLS) or mutual TLS (mTLS) to secure communications between eBPF agents and the FlowLogs Pipeline. 

By default, communications are secured automatically by using OpenShift service Certificate Authority (CA) annotations with zero configuration required. 

The following example demonstrates how to provide your own certificates rather than relying on automatic TLS configuration. This configuration applies only when the deployment model is set to `Service` mode. 

**Prerequisites**

  * You have installed the Network Observability Operator. 
  * You have cluster administrator permissions. 



**Procedure**

  1. In the web console, go to **Ecosystem** **Installed Operators** page. 
  2. Under the **Provided APIs** heading for **Network Observability** , select **Flow Collector**. 
  3. Select **cluster** then select the **YAML** tab. 
  4. Configure the `FlowCollector` CR for agent TLS settings. A sample configuration is as follows: 

**Example`FlowCollector` CR for provided certificates mode**

```yaml
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  processor:
    service:
      tlsType: Provided
      providedCertificates:
        caFile:
          type: configmap
          name: my-ca-configmap
          file: service-ca.crt
        serverCert:
          type: secret
          name: my-server-cert-secret
          certFile: tls.crt
          certKey: tls.key
        clientCert: {}
# ...
```


where: 

`spec.processor.service.tlsType`
    

Specifies the TLS configuration mode: 

     * `Auto` (default): Communications are automatically secured by using OpenShift service CA annotations. This provides TLS encryption with zero configuration. 
     * `Disabled`: TLS is disabled. Communications between agents and FLP are not encrypted. Use this option only in development or testing environments. 
     * `Provided`: You provide your own certificates for TLS or mutual TLS. This option requires additional configuration by using the `caFile`, `serverCert`, and `clientCert` fields. When `clientCert` is omitted, TLS is configured rather than mTLS. 

`spec.processor.service.providedCertificates.caFile.type`
     Specifies how the CA certificate is provided. Valid values are `configmap` or `secret`. 
`spec.processor.service.providedCertificates.caFile.name`
     Name of the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.caFile.file`
     Name of the CA file within the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.serverCert.type`
     Specifies how the server (FLP) certificate is provided for both TLS and mutual TLS. Valid values are `configmap` or `secret`. 
`spec.processor.service.providedCertificates.serverCert.name`
     Name of the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.serverCert.certFile`
     Name of the server certificate file within the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.serverCert.certKey`
     Name of the server certificate key file within the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.clientCert.type`
     Specifies how the client (eBPF Agent) certificate is provided when using mutual TLS. Valid values are `configmap` or `secret`. 
`spec.processor.service.providedCertificates.clientCert.name`
     Name of the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.clientCert.certFile`
     Name of the client certificate file within the `configmap` or `secret`. 
`spec.processor.service.providedCertificates.clientCert.certKey`
     Name of the client certificate key file within the `configmap` or `secret`. 




**Verification**

  1. After configuring TLS, verify that the agents are communicating securely with FLP by running the following command: 

```shell-session
$ oc logs -n netobserv-privileged ds/netobserv-ebpf-agent | grep -i "starting grpc"
```


**Example output**

```shell-session
time="2026-09-30T07:19:14Z" level=info msg="Starting GRPC client with TLS" component=grpc.Client
```


Note

Using the `Auto` mode provides the best balance of security and ease of use for most deployments. Consider using `Provided` mode only if you have specific certificate requirements or are integrating with an existing Public Key Infrastructure (PKI). 

When using mutual TLS (mTLS) with the `Provided` mode, both the CA certificate and user certificate must be configured. The FLP verifies the agent certificate, and the agent verifies the FLP certificate.
