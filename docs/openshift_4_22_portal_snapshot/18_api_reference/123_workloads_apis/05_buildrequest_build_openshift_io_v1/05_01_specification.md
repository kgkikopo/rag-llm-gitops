# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`binary` |  `object` |  BinaryBuildSource describes a binary file to be used for the Docker and Source build strategies, where the file will be extracted and used as the build source.   
`dockerStrategyOptions` |  `object` |  DockerStrategyOptions contains extra strategy options for container image builds   
`env` |  [`array (EnvVar)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-EnvVar) |  env contains additional environment variables you want to pass into a builder container.   
`from` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  from is the reference to the ImageStreamTag that triggered the build.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`lastVersion` |  `integer` |  lastVersion (optional) is the LastVersion of the BuildConfig that was used to generate the build. If the BuildConfig in the generator doesn’t match, a build will not be generated.   
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`revision` |  `object` |  SourceRevision is the revision or commit information from the source for the build   
`sourceStrategyOptions` |  `object` |  SourceStrategyOptions contains extra strategy options for Source builds   
`triggeredBy` |  `array` |  triggeredBy describes which triggers started the most recent update to the build configuration and contains information about those triggers.   
`triggeredBy[]` |  `object` |  BuildTriggerCause holds information about a triggered build. It is used for displaying build trigger data for each build and build configuration in oc describe. It is also used to describe which triggers led to the most recent update in the build configuration.   
`triggeredByImage` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  triggeredByImage is the Image that triggered this build.   
Show more

## 5.1.1. .binary

Description
     BinaryBuildSource describes a binary file to be used for the Docker and Source build strategies, where the file will be extracted and used as the build source. 
Type
     `object`

Property| Type| Description  
---|---|---  
`asFile` |  `string` |  asFile indicates that the provided binary input should be considered a single file within the build input. For example, specifying "webapp.war" would place the provided binary as `/webapp.war` for the builder. If left empty, the Docker and Source build strategies assume this file is a zip, tar, or tar.gz file and extract it as the source. The custom strategy receives this binary as standard input. This filename may not contain slashes or be '..' or '.'.   
Show more

## 5.1.2. .dockerStrategyOptions

Description
     DockerStrategyOptions contains extra strategy options for container image builds 
Type
     `object`

Property| Type| Description  
---|---|---  
`buildArgs` |  [`array (EnvVar)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-EnvVar) |  Args contains any build arguments that are to be passed to Docker. See <https://docs.docker.com/engine/reference/builder/#/arg> for more details   
`noCache` |  `boolean` |  noCache overrides the docker-strategy noCache option in the build config   
Show more

## 5.1.3. .revision

Description
     SourceRevision is the revision or commit information from the source for the build 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`git` |  `object` |  GitSourceRevision is the commit information from a git source for a build   
`type` |  `string` |  type of the build source, may be one of 'Source', 'Dockerfile', 'Binary', or 'Images'   
Show more

## 5.1.4. .revision.git

Description
     GitSourceRevision is the commit information from a git source for a build 
Type
     `object`

Property| Type| Description  
---|---|---  
`author` |  `object` |  SourceControlUser defines the identity of a user of source control   
`commit` |  `string` |  commit is the commit hash identifying a specific commit   
`committer` |  `object` |  SourceControlUser defines the identity of a user of source control   
`message` |  `string` |  message is the description of a specific commit   
Show more

## 5.1.5. .revision.git.author

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.6. .revision.git.committer

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.7. .sourceStrategyOptions

Description
     SourceStrategyOptions contains extra strategy options for Source builds 
Type
     `object`

Property| Type| Description  
---|---|---  
`incremental` |  `boolean` |  incremental overrides the source-strategy incremental option in the build config   
Show more

## 5.1.8. .triggeredBy

Description
     triggeredBy describes which triggers started the most recent update to the build configuration and contains information about those triggers. 
Type
     `array`

## 5.1.9. .triggeredBy[]

Description
     BuildTriggerCause holds information about a triggered build. It is used for displaying build trigger data for each build and build configuration in oc describe. It is also used to describe which triggers led to the most recent update in the build configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`bitbucketWebHook` |  `object` |  BitbucketWebHookCause has information about a Bitbucket webhook that triggered a build.   
`genericWebHook` |  `object` |  GenericWebHookCause holds information about a generic WebHook that triggered a build.   
`githubWebHook` |  `object` |  GitHubWebHookCause has information about a GitHub webhook that triggered a build.   
`gitlabWebHook` |  `object` |  GitLabWebHookCause has information about a GitLab webhook that triggered a build.   
`imageChangeBuild` |  `object` |  ImageChangeCause contains information about the image that triggered a build   
`message` |  `string` |  message is used to store a human readable message for why the build was triggered. E.g.: "Manually triggered by user", "Configuration change",etc.   
Show more

## 5.1.10. .triggeredBy[].bitbucketWebHook

Description
     BitbucketWebHookCause has information about a Bitbucket webhook that triggered a build. 
Type
     `object`

Property| Type| Description  
---|---|---  
`revision` |  `object` |  SourceRevision is the revision or commit information from the source for the build   
`secret` |  `string` |  secret is the obfuscated webhook secret that triggered a build.   
Show more

## 5.1.11. .triggeredBy[].bitbucketWebHook.revision

Description
     SourceRevision is the revision or commit information from the source for the build 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`git` |  `object` |  GitSourceRevision is the commit information from a git source for a build   
