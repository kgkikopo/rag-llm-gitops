# 1.2. ImageSignature [image.openshift.io/v1]

Description
    

ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
