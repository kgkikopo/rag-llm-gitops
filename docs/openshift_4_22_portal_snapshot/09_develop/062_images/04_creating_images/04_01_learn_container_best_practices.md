# 4.1. Learn container best practices

When creating container images to run on OpenShift Container Platform there are a number of best practices to consider as an image author to ensure a good experience for consumers of those images. 

Because images are intended to be immutable and used as-is, the following guidelines ensure that your images are highly consumable and easy to use on OpenShift Container Platform. 

## 4.1.1. General container image guidelines

Follow fundamental guidelines for creating container images to ensure they are secure, efficient, and reproducible for deployment in OpenShift Container Platform. 

### 4.1.1.1. Reuse images

Wherever possible, base your image on an appropriate upstream image using the `FROM` statement. This ensures your image can easily pick up security fixes from an upstream image when it is updated, rather than you having to update your dependencies directly. 

In addition, use tags in the `FROM` instruction, for example, `rhel:rhel7`, to make it clear to users exactly which version of an image your image is based on. Using a tag other than `latest` ensures your image is not subjected to breaking changes that might go into the `latest` version of an upstream image. 

### 4.1.1.2. Maintain compatibility within tags

When tagging your own images, try to maintain backwards compatibility within a tag. For example, if you provide an image named `image` and it currently includes version `1.0`, you might provide a tag of `image:v1`. When you update the image, as long as it continues to be compatible with the original image, you can continue to tag the new image `image:v1`, and downstream consumers of this tag are able to get updates without being broken. 

If you later release an incompatible update, then switch to a new tag, for example `image:v2`. This allows downstream consumers to move up to the new version at will, but not be inadvertently broken by the new incompatible image. Any downstream consumer using `image:latest` takes on the risk of any incompatible changes being introduced. 

### 4.1.1.3. Avoid multiple processes

Do not start multiple services, such as a database and `SSHD`, inside one container. This is not necessary because containers are lightweight and can be easily linked together for orchestrating multiple processes. OpenShift Container Platform allows you to easily colocate and co-manage related images by grouping them into a single pod. 

This colocation ensures the containers share a network namespace and storage for communication. Updates are also less disruptive as each image can be updated less frequently and independently. Signal handling flows are also clearer with a single process as you do not have to manage routing signals to spawned processes. 

### 4.1.1.4. Use exec in wrapper scripts

Many images use wrapper scripts to do some setup before starting a process for the software being run. If your image uses such a script, that script uses `exec` so that the script’s process is replaced by your software. If you do not use `exec`, then signals sent by your container runtime go to your wrapper script instead of your software’s process. This is not what you want. 

If you have a wrapper script that starts a process for some server. You start your container, for example, using `podman run -i`, which runs the wrapper script, which in turn starts your process. If you want to close your container with `CTRL+C`. If your wrapper script used `exec` to start the server process, `podman` sends SIGINT to the server process, and everything works as you expect. If you did not use `exec` in your wrapper script, `podman` sends SIGINT to the process for the wrapper script and your process keeps running like nothing happened. 

Also note that your process runs as `PID 1` when running in a container. This means that if your main process terminates, the entire container is stopped, canceling any child processes you launched from your `PID 1` process. 

### 4.1.1.5. Clean temporary files

Remove all temporary files you create during the build process. This also includes any files added with the `ADD` command. For example, run the `yum clean` command after performing `yum install` operations. 

You can prevent the `yum` cache from ending up in an image layer by creating your `RUN` statement as follows: 

```shell-session
RUN yum -y install mypackage && yum -y install myotherpackage && yum clean all -y
```


Note that if you instead write: 

```shell-session
RUN yum -y install mypackage
RUN yum -y install myotherpackage && yum clean all -y
```


Then the first `yum` invocation leaves extra files in that layer, and these files cannot be removed when the `yum clean` operation is run later. The extra files are not visible in the final image, but they are present in the underlying layers. 

The current container build process does not allow a command run in a later layer to shrink the space used by the image when something was removed in an earlier layer. However, this may change in the future. This means that if you perform an `rm` command in a later layer, although the files are hidden it does not reduce the overall size of the image to be downloaded. Therefore, as with the `yum clean` example, it is best to remove files in the same command that created them, where possible, so they do not end up written to a layer. 

In addition, performing multiple commands in a single `RUN` statement reduces the number of layers in your image, which improves download and extraction time. 

### 4.1.1.6. Place instructions in the proper order

The container builder reads the `Dockerfile` and runs the instructions from top to bottom. Every instruction that is successfully executed creates a layer which can be reused the next time this or another image is built. It is very important to place instructions that rarely change at the top of your `Dockerfile`. Doing so ensures the next builds of the same image are very fast because the cache is not invalidated by upper layer changes. 

For example, if you are working on a `Dockerfile` that contains an `ADD` command to install a file you are iterating on, and a `RUN` command to `yum install` a package, it is best to put the `ADD` command last: 

