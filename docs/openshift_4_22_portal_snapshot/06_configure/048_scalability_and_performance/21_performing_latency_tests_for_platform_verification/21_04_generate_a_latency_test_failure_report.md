# 21.4. Generate a latency test failure report

To analyze test failures and troubleshoot performance issues, generate a JUnit latency test output and test failure report. Reviewing this diagnostic data helps you pinpoint exactly where your system is experiencing delays. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 



**Procedure**

  * Create a test failure report with information about the cluster state and resources for troubleshooting by passing the `--report` parameter with the path to where the report is dumped: 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -v $(pwd)/reportdest:<report_folder_path> \
-e KUBECONFIG=/kubeconfig/kubeconfig registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22 \
/usr/bin/test-run.sh --report <report_folder_path> --ginkgo.v
```


    * `<report_folder_path>`: Specifies the path to the folder where the report is generated.
