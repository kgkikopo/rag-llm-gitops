# 3.2. Dockerfile source

When you supply a `dockerfile` value, the content of this field is written to disk as a file named `dockerfile`. This is done after other input sources are processed, so if the input source repository contains a Dockerfile in the root directory, it is overwritten with this content. 

The source definition is part of the `spec` section in the `BuildConfig`: 

```yaml
source:
  dockerfile: "FROM centos:7\nRUN yum install -y httpd" 
```


1

```yaml

```


[1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/builds_using_buildconfig/creating-build-inputs#CO2-1)
    

The `dockerfile` field contains an inline Dockerfile that is built. 

**Additional resources**

  * The typical use for this field is to provide a Dockerfile to a docker strategy build.
