# 1.1. Validating RHCOS live media

For user-provisioned infrastructure installations, you can access information and use the OpenShift Container Platform installer to indirectly validate RHCOS bootimage artifacts using their SHA-256 checksums. 

The OpenShift Container Platform installation program contains pinned versions of RHCOS bootimages. Fully automated installations use these pinned artifacts by default. The mirror registry where you downloaded the installation program contains a `sha256sum` encrypted with the Red Hat product key. 

**Procedure**

  * Run the following command to print the metadata for any bootimage artifact: 

```shell-session
$ openshift-install coreos print-stream-json | jq <bootimage>
```


where: 

`<bootimage>`: Specifies the query for the bootimage you want to obtain information on. For validation purposes, the bootimage artifact must have a generated `sha256sum`. This can include OVA, VHD, QCOW2, and others. For example, to get information on an `x86_64` architecture `iso` file for bare metal platforms, use `.architectures.x86_64.artifacts.metal.formats.iso`. 

**Example output**

```plaintext
{
  "disk": {
    "location": "<url>/art/storage/prod/streams/<release>/builds/rhcos-<release>-live.<architecture>.<artifact>",
    "sha256": "abc2add9746eb7be82e6919ec13aad8e9eae8cf073d8da6126d7c95ea0dee962"
  }
}
```
