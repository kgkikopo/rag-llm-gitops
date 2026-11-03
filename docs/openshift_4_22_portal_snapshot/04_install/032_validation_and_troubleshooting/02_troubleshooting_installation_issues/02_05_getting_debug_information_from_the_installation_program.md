# 2.5. Getting debug information from the installation program

You can choose between two methods to get debug information from the installation program. 

**Procedure**

  * Look at debug messages from a past installation in the hidden `.openshift_install.log` file. To do this task, enter a command similar to the following example: 

```shell-session
$ cat ~/<installation_directory>/.openshift_install.log
```


For `<installation_directory>`, specify the same directory you specified when you ran `./openshift-install create cluster`. 

  * Change to the directory that contains the installation program and re-run the command with the `--log-level=debug` argument: 

```shell-session
$ ./openshift-install create cluster --dir <installation_directory> --log-level debug
```


For `<installation_directory>`, specify the same directory you specified when you ran `./openshift-install create cluster`.
