# 4.2. Output image environment variables

docker and source-to-image (S2I) strategy builds set the following environment variables on output images: 

Variable| Description  
---|---  
`OPENSHIFT_BUILD_NAME` |  Name of the build   
`OPENSHIFT_BUILD_NAMESPACE` |  Namespace of the build   
`OPENSHIFT_BUILD_SOURCE` |  The source URL of the build   
`OPENSHIFT_BUILD_REFERENCE` |  The Git reference used in the build   
`OPENSHIFT_BUILD_COMMIT` |  Source commit used in the build   
Show more

Additionally, any user-defined environment variable, for example those configured with S2I or docker strategy options, will also be part of the output image environment variable list.
