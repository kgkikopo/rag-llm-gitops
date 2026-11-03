# 7.5. Troubleshoot accessing a hosted cluster by using a custom DNS

If you encounter an issue when you access a hosted cluster by using a custom DNS, you can determine the root cause so that you can resolve the issue. 

**Procedure**

  1. Verify that the DNS record is properly configured and resolved. 
  2. Check that the TLS certificates for the custom domain are valid, verifying that the SAN is correct for your domain, by entering the following command: 

```shell-session
$ oc get secret \
  -n clusters <serving_certificate_name> \
  -o jsonpath='{.data.tls\.crt}' | base64 \
  -d |openssl x509 -text -noout -
```


  3. Ensure that network connectivity to the custom domain is working. 
  4. In the `HostedCluster` resource, verify that the status shows the correct custom `kubeconfig` information, as shown in the following example: 

**Example`HostedCluster` status**

```yaml
status:
  customKubeconfig:
    name: sample-hosted-custom-admin-kubeconfig
```


  5. Check the `kube-apiserver` logs in the `HostedControlPlane` namespace by entering the following command: 

```shell-session
$ oc logs -n <hosted_control_plane_namespace> \
  -l app=kube-apiserver -f -c kube-apiserver
```
