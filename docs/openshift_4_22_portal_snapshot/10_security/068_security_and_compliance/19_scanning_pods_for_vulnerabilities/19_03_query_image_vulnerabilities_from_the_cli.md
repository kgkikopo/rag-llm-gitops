# 19.3. Query image vulnerabilities from the CLI

You can display information about vulnerabilities detected by the Red Hat Quay Container Security Operator by using the `oc` command. 

**Prerequisites**

  * You have installed the Red Hat Quay Container Security Operator on your OpenShift Container Platform instance. 



**Procedure**

  1. Enter the following command to query for detected container image vulnerabilities: 

```shell-session
$ oc get vuln --all-namespaces
```


**Example output**

```shell-session
NAMESPACE     NAME              AGE
default       sha256.ca90...    6m56s
skynet        sha256.ca90...    9m37s
```


  2. To display details for a particular vulnerability, append the vulnerability name and its namespace to the `oc describe` command. The following example shows an active container whose image includes an RPM package with a vulnerability: 

```shell-session
$ oc describe vuln --namespace mynamespace sha256.ac50e3752...
```


**Example output**

```shell-session
Name:         sha256.ac50e3752...
Namespace:    quay-enterprise
...
Spec:
  Features:
    Name:            nss-util
    Namespace Name:  centos:7
    Version:         3.44.0-3.el7
    Versionformat:   rpm
    Vulnerabilities:
      Description: Network Security Services (NSS) is a set of libraries...
```
