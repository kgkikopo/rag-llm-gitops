# 6.3. Image stream images

To precisely identify and manage the actual image content associated with a specific tag, reference and use image stream images in OpenShift Container Platform. This ensures your application deployments reliably target immutable image definitions. 

An image stream image points from within an image stream to a particular image ID. 

Image stream images allow you to retrieve metadata about an image from a particular image stream where it is tagged. 

Image stream image objects are automatically created in OpenShift Container Platform whenever you import or tag an image into the image stream. You should never have to explicitly define an image stream image object in any image stream definition that you use to create image streams. 

The image stream image consists of the image stream name and image ID from the repository, delimited by an `@` sign: 

```plaintext
<image-stream-name>@<image-id>
```


To refer to the image in the `ImageStream` object example, the image stream image looks like: 

```plaintext
origin-ruby-sample@sha256:47463d94eb5c049b2d23b03a9530bf944f8f967a0fe79147dd6b9135bf7dd13d
```
