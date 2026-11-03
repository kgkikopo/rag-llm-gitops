# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object metadata   
`spec` |  `object` |  DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.   
Show more

## 4.1.1. .spec

Description
     DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it. 
Type
     `object`

Property| Type| Description  
---|---|---  
`config` |  `array` |  Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim.   
`config[]` |  `object` |  DeviceClassConfiguration is used in DeviceClass.   
`extendedResourceName` |  `string` |  ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod’s extended resource requests. It has the same format as the name of a pod’s extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod’s extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.  This is an alpha field.   
`selectors` |  `array` |  Each selector must be satisfied by a device which is claimed via this class.   
`selectors[]` |  `object` |  DeviceSelector must have exactly one field set.   
Show more

## 4.1.2. .spec.config

Description
    

Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver. 

They are passed to the driver, but are not considered while allocating the claim. 

Type
     `array`

## 4.1.3. .spec.config[]

Description
     DeviceClassConfiguration is used in DeviceClass. 
Type
     `object`

Property| Type| Description  
---|---|---  
`opaque` |  `object` |  OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.   
Show more

## 4.1.4. .spec.config[].opaque

Description
     OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor. 
Type
     `object`
Required
    

  * `driver`
  * `parameters`



Property| Type| Description  
---|---|---  
`driver` |  `string` |  Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters.   
`parameters` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki.   
Show more

## 4.1.5. .spec.selectors

Description
     Each selector must be satisfied by a device which is claimed via this class. 
Type
     `array`

## 4.1.6. .spec.selectors[]

Description
     DeviceSelector must have exactly one field set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cel` |  `object` |  CELDeviceSelector contains a CEL expression for selecting a device.   
Show more

## 4.1.7. .spec.selectors[].cel

Description
     CELDeviceSelector contains a CEL expression for selecting a device. 
Type
     `object`
Required
    

  * `expression`



Property| Type| Description  
---|---|---  
`expression` |  `string` |  Expression is a CEL expression which evaluates a single device. It must evaluate to true when the device under consideration satisfies the desired criteria, and false when it does not. Any other result is an error and causes allocation of devices to abort.  The expression’s input is an object named "device", which carries the following properties: - driver (string): the name of the driver which defines this device. - attributes (map[string]object): the device’s attributes, grouped by prefix (e.g. device.attributes["dra.example.com"] evaluates to an object with all of the attributes which were prefixed by "dra.example.com". - capacity (map[string]object): the device’s capacities, grouped by prefix. - allowMultipleAllocations (bool): the allowMultipleAllocations property of the device (v1.34+ with the DRAConsumableCapacity feature enabled).  Example: Consider a device with driver="dra.example.com", which exposes two attributes named "model" and "ext.example.com/family" and which exposes one capacity named "modules". This input to this expression would have the following fields:  device.driver device.attributes["dra.example.com"].model device.attributes["ext.example.com"].family device.capacity["dra.example.com"].modules  The device.driver field can be used to check for a specific driver, either as a high-level precondition (i.e. you only want to consider devices from this driver) or as part of a multi-clause expression that is meant to consider devices from different drivers.  The value type of each attribute is defined by the device definition, and users who write these expressions must consult the documentation for their specific drivers. The value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown field will cause an evaluation error and allocation to abort.  A robust expression should check for the existence of attributes before referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to simplify expressions that access multiple attributes with the same domain. For example:  cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited based on the estimated number of logical steps.   
Show more
