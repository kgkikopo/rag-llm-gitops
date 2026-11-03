# 4.9. Uninstalling the mirror registry for Red Hat OpenShift

You can uninstall the _mirror registry for Red Hat OpenShift_ from your local host. 

**Prerequisites**

  * You have installed _mirror registry for Red Hat OpenShift_ on a local host. 



**Procedure**

  * Uninstall the _mirror registry for Red Hat OpenShift_ from your local host by running the following command: 

```shell-session
$ ./mirror-registry uninstall -v \
  --quayRoot <example_directory_name>
```


Note

    * Deleting the _mirror registry for Red Hat OpenShift_ prompts the user before deletion. You can use `--autoApprove` to skip this prompt. 
    * Users who install the _mirror registry for Red Hat OpenShift_ with the `--quayRoot` flag must include the `--quayRoot` flag when uninstalling. For example, if you installed the _mirror registry for Red Hat OpenShift_ with `--quayRoot example_directory_name`, you must include that string to properly uninstall the mirror registry.
