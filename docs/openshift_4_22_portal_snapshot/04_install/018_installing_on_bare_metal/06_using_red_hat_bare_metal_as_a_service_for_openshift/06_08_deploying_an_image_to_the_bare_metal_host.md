# 6.8. Deploying an image to the bare-metal host

To deploy the image to the host, update the `image` field in the `spec` section of the `BareMetalHost` resource. Once you update the `image` field, provisioning begins immediately. 

Deploying an image transforms bare hardware into a functional system ready to run your workloads, in an automated and repeatable way. 

**Procedure**

  * Update the `image` field in the `BareMetalHost` CR by running the following command: 

```shell-session
$ oc patch baremetalhost <hostname> \
  --type merge -p '{"spec": {"image": {"url": "<image_url>", "checksum": "<checksum_url>", "checksumType": "auto"}}}'
```


`<hostname>`
     The name of your `BareMetalHost` resource. 
`<image_url>`
     The URL of the image to deploy. You can access images using the HTTP and OCI protocols. Accessing images using the OCI protocol is available as a Technology Preview. 
`<checksum_url>`
     The URL of the checksum file for the image.
