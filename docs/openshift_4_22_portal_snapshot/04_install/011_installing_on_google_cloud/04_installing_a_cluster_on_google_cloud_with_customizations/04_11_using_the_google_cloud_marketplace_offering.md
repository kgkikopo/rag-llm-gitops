# 4.11. Using the Google Cloud Marketplace offering

You can deploy an OpenShift Container Platform cluster through the Google Cloud Marketplace offering, which is billed on a pay-per-use basis (hourly, per core) through Google Cloud. Red Hat still provides direct support for these clusters. 

By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to deploy compute machines. To deploy an OpenShift Container Platform cluster by using an RHCOS image from the Google Cloud Marketplace, override the default behavior by modifying the `install-config.yaml` file to reference the location of the Google Cloud Marketplace offer. 

Note

You should only modify the RHCOS image for compute machines to use a Google Cloud Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Google Cloud bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Google Cloud Marketplace image to them will incur additional licensing costs that cannot be recovered. 

**Prerequisites**

  * You have an existing `install-config.yaml` file. 



**Procedure**

  1. Edit the `compute.platform.gcp.osImage` parameters to specify the location of the Google Cloud Marketplace image: 

     * Set the `project` parameter to `redhat-marketplace-public`
     * Set the `name` parameter to one of the following offers: 

OpenShift Container Platform
     `redhat-coreos-ocp-413-x86-64-202305021736`
OpenShift Platform Plus
     `redhat-coreos-opp-413-x86-64-202305021736`
OpenShift Kubernetes Engine
     `redhat-coreos-oke-413-x86-64-202305021736`

  2. Save the file and reference it when deploying the cluster. 

The following sample `install-config.yaml` file specifies a Google Cloud Marketplace image for compute machines: 

```yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
# ...
compute:
  platform:
    gcp:
      osImage:
        project: redhat-marketplace-public
        name: redhat-coreos-ocp-413-x86-64-202305021736
# ...
```
