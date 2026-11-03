# 5.7. Verifying your selected images for mirroring

You can use oc-mirror plugin v2 to perform a test run (dry run) that does not actually mirror any images. This enables you to review the list of images that would be mirrored. 

You can also use a dry run to catch any errors with your image set configuration early. When running a dry run on a mirror-to-disk workflow, the oc-mirror plugin v2 checks if all the images within the image set are available in its cache. Any missing images are listed in the `missing.txt` file. When a dry run is performed before mirroring, both `missing.txt` and `mapping.txt` files contain the same list of images. 

## 5.7.1. Performing a dry run for oc-mirror plugin v2

Verify your image set configuration by performing a dry run without mirroring any images. This ensures your setup is correct and prevents unintended changes. 

**Procedure**

  * To perform a test run, run the `oc mirror` command and append the `--dry-run` argument to the command: 

```shell-session
$ oc mirror -c <image_set_config_yaml> file://<oc_mirror_workspace_path> --dry-run --v2
```


where: 

`<image_set_config_yaml>`
     Specifies the image set configuration file that you created. 
`<oc_mirror_workspace_path>`
     Insert the address of the workspace path. 
`<mirror_registry_url>`
    

Insert the URL or address of the remote container registry from which images will be mirrored or deleted. 

**Example output**

```shell-session
[INFO]   : :wave: Hello, welcome to oc-mirror
[INFO]   : :gear:  setting up the environment for you...
[INFO]   : :twisted_rightwards_arrows: workflow mode: mirrorToDisk
[INFO]   : :sleuth_or_spy:  going to discover the necessary images...
[INFO]   : :mag: collecting release images...
[INFO]   : :mag: collecting operator images...
[INFO]   : :mag: collecting additional images...
[WARN]   : :warning:  54/54 images necessary for mirroring are not available in the cache.
[WARN]   : List of missing images in : CLID-19/working-dir/dry-run/missing.txt.
please re-run the mirror to disk process
[INFO]   : :page_facing_up: list of all images for mirroring in : CLID-19/working-dir/dry-run/mapping.txt
[INFO]   : mirror time     : 9.641091076s
[INFO]   : :wave: Goodbye, thank you for using oc-mirror
```


**Verification**

  1. Navigate to the workspace directory that was generated: 

```shell-session
$ cd <oc_mirror_workspace_path>
```


  2. Review the `mapping.txt` and `missing.txt` files that were generated. These files contain a list of all images that would be mirrored.
