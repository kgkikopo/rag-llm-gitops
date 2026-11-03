# 1.12. Image stream triggers

Image stream triggers in OpenShift Container Platform cause specific actions when image stream tags change. You can configure triggers to automatically start builds or deployments when new images are imported. 

For example, importing a new image can cause the value of the tag to change, which causes a trigger to fire when there are deployments, builds, or other resources listening for those.
