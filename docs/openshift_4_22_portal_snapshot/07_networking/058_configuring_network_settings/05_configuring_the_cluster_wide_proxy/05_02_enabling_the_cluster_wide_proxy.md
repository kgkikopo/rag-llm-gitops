# 5.2. Enabling the cluster-wide proxy

To enable the cluster-wide egress proxy for your OpenShift Container Platform cluster, you can modify the `Proxy` object to configure HTTP and HTTPS proxy settings and specify domains that bypass the proxy. 

When a cluster is installed or upgraded without the proxy configured, a `Proxy` object is still generated but it has a nil `spec`. For example: 

```yaml
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
spec:
  trustedCA:
    name: ""
status:
```


Note

Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created. 

A cluster administrator can configure the proxy for OpenShift Container Platform by modifying the `cluster` `Proxy` object. 

Warning

After you enable the cluster-wide proxy capability for your cluster and you save the `Proxy` object file, the Machine Config Operator (MCO) reboots all nodes in your cluster so that each node can access connections that exist outside of the cluster. You do not need to manually reboot these nodes. 

**Prerequisites**

  * You have cluster administrator permissions. 
  * You installed the OpenShift Container Platform `oc` CLI tool. 



**Procedure**

  1. Create a config map that contains any additional CA certificates required for proxying HTTPS connections. 

Note

You can skip this step if the identity certificate of the proxy is signed by an authority from the Red Hat Enterprise Linux CoreOS (RHCOS) trust bundle. 

     1. Create a file called `user-ca-bundle.yaml`, and provide the values of your PEM-encoded certificates: 

```yaml
apiVersion: v1
data:
  ca-bundle.crt: | 
```


1

```yaml
    <MY_PEM_ENCODED_CERTS> 
```


2

```yaml
kind: ConfigMap
metadata:
  name: user-ca-bundle 
```


3

```yaml
  namespace: openshift-config 
```


4

```yaml

```


where: 

`data.ca-bundle.crt`
     Specifies the data key that must be named `ca-bundle.crt`. 
`<MY_PEM_ENCODED_CERTS>`
     Specifies one or more PEM-encoded X.509 certificates used to sign the proxy’s identity certificate. 
`user-ca-bundle`
     Specifies the config map name that is referenced from the `Proxy` object. 
`openshift-config`
     Specifies the namespace that the config map must exist in. 

     2. Create the config map from the `user-ca-bundle.yaml` file by entering the following command: 

```shell-session
$ oc create -f user-ca-bundle.yaml
```


  2. Use the `oc edit` command to modify the `Proxy` object: 

```shell-session
$ oc edit proxy/cluster
```


  3. Configure the necessary fields for the proxy: 

```yaml
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
spec:
  httpProxy: http://<username>:<pswd>@<ip>:<port> 
```


1

```yaml
  httpsProxy: https://<username>:<pswd>@<ip>:<port> 
```


2

```yaml
  noProxy: example.com 
```


3

```yaml
  readinessEndpoints:
  - http://www.google.com 
```


4

```yaml
  - https://www.google.com
  trustedCA:
    name: user-ca-bundle 
```


5

```yaml

```


where: 

`httpProxy`
     Specifies the proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`. 
`httpsProxy`
     Specifies the proxy URL to use for creating HTTPS connections outside the cluster. The URL scheme must be either `http` or `https`. Specify a URL for the proxy that supports the URL scheme. For example, most proxies report an error if they are configured to use `https` but they only support `http`. This failure message may not propagate to the logs and can appear to be a network connection failure instead. If using a proxy that listens for `https` connections from the cluster, you might need to configure the cluster to accept the CAs and certificates that the proxy uses. 
`noProxy`
    

Specifies a comma-separated list of destination domain names, domains, IP addresses (or other network CIDRs), and port numbers to exclude proxying. Note that Port numbers are only supported when configuring IPv6 addresses. Port numbers are not supported when configuring IPv4 addresses. 

Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass proxy for all destinations. 

If your `noproxy` field needs to include a domain address, you must explicitly specify that FQDN, or prefix-matched subdomain, in the `noproxy` field. You cannot use the IP address or CIDR range that encapsulates the domain. This is because the cluster does not wait for DNS to return the IP address before assigning the route connection, and checks explicitly against the request being made. For example, if you have a CIDR block value, such as `10.0.0.0/24`, for the `noproxy` field and the field attempts to access `https://10.0.0.11`, the addresses successfully match. However, attempting to access `https://exampleserver.externaldomain.com`, whose A record entry is `10.0.0.11`, fails. An additional value of `.externaldomain.com` for your `noproxy` field is necessary. 

If you scale up compute nodes that are not included in the network defined by the `networking.machineNetwork[].cidr` field from the installation configuration, you must add them to this list to prevent connection issues. 

This field is ignored if neither the `httpProxy` or `httpsProxy` fields are set. 

`readinessEndpoints`
     Specifies one or more URLs external to the cluster to use to perform a readiness check before writing the `httpProxy` and `httpsProxy` values to status. 
`trustedCA`
     Specifies a reference to the config map in the `openshift-config` namespace that contains additional CA certificates required for proxying HTTPS connections. Note that the config map must already exist before referencing it here. This field is required unless the proxy’s identity certificate is signed by an authority from the RHCOS trust bundle. 

  4. Save the file to apply the changes.
