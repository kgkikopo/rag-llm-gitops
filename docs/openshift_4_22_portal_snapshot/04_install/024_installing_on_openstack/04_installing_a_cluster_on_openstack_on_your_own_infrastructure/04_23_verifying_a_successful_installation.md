# 4.23. Verifying a successful installation

Verify that the OpenShift Container Platform installation is complete. 

**Prerequisites**

  * You have the installation program (`openshift-install`) 



**Procedure**

  * On a command line, enter: 

```shell-session
$ openshift-install --log-level debug wait-for install-complete
```


The program outputs the console URL, as well as the administrator’s login information.