```shell-session
FROM foo
RUN yum -y install mypackage && yum clean all -y
ADD myfile /test/myfile
```


This way each time you edit `myfile` and rerun `podman build` or `docker build`, the system reuses the cached layer for the `yum` command and only generates the new layer for the `ADD` operation. 

If instead you wrote the `Dockerfile` as: 

```shell-session
FROM foo
ADD myfile /test/myfile
RUN yum -y install mypackage && yum clean all -y
```


Then each time you changed `myfile` and reran `podman build` or `docker build`, the `ADD` operation would invalidate the `RUN` layer cache, so the `yum` operation must be rerun as well. 

### 4.1.1.7. Mark important ports

The EXPOSE instruction makes a port in the container available to the host system and other containers. While it is possible to specify that a port should be exposed with a `podman run` invocation, using the EXPOSE instruction in a `Dockerfile` makes it easier for both humans and software to use your image by explicitly declaring the ports your software needs to run: 

  * Exposed ports show up under `podman ps` associated with containers created from your image. 
  * Exposed ports are present in the metadata for your image returned by `podman inspect`. 
  * Exposed ports are linked when you link one container to another. 



### 4.1.1.8. Set environment variables

It is good practice to set environment variables with the `ENV` instruction. One example is to set the version of your project. This makes it easy for people to find the version without looking at the `Dockerfile`. Another example is advertising a path on the system that could be used by another process, such as `JAVA_HOME`. 

### 4.1.1.9. Avoid default passwords

Avoid setting default passwords. Many people extend the image and forget to remove or change the default password. This can lead to security issues if a user in production is assigned a well-known password. Passwords are configurable using an environment variable instead. 

If you do choose to set a default password, ensure that an appropriate warning message is displayed when the container is started. The message should inform the user of the value of the default password and explain how to change it, such as what environment variable to set. 

### 4.1.1.10. Avoid sshd

It is best to avoid running `sshd` in your image. You can use the `podman exec` or `docker exec` command to access containers that are running on the local host. Alternatively, you can use the `oc exec` command or the `oc rsh` command to access containers that are running on the OpenShift Container Platform cluster. Installing and running `sshd` in your image opens up additional vectors for attack and requirements for security patching. 

### 4.1.1.11. Use volumes for persistent data

Images use a _volume_ for persistent data. This way OpenShift Container Platform mounts the network storage to the node running the container, and if the container moves to a new node the storage is reattached to that node. By using the volume for all persistent storage needs, the content is preserved even if the container is restarted or moved. If your image writes data to arbitrary locations within the container, that content could not be preserved. 

All data that needs to be preserved even after the container is destroyed must be written to a volume. Container engines support a `readonly` flag for containers, which can be used to strictly enforce good practices about not writing data to ephemeral storage in a container. Designing your image around that capability now makes it easier to take advantage of it later. 

Explicitly defining volumes in your `Dockerfile` makes it easy for consumers of the image to understand what volumes they must define when running your image. 

See the "Kubernetes documentation" for more information on how volumes are used in OpenShift Container Platform. 

Note

Even with persistent volumes, each instance of your image has its own volume, and the filesystem is not shared between instances. This means the volume cannot be used to share state in a cluster. 

