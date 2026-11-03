# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec contains configuration for a console sample.   
Show more

## 8.1.1. .spec

Description
     spec contains configuration for a console sample. 
Type
     `object`
Required
    

  * `abstract`
  * `description`
  * `source`
  * `title`



Property| Type| Description  
---|---|---  
`abstract` |  `string` |  abstract is a short introduction to the sample.  It is required and must be no more than 100 characters in length.  The abstract is shown on the sample card tile below the title and provider and is limited to three lines of content.   
`description` |  `string` |  description is a long form explanation of the sample.  It is required and can have a maximum length of **4096** characters.  It is a README.md-like content for additional information, links, pre-conditions, and other instructions. It will be rendered as Markdown so that it can contain line breaks, links, and other simple formatting.   
`icon` |  `string` |  icon is an optional base64 encoded image and shown beside the sample title.  The format must follow the data: URL format and can have a maximum size of **10 KB**.  data:[<mediatype>][;base64],<base64 encoded image> For example:  data:image;base64, plus the base64 encoded image.  Vector images can also be used. SVG icons must start with:  data:image/svg+xml;base64, plus the base64 encoded SVG image.  All sample catalog icons will be shown on a white background (also when the dark theme is used). The web console ensures that different aspect ratios work correctly. Currently, the surface of the icon is at most 40x100px.  For more information on the data URL format, please visit <https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs>.   
`provider` |  `string` |  provider is an optional label to honor who provides the sample.  It is optional and must be no more than 50 characters in length.  A provider can be a company like "Red Hat" or an organization like "CNCF" or "Knative".  Currently, the provider is only shown on the sample card tile below the title with the prefix "Provided by "   
`source` |  `object` |  source defines where to deploy the sample service from. The sample may be sourced from an external git repository or container image.   
`tags` |  `array (string)` |  tags are optional string values that can be used to find samples in the samples catalog.  Examples of common tags may be "Java", "Quarkus", etc.  They will be displayed on the samples details page.   
`title` |  `string` |  title is the display name of the sample.  It is required and must be no more than 50 characters in length.   
`type` |  `string` |  type is an optional label to group multiple samples.  It is optional and must be no more than 20 characters in length.  Recommendation is a singular term like "Builder Image", "Devfile" or "Serverless Function".  Currently, the type is shown a badge on the sample card tile in the top right corner.   
Show more

## 8.1.2. .spec.source

Description
     source defines where to deploy the sample service from. The sample may be sourced from an external git repository or container image. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`containerImport` |  `object` |  containerImport allows the user import a container image.   
`gitImport` |  `object` |  gitImport allows the user to import code from a git repository.   
`type` |  `string` |  type of the sample, currently supported: "GitImport";"ContainerImport"   
Show more

## 8.1.3. .spec.source.containerImport

Description
     containerImport allows the user import a container image. 
Type
     `object`
Required
    

  * `image`



Property| Type| Description  
---|---|---  
`image` |  `string` |  reference to a container image that provides a HTTP service. The service must be exposed on the default port (8080) unless otherwise configured with the port field.  Supported formats: - <repository-name>/<image-name> \- docker.io/<repository-name>/<image-name> \- quay.io/<repository-name>/<image-name> \- quay.io/<repository-name>/<image-name>@sha256:<image hash> \- quay.io/<repository-name>/<image-name>:<tag>  
`service` |  `object` |  service contains configuration for the Service resource created for this sample.   
Show more

## 8.1.4. .spec.source.containerImport.service

Description
     service contains configuration for the Service resource created for this sample. 
Type
     `object`

Property| Type| Description  
---|---|---  
`targetPort` |  `integer` |  targetPort is the port that the service listens on for HTTP requests. This port will be used for Service and Route created for this sample. Port must be in the range 1 to 65535. Default port is 8080.   
Show more

## 8.1.5. .spec.source.gitImport

Description
     gitImport allows the user to import code from a git repository. 
Type
     `object`
Required
    

  * `repository`



Property| Type| Description  
---|---|---  
`repository` |  `object` |  repository contains the reference to the actual Git repository.   
`service` |  `object` |  service contains configuration for the Service resource created for this sample.   
Show more

## 8.1.6. .spec.source.gitImport.repository

Description
     repository contains the reference to the actual Git repository. 
Type
     `object`
Required
    

  * `url`



Property| Type| Description  
---|---|---  
`contextDir` |  `string` |  contextDir is used to specify a directory within the repository to build the component. Must start with `/` and have a maximum length of 256 characters. When omitted, the default value is to build from the root of the repository.   
`revision` |  `string` |  revision is the git revision at which to clone the git repository Can be used to clone a specific branch, tag or commit SHA. Must be at most 256 characters in length. When omitted the repository’s default branch is used.   
`url` |  `string` |  url of the Git repository that contains a HTTP service. The HTTP service must be exposed on the default port (8080) unless otherwise configured with the port field.  Only public repositories on GitHub, GitLab and Bitbucket are currently supported:  \- [https://github.com/<org>/<repository>](https://github.com/<org>/<repository>) \- [https://gitlab.com/<org>/<repository>](https://gitlab.com/<org>/<repository>) \- [https://bitbucket.org/<org>/<repository>](https://bitbucket.org/<org>/<repository>) The url must have a maximum length of 256 characters.   
Show more

## 8.1.7. .spec.source.gitImport.service

Description
     service contains configuration for the Service resource created for this sample. 
Type
     `object`

Property| Type| Description  
---|---|---  
`targetPort` |  `integer` |  targetPort is the port that the service listens on for HTTP requests. This port will be used for Service created for this sample. Port must be in the range 1 to 65535. Default port is 8080.   
Show more
