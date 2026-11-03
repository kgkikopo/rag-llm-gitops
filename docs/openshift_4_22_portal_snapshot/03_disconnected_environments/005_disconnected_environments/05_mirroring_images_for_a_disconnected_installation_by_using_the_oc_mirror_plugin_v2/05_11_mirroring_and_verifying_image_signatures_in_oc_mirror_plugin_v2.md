# 5.11. Mirroring and verifying image signatures in oc-mirror plugin v2

The oc-mirror plugin v2 supports mirroring and verifying cosign tag-based signatures for container images. By default, signature mirroring is enabled. When enabled, the oc-mirror plugin v2 mirrors `Sigstore` tag-based signatures for the following images: 

  * OpenShift Container Platform release images 
  * Operator images 
  * Additional images 
  * Helm charts 



The oc-mirror plugin v2 manages image signature mirroring with the following behaviors: 

  * By default, the oc-mirror plugin v2 mirrors signatures for all images. To override this behavior, you must disable the signature mirroring. 
  * Because the certified, marketplace, and community catalogs contain third-party content, Red Hat does not ensure the availability or validity of their signatures. In such cases, you must disable signature mirroring. 



For more information on disabling signature mirroring, see "Disabling signature mirroring for oc-mirror plugin v2". 

For more details on configuration formats, see "containers-registries.d(5) manual". 

**Additional resources**

  * [containers-registries.d(5) manual](https://github.com/containers/container-libs/blob/main/image/docs/containers-registries.d.5.md)



## 5.11.1. Disabling signature mirroring for oc-mirror plugin v2

You can disable signature mirroring for all images by providing the `--remove-signatures` flag for the `oc mirror` command when the destination registry does not support signature storage or when you need to bypass invalid or expired source signatures. 

**Procedure**

  1. If you want to disable signature mirroring for all images, add `remove-signatures` flag while mirroring images. For example: 

```shell-session
$ oc mirror --config=imageset-config.yaml <destination_registry> --remove-signatures
```


  2. If you want to enable or disable signature mirroring for specific elements, such as transport protocol, registry, namespace or image, use the following steps: 

     1. Create a YAML file in either the `$HOME/.config/containers/registries.d/` or `/etc/containers/registries.d/` directory. 
     2. Specify the `use-sigstore-attachments` parameter and set it to either `true` or `false` under the specific element you want to control, as seen in the following examples: 

**Example: Disable signature mirroring for the`quay.io` registry**

```yaml
# ...
docker:
  quay.io:
    use-sigstore-attachments: false
# ...
```


**Example: Enable signature mirroring for all registries**

```yaml
# ...
default-docker:
  use-sigstore-attachments: true
# ...
```


## 5.11.2. Enabling signature verification for oc-mirror plugin v2

Starting with OpenShift Container Platform 4.19, the oc-mirror plugin v2 supports signature verification, which is disabled by default. 

When enabled, the plugin verifies that container images match their signatures, ensuring they have not been altered and come from trusted sources. If a signature mismatch is detected, the mirroring workflow will fail. 

**Procedure**

  1. If you want to enable signature verification for all images, run the following command: 

```shell-session
$ oc mirror --secure-policy=true
```


  2. If you want to enable or disable signature verification for specific elements — such as a transport protocol, registry, namespace, or image — follow these steps: 

     1. Create a `policy.json` file in either the `$HOME/.config/containers/` or `/etc/containers/` directory. 

Note

If your policy configuration file is located outside the default directory, you can specify its path by using the `--policy` flag with the `oc mirror` command. 

For more information, see [`containers-policy.json(5)`](https://github.com/containers/image/blob/main/docs/containers-policy.json.5.md). 

     2. Define verification rules for the desired scope (for example, registry or image) using the appropriate policy configuration. You can set the verification requirement by specifying the desired rule under each element. 

**Example: Enable verification for only a specific image, and reject all other images**

```plaintext
{
  "default": [{"type": "reject"}],
  "transports": {
    "docker": {
      "hostname:5000/myns/sigstore-signed-image": [
        {
          "type": "sigstoreSigned",
          "keyPath": "/path/to/sigstore-pubkey.pub",
          "signedIdentity": {"type": "matchRepository"}
        }
      ]
    }
  }
}
```