### 4.1.1.12. Additional resources

  * [volume](https://docs.docker.com/reference/builder/#volume)
  * [Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/volumes)



## 4.1.2. OpenShift Container Platform-specific guidelines

Use the integrated image-building capabilities of OpenShift Container Platform to create, manage, and deploy reproducible container images directly from source code or Dockerfiles. 

### 4.1.2.1. Enable images for source-to-image (S2I)

For images that are intended to run application code provided by a third party, such as a Ruby image designed to run Ruby code provided by a developer, you can enable your image to work with the Source-to-Image (S2I) build tool. S2I is a framework that makes it easy to write images that take application source code as an input and produce a new image that runs the assembled application as output. 

### 4.1.2.2. Support arbitrary user ids

By default, OpenShift Container Platform runs containers using an arbitrarily assigned user ID. This provides additional security against processes escaping the container due to a container engine vulnerability and thereby achieving escalated permissions on the host node. 

For an image to support running as an arbitrary user, directories and files that are written to by processes in the image must be owned by the root group and be read/writable by that group. Files to be executed must also have group execute permissions. 

Adding the following to your Dockerfile sets the directory and file permissions to allow users in the root group to access them in the built image: 

```shell-session
RUN chgrp -R 0 /some/directory && \
    chmod -R g=u /some/directory
```


Because the container user is always a member of the root group, the container user can read and write these files. 

Warning

Care must be taken when altering the directories and file permissions of the sensitive areas of a container. If applied to sensitive areas, such as the `/etc/passwd` file, such changes can allow the modification of these files by unintended users, potentially exposing the container or host. CRI-O supports the insertion of arbitrary user IDs into a container’s `/etc/passwd` file. As such, changing permissions is never required. 

Additionally, the `/etc/passwd` file should not exist in any container image. If it does, the CRI-O container runtime will fail to inject a random UID into the `/etc/passwd` file. In such cases, the container might face challenges in resolving the active UID. Failing to meet this requirement could impact the functionality of certain containerized applications. 

In addition, the processes running in the container must not listen on privileged ports, ports below 1024, since they are not running as a privileged user. 

Important

If your S2I image does not include a `USER` declaration with a numeric user, your builds fail by default. To allow images that use either named users or the root `0` user to build in OpenShift Container Platform, you can add the project’s builder service account, `system:serviceaccount:<your-project>:builder`, to the `anyuid` security context constraint (SCC). Alternatively, you can allow all images to run as any user. 

### 4.1.2.3. Use services for inter-image communication

For cases where your image needs to communicate with a service provided by another image, such as a web front end image that needs to access a database image to store and retrieve data, your image consumes an OpenShift Container Platform service. Services provide a static endpoint for access which does not change as containers are stopped, started, or moved. In addition, services provide load balancing for requests. 

### 4.1.2.4. Provide common libraries

For images that are intended to run application code provided by a third party, ensure that your image contains commonly used libraries for your platform. In particular, provide database drivers for common databases used with your platform. For example, provide JDBC drivers for MySQL and PostgreSQL if you are creating a Java framework image. Doing so prevents the need for common dependencies to be downloaded during application assembly time, speeding up application image builds. It also simplifies the work required by application developers to ensure all of their dependencies are met. 

### 4.1.2.5. Use environment variables for configuration

Users of your image are able to configure it without having to create a downstream image based on your image. This means that the runtime configuration is handled using environment variables. For a simple configuration, the running process can consume the environment variables directly. For a more complicated configuration or for runtimes which do not support this, configure the runtime by defining a template configuration file that is processed during startup. During this processing, values supplied using environment variables can be substituted into the configuration file or used to make decisions about what options to set in the configuration file. 

Note

It is also possible and recommended to pass secrets such as certificates and keys into the container using environment variables. This ensures that the secret values do not end up committed in an image and leaked into a container image registry. 

Providing environment variables allows consumers of your image to customize behavior, such as database settings, passwords, and performance tuning, without having to introduce a new layer on top of your image. Instead, they can simply define environment variable values when defining a pod and change those settings without rebuilding the image. 

For extremely complex scenarios, configuration can also be supplied using volumes that would be mounted into the container at runtime. However, if you elect to do it this way you must ensure that your image provides clear error messages on startup when the necessary volume or configuration is not present. 

This topic is related to the Using Services for Inter-image Communication topic in that configuration like datasources are defined in terms of environment variables that provide the service endpoint information. This allows an application to dynamically consume a datasource service that is defined in the OpenShift Container Platform environment without modifying the application image. 

In addition, tuning is done by inspecting the `cgroups` settings for the container. This allows the image to tune itself to the available memory, CPU, and other resources. For example, Java-based images tune their heap based on the `cgroup` maximum memory parameter to ensure they do not exceed the limits and get an out-of-memory error. 

### 4.1.2.6. Set image metadata

Defining image metadata helps OpenShift Container Platform better consume your container images, allowing OpenShift Container Platform to create a better experience for developers using your image. For example, you can add metadata to provide helpful descriptions of your image, or offer suggestions on other images that are needed. 

### 4.1.2.7. Clustering

You must fully understand what it means to run multiple instances of your image. In the simplest case, the load balancing function of a service handles routing traffic to all instances of your image. However, many frameworks must share information to perform leader election or failover state; for example, in session replication. 

Consider how your instances accomplish this communication when running in OpenShift Container Platform. Although pods can communicate directly with each other, their IP addresses change anytime the pod starts, stops, or is moved. Therefore, it is important for your clustering scheme to be dynamic. 

### 4.1.2.8. Logging

It is best to send all logging to standard out. OpenShift Container Platform collects standard out from containers and sends it to the centralized logging service where it can be viewed. If you must separate log content, prefix the output with an appropriate keyword, which makes it possible to filter the messages. 

If your image logs to a file, users must use manual operations to enter the running container and retrieve or view the log file. 

### 4.1.2.9. Liveness and readiness probes

Document example liveness and readiness probes that can be used with your image. These probes allow users to deploy your image with confidence that traffic is not be routed to the container until it is prepared to handle it, and that the container is restarted if the process gets into an unhealthy state. 

### 4.1.2.10. Templates

Consider providing an example template with your image. A template gives users an easy way to quickly get your image deployed with a working configuration. Your template must include the liveness and readiness probes you documented with the image, for completeness. 

**Additional resources**

  * [Source-to-Image (S2I)](https://github.com/openshift/source-to-image)
