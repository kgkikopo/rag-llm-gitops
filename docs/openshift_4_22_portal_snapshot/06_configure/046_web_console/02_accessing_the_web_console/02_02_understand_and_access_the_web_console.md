# 2.2. Understand and access the web console

The web console runs as a pod on the control plane node. The static assets required to run the web console are served by the pod. 

After you install OpenShift Container Platform using the `openshift-install create cluster` command, you can find the web console URL and login credentials for the installed cluster in the CLI output of the installation program. For example: 

```shell-session
INFO Install complete!
INFO Run 'export KUBECONFIG=<your working directory>/auth/kubeconfig' to manage the cluster with 'oc', the OpenShift CLI.
INFO The cluster is ready when 'oc login -u kubeadmin -p <provided>' succeeds (wait a few minutes).
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.demo1.openshift4-beta-abcorp.com
INFO Login to the console with user: kubeadmin, password: <provided>
```


Use those details to log in and access the web console. 

For existing clusters that you did not install, you can use `oc whoami --show-console` to see the web console URL. 

Important

The `dir` parameter specifies the `assets` directory, which stores the manifest files, the ISO image, and the `auth` directory. The `auth` directory stores the `kubeadmin-password` and `kubeconfig` files. As a `kubeadmin` user, you can use the `kubeconfig` file to access the cluster with the following setting: `export KUBECONFIG=<install_directory>/auth/kubeconfig`. The `kubeconfig` is specific to the generated ISO image, so if the `kubeconfig` is set and the `oc` command fails, it is possible that the system did not boot with the generated ISO image. To perform debugging, during the bootstrap process, you can log in to the console as the `core` user by using the contents of the `kubeadmin-password` file. 

**Additional resources**

  * [OpenShift Container Platform 4.x Tested Integrations](https://access.redhat.com/articles/4128421)
  * [Enabling feature sets using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-cluster-enabling-features)
