# 4.14. Specify files to sign

You can specify full paths or wildcard and glob patterns to sign kernel module (`.ko`) files in specific directories. 

Kernel Module Management (KMM) provides support for wildcard and glob pattern support for the `sign.filesToSign` field in the `Module` CR for signing kernel modules. In addition to using a full path to explicit files, you can use any glob patterns supported by the Bash shell to specify the files to sign. 

The `DirName` value from `moduleLoader.container.modprobe` is propagated into the sign image. The validation webhook also verifies that all `filesToSign` entries fall under the configured `DirName`. 

All paths in `filesToSign` must be under the directory defined by `DirName` in the same `moduleLoader.container.modprobe` (default `/opt`). 

The KMM Operator loads the signed kmods onto all of the nodes that match the selector. The kmods should be successfully loaded on any nodes that have the public key in their Machine Owner Key (MOK) database and on any nodes that are not secure-boot enabled (which will just ignore the signature). They should fail to load on any that have secure-boot enabled but do not have that key in their MOK database. 

## 4.14.1. Defining full paths

You can define one or more absolute paths to kernel module `.ko` files inside the image. 

The following example shows full path usage in the `sign.filesToSign` field: 

```yaml
sign:
  certSecret:
    name: <cert_secret>
  keySecret:
    name: <key_secret>
  filesToSign:
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my-kmod>.ko
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my_kmod1>.ko
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my_kmod2>.ko
```


## 4.14.2. Using wildcard and glob patterns

You can use wildcard and any glob expression supported by the Ash shell in the `sign.filesToSign` field. The shell expands each entry at sign time, so you can match multiple modules with a single entry. 

  * The following example signs all `.ko` files in that directory: 

```yaml
sign:
  certSecret:
    name: <cert_secret>
  keySecret:
    name: <key_secret>
  filesToSign:
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/*.ko
```


  * The following example signs all modules matching that pattern, for example, `kmm_ci_a.ko`, `kmm_ci_b.ko`, and so on: 

```yaml
sign:
  certSecret:
    name: <cert_secret>
  keySecret:
    name: <key_secret>
  filesToSign:
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/kmm_ci_?.ko
```


  * The following example signs `driver-a.ko`, `driver-b.ko`, or `driver-c.ko`: 

```yaml
sign:
  certSecret:
    name: <cert_secret>
  keySecret:
    name: <key_secret>
  filesToSign:
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/driver-[abc].ko
```


  * The following example signs `mod-0.ko` through `mod-9.ko`: 

```yaml
sign:
  certSecret:
    name: <cert_secret>
  keySecret:
    name: <key_secret>
  filesToSign:
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/mod-[0-9].ko
```
