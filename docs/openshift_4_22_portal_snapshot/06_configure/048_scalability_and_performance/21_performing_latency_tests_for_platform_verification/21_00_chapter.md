# Chapter 21. Performing latency tests for platform verification

You can use the Cloud-native Network Functions (CNF) tests image to run latency tests on a CNF-enabled OpenShift Container Platform cluster, where all the components required for running CNF workloads are installed. Run the latency tests to validate node tuning for your workload. 

The `cnf-tests` container image is available at `registry.redhat.io/openshift4/cnf-tests-rhel9:v4.22`. 

Note

The `cnf-tests-rhel9` image is a multi-architecture image that supports both `x86_64` (amd64) and `aarch64` (arm64) nodes. The image pull path is the same for all architectures because the container runtime automatically resolves the correct architecture manifest.

- [21.1. Prerequisites for running latency tests](21_01_prerequisites_for_running_latency_tests.md)
- [21.2. Measuring latency](21_02_measuring_latency.md)
- [21.3. Run the latency tests](21_03_run_the_latency_tests.md)
- [21.4. Generate a latency test failure report](21_04_generate_a_latency_test_failure_report.md)
- [21.5. Generate a JUnit latency test report](21_05_generate_a_junit_latency_test_report.md)
- [21.6. Run latency tests on a single-node OpenShift cluster](21_06_run_latency_tests_on_a_single_node_openshift_cluster.md)
- [21.7. Running latency tests in a disconnected cluster](21_07_running_latency_tests_in_a_disconnected_cluster.md)
- [21.8. Troubleshoot errors with the cnf-tests container](21_08_troubleshoot_errors_with_the_cnf_tests_container.md)
