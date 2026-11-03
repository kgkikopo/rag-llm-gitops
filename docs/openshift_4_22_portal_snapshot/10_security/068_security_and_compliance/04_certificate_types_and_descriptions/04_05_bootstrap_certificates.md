# 4.5. Bootstrap certificates

You should understand how bootstrap certificates enable kubelet transport layer security (TLS) bootstrapping when nodes join a cluster, including how the certificates are issued and rotated and how the certificates are managed. 

## 4.5.1. Purpose

The kubelet, in OpenShift Container Platform 4 and later, uses the bootstrap certificate located in `/etc/kubernetes/kubeconfig` to initially bootstrap. This is followed by the bootstrap initialization process and the authorization of the kubelet to create a certificate signing request (CSR). 

In that process, the kubelet generates a CSR while communicating over the bootstrap channel. The controller manager signs the CSR, resulting in a certificate that the kubelet manages. For more information, see "Bootstrap initialization" and "Authorize kubelet to create a CSR" in the _Additional resources_ section. 

## 4.5.2. Management

These certificates are managed by the system and not the user. 

## 4.5.3. Expiration

This bootstrap certificate is valid for 10 years. 

The kubelet-managed certificate is valid for one year and rotates automatically at around the 80 percent mark of that one year. 

Note

OpenShift Lifecycle Manager (OLM) does not update the bootstrap certificate. 

## 4.5.4. Customization

You cannot customize the bootstrap certificates. 

**Additional resources**

  * [Bootstrap initialization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#bootstrap-initialization)
  * [Authorize kubelet to create a CSR](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#authorize-kubelet-to-create-csr)
