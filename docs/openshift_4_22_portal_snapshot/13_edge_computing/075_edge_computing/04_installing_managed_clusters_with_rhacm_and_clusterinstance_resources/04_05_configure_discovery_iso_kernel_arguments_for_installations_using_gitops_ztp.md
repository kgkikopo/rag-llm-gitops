# 4.5. Configure Discovery ISO kernel arguments for installations using GitOps ZTP

You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO that the GitOps Zero Touch Provisioning (ZTP) workflow uses during OpenShift Container Platform installation on managed bare-metal hosts. 

For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation. 

Note

In OpenShift Container Platform 4.22, you can only add kernel arguments. You can not replace or delete kernel arguments. 

**Prerequisites**

  * You have installed the OpenShift CLI (oc). 
  * You have logged in to the hub cluster as a user with cluster-admin privileges. 



**Procedure**

  1. Create the `InfraEnv` CR and edit the `spec.kernelArguments` specification to configure kernel arguments. 

     1. Save the following YAML in an `InfraEnv-example.yaml` file: 

Note

The `InfraEnv` CR in this example uses template syntax such as `{{ .Cluster.ClusterName }}` that is populated based on values in the `ClusterInstance` CR. The `ClusterInstance` CR automatically populates values for these templates during deployment. Do not edit the templates manually. 

```yaml
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"
  name: "{{ .Cluster.ClusterName }}"
  namespace: "{{ .Cluster.ClusterName }}"
spec:
  clusterRef:
    name: "{{ .Cluster.ClusterName }}"
    namespace: "{{ .Cluster.ClusterName }}"
  kernelArguments:
    - operation: append
      value: audit=0
    - operation: append
      value: trace=1
  sshAuthorizedKey: "{{ .Site.SshPublicKey }}"
  proxy: "{{ .Cluster.ProxySettings }}"
  pullSecretRef:
    name: "{{ .Site.PullSecretRef.Name }}"
  ignitionConfigOverride: "{{ .Cluster.IgnitionConfigOverride }}"
  nmStateConfigLabelSelector:
    matchLabels:
      nmstate-label: "{{ .Cluster.ClusterName }}"
  additionalNTPSources: "{{ .Cluster.AdditionalNTPSources }}"
```


        * `kernelArguments.operation` specifies the append operation to add a kernel argument. 
        * `kernelArguments.value` specifies the kernel argument you want to configure. This example configures the `audit` kernel argument and the `trace` kernel argument. 

  2. Commit the `InfraEnv-example.yaml` file to your Git repository and push your changes. The following example shows a sample Git repository structure: 

```plaintext
~/example-ztp/install
          └── site-install
               ├── clusterinstance-example.yaml
               ├── InfraEnv-example.yaml
               └── kustomization.yaml
```


  3. Update the `kustomization.yaml` file to use the `configMapGenerator` field to package the `InfraEnv` CR into a `ConfigMap`: 

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - clusterinstance-example.yaml
configMapGenerator:
  - name: custom-infraenv-cm
    namespace: example-cluster
    files:
      - InfraEnv-example.yaml
generatorOptions:
  disableNameSuffixHash: true
```


     * `clusterinstance-example.yaml` specifies the name of the `ClusterInstance` CR. 
     * `configMapGenerator.name` specifies the name of the `ConfigMap` that contains the custom `InfraEnv` CR. 
     * `configMapGenerator.namespace` must match the `ClusterInstance` namespace. 

  4. In your `ClusterInstance` CR, reference the `ConfigMap` in the `spec.templateRefs` field: 

```yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-cluster"
  namespace: "example-cluster"
spec:
  clusterName: "example-cluster"
  templateRefs:
    - name: custom-infraenv-cm
      namespace: example-cluster
# ...
```


     * `spec.templateRefs` specifies the `ConfigMap` CR that contains the custom `InfraEnv` CR template. 

  5. Commit the `ClusterInstance` CR and `kustomization.yaml` to your Git repository and push your changes. 

When the Argo CD pipeline syncs the changes, the SiteConfig Operator uses the custom `InfraEnv-example` CR from the generated `ConfigMap` to configure the infrastructure environment, including the custom kernel arguments. 




**Verification**

To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file. 

  1. Begin an SSH session with the target host: 

```shell-session
$ ssh -i /path/to/privatekey core@<host_name>
```


  2. View the system’s kernel arguments by using the following command: 

```shell-session
$ cat /proc/cmdline
```
