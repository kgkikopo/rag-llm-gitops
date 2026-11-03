# 3.3. Enabling Swift on RHOSP

Swift is operated by a user account with the `swiftoperator` role. Add the role to an account before you run the installation program. 

Important

If [the Red Hat OpenStack Platform (RHOSP) object storage service](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html-single/storage_guide/index#ch-manage-containers), commonly known as Swift, is available, OpenShift Container Platform uses Swift as the image registry storage. If Swift is unavailable, the installation program relies on the RHOSP block storage service, commonly known as Cinder. 

If Swift is present and you want to use it, you must enable access to Swift. If Swift is not present, or if you do not want to use Swift, skip this section. 

Important

RHOSP 17 sets the `rgw_max_attr_size` parameter of Ceph RGW to 256 characters. This setting causes issues with uploading container images to the OpenShift Container Platform registry. You must set the value of `rgw_max_attr_size` to at least 1024 characters. 

Before installation, check if your RHOSP deployment is affected by this problem. If your deployment is affected by this problem, reconfigure Ceph RGW. 

**Prerequisites**

  * You have a RHOSP administrator account on the target environment. 
  * The Swift service is installed. 
  * On [Ceph RGW](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html-single/deploying_an_overcloud_with_containerized_red_hat_ceph/index#ceph-rgw), the `account in url` option is enabled. 



**Procedure**

  * As an administrator in the RHOSP CLI, add the `swiftoperator` role to the account that will access Swift: 

```shell-session
$ openstack role add --user <user> --project <project> swiftoperator
```


Your RHOSP deployment can now use Swift for the image registry.
