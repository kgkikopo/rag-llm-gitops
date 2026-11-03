# 15.1. Getting the factory-precaching-cli tool

The factory-precaching-cli tool Go binary in the container image is executed on the server running an RHCOS live image using `podman`. 

The factory-precaching-cli tool Go binary is publicly available in [the {rds-first} tools container image](https://quay.io/openshift-kni/telco-ran-tools:latest). 

If you are working in a disconnected environment or have a private registry, you need to copy the image there so you can download the image to the server. 

**Procedure**

  * Pull the factory-precaching-cli tool image by running the following command: 

```shell-session
# podman pull quay.io/openshift-kni/telco-ran-tools:latest
```


**Verification**

  * To check that the tool is available, query the current version of the factory-precaching-cli tool Go binary: 

```shell-session
# podman run quay.io/openshift-kni/telco-ran-tools:latest -- factory-precaching-cli -v
```


The following is example output: 

```shell-session
factory-precaching-cli version 20221018.120852+main.feecf17
```
