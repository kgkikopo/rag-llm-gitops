# 2.6. Remove deprecated image stream tags from the Cluster Samples Operator

The Cluster Samples Operator leaves deprecated image stream tags in an image stream because users can have deployments that use the deprecated image stream tags. 

You can remove deprecated image stream tags by editing the image stream with the `oc tag` command. 

Note

Deprecated image stream tags that the samples providers have removed from their image streams are not included on initial installations. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  * Remove deprecated image stream tags by editing the image stream with the following `oc tag` command: 

```shell-session
$ oc tag -d <image_stream_name:tag>
```


**Example output**

```shell-session
Deleted tag default/<image_stream_name:tag>.
```