`type` |  `string` |  type of the build source, may be one of 'Source', 'Dockerfile', 'Binary', or 'Images'   
Show more

## 5.1.12. .triggeredBy[].bitbucketWebHook.revision.git

Description
     GitSourceRevision is the commit information from a git source for a build 
Type
     `object`

Property| Type| Description  
---|---|---  
`author` |  `object` |  SourceControlUser defines the identity of a user of source control   
`commit` |  `string` |  commit is the commit hash identifying a specific commit   
`committer` |  `object` |  SourceControlUser defines the identity of a user of source control   
`message` |  `string` |  message is the description of a specific commit   
Show more

## 5.1.13. .triggeredBy[].bitbucketWebHook.revision.git.author

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.14. .triggeredBy[].bitbucketWebHook.revision.git.committer

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.15. .triggeredBy[].genericWebHook

Description
     GenericWebHookCause holds information about a generic WebHook that triggered a build. 
Type
     `object`

Property| Type| Description  
---|---|---  
`revision` |  `object` |  SourceRevision is the revision or commit information from the source for the build   
`secret` |  `string` |  secret is the obfuscated webhook secret that triggered a build.   
Show more

## 5.1.16. .triggeredBy[].genericWebHook.revision

Description
     SourceRevision is the revision or commit information from the source for the build 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`git` |  `object` |  GitSourceRevision is the commit information from a git source for a build   
`type` |  `string` |  type of the build source, may be one of 'Source', 'Dockerfile', 'Binary', or 'Images'   
Show more

## 5.1.17. .triggeredBy[].genericWebHook.revision.git

Description
     GitSourceRevision is the commit information from a git source for a build 
Type
     `object`

Property| Type| Description  
---|---|---  
`author` |  `object` |  SourceControlUser defines the identity of a user of source control   
`commit` |  `string` |  commit is the commit hash identifying a specific commit   
`committer` |  `object` |  SourceControlUser defines the identity of a user of source control   
`message` |  `string` |  message is the description of a specific commit   
Show more

## 5.1.18. .triggeredBy[].genericWebHook.revision.git.author

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.19. .triggeredBy[].genericWebHook.revision.git.committer

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.20. .triggeredBy[].githubWebHook

Description
     GitHubWebHookCause has information about a GitHub webhook that triggered a build. 
Type
     `object`

Property| Type| Description  
---|---|---  
`revision` |  `object` |  SourceRevision is the revision or commit information from the source for the build   
`secret` |  `string` |  secret is the obfuscated webhook secret that triggered a build.   
Show more

## 5.1.21. .triggeredBy[].githubWebHook.revision

Description
     SourceRevision is the revision or commit information from the source for the build 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`git` |  `object` |  GitSourceRevision is the commit information from a git source for a build   
`type` |  `string` |  type of the build source, may be one of 'Source', 'Dockerfile', 'Binary', or 'Images'   
Show more

## 5.1.22. .triggeredBy[].githubWebHook.revision.git

Description
     GitSourceRevision is the commit information from a git source for a build 
Type
     `object`

Property| Type| Description  
---|---|---  
`author` |  `object` |  SourceControlUser defines the identity of a user of source control   
`commit` |  `string` |  commit is the commit hash identifying a specific commit   
`committer` |  `object` |  SourceControlUser defines the identity of a user of source control   
`message` |  `string` |  message is the description of a specific commit   
Show more

## 5.1.23. .triggeredBy[].githubWebHook.revision.git.author

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.24. .triggeredBy[].githubWebHook.revision.git.committer

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.25. .triggeredBy[].gitlabWebHook

Description
     GitLabWebHookCause has information about a GitLab webhook that triggered a build. 
Type
     `object`

Property| Type| Description  
---|---|---  
`revision` |  `object` |  SourceRevision is the revision or commit information from the source for the build   
`secret` |  `string` |  secret is the obfuscated webhook secret that triggered a build.   
Show more

## 5.1.26. .triggeredBy[].gitlabWebHook.revision

Description
     SourceRevision is the revision or commit information from the source for the build 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`git` |  `object` |  GitSourceRevision is the commit information from a git source for a build   
`type` |  `string` |  type of the build source, may be one of 'Source', 'Dockerfile', 'Binary', or 'Images'   
Show more

## 5.1.27. .triggeredBy[].gitlabWebHook.revision.git

Description
     GitSourceRevision is the commit information from a git source for a build 
Type
     `object`

Property| Type| Description  
---|---|---  
`author` |  `object` |  SourceControlUser defines the identity of a user of source control   
`commit` |  `string` |  commit is the commit hash identifying a specific commit   
`committer` |  `object` |  SourceControlUser defines the identity of a user of source control   
`message` |  `string` |  message is the description of a specific commit   
Show more

## 5.1.28. .triggeredBy[].gitlabWebHook.revision.git.author

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.29. .triggeredBy[].gitlabWebHook.revision.git.committer

Description
     SourceControlUser defines the identity of a user of source control 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |  email of the source control user   
`name` |  `string` |  name of the source control user   
Show more

## 5.1.30. .triggeredBy[].imageChangeBuild

Description
     ImageChangeCause contains information about the image that triggered a build 
Type
     `object`

Property| Type| Description  
---|---|---  
`fromRef` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  fromRef contains detailed information about an image that triggered a build.   
`imageID` |  `string` |  imageID is the ID of the image that triggered a new build.   
Show more
