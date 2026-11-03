# 7.5. Viewing build details

You can view build details with the web console or by using the `oc describe` CLI command. 

This displays information including: 

  * The build source. 
  * The build strategy. 
  * The output destination. 
  * Digest of the image in the destination registry. 
  * How the build was created. 



If the build uses the `Docker` or `Source` strategy, the `oc describe` output also includes information about the source revision used for the build, including the commit ID, author, committer, and message. 

**Procedure**

  * To view build details, enter the following command: 

```shell-session
$ oc describe build <build_name>
```
