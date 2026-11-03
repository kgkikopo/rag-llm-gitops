# 12.2. API endpoints

The following API endpoints are available: 

  * `/apis/packages.operators.coreos.com/v1/packagemanifests`

    * `GET`: list objects of kind PackageManifest 

  * `/apis/packages.operators.coreos.com/v1/namespaces/{namespace}/packagemanifests`

    * `GET`: list objects of kind PackageManifest 

  * `/apis/packages.operators.coreos.com/v1/namespaces/{namespace}/packagemanifests/{name}`

    * `GET`: read the specified PackageManifest 

  * `/apis/packages.operators.coreos.com/v1/namespaces/{namespace}/packagemanifests/{name}/icon`

    * `GET`: connect GET requests to icon of PackageManifest 




## 12.2.1. /apis/packages.operators.coreos.com/v1/packagemanifests

HTTP method
     `GET`
Description
     list objects of kind PackageManifest 

Table 12.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PackageManifestList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-operator-framework-operator-lifecycle-manager-pkg-package-server-apis-operators-v1-PackageManifestList) schema   
Show more

## 12.2.2. /apis/packages.operators.coreos.com/v1/namespaces/{namespace}/packagemanifests

HTTP method
     `GET`
Description
     list objects of kind PackageManifest 

Table 12.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PackageManifestList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-operator-framework-operator-lifecycle-manager-pkg-package-server-apis-operators-v1-PackageManifestList) schema   
Show more

## 12.2.3. /apis/packages.operators.coreos.com/v1/namespaces/{namespace}/packagemanifests/{name}

Table 12.3. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PackageManifest   
Show more

HTTP method
     `GET`
Description
     read the specified PackageManifest 

Table 12.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PackageManifest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/packagemanifest-packages-operators-coreos-com-v1 "Chapter 12. PackageManifest \[packages.operators.coreos.com/v1\]") schema   
Show more

## 12.2.4. /apis/packages.operators.coreos.com/v1/namespaces/{namespace}/packagemanifests/{name}/icon

Table 12.5. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PackageManifest   
Show more

HTTP method
     `GET`
Description
     connect GET requests to icon of PackageManifest 

Table 12.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  `string`  
Show more
