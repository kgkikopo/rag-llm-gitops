# 21.5. Generate a JUnit latency test report

To analyze system performance and track execution delays, generate a JUnit latency test report. Reviewing this diagnostic output helps you identify configuration issues and performance bottlenecks within your cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in as a user with `cluster-admin` privileges. 



**Procedure**

  * Create a JUnit-compliant XML report by passing the `--junit` parameter together with the path to where the report is dumped: 

Note

You must create the `junit` folder before running this command. 

```shell-session
$ podman run -v $(pwd)/:/kubeconfig:Z -v $(pwd)/junit:/junit \
-e KUBECONFIG=/kubeconfig/kubeconfig registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22 \
/usr/bin/test-run.sh --ginkgo.junit-report junit/<file_name>.xml --ginkgo.v
```


where: 

`file_name`
     The name of the XML report file.
