# 4.14. Preparing the bootstrap Ignition files

The OpenShift Container Platform installation process relies on bootstrap machines that are created from a bootstrap Ignition configuration file. 

Edit the file and upload it. Then, create a secondary bootstrap Ignition configuration file that Red Hat OpenStack Platform (RHOSP) uses to download the primary file. 

**Prerequisites**

  * You have the bootstrap Ignition file that the installer program generates, `bootstrap.ign`. 
  * The infrastructure ID from the installer’s metadata file is set as an environment variable (`$INFRA_ID`). 

    * If the variable is not set, see **Creating the Kubernetes manifest and Ignition config files**. 

  * You have an HTTP(S)-accessible way to store the bootstrap Ignition file. 

    * The documented procedure uses the RHOSP image service (Glance), but you can also use the RHOSP storage service (Swift), Amazon S3, an internal HTTP server, or an ad hoc Nova server. 




**Procedure**

  1. Run the following Python script. The script modifies the bootstrap Ignition file to set the hostname and, if available, CA certificate file when it runs: 

```plaintext
import base64
import json
import os

with open('bootstrap.ign', 'r') as f:
    ignition = json.load(f)

files = ignition['storage'].get('files', [])

infra_id = os.environ.get('INFRA_ID', 'openshift').encode()
hostname_b64 = base64.standard_b64encode(infra_id + b'-bootstrap\n').decode().strip()
files.append(
{
    'path': '/etc/hostname',
    'mode': 420,
    'contents': {
        'source': 'data:text/plain;charset=utf-8;base64,' + hostname_b64
    }
})

ca_cert_path = os.environ.get('OS_CACERT', '')
if ca_cert_path:
    with open(ca_cert_path, 'r') as f:
        ca_cert = f.read().encode()
        ca_cert_b64 = base64.standard_b64encode(ca_cert).decode().strip()

    files.append(
    {
        'path': '/opt/openshift/tls/cloud-ca-cert.pem',
        'mode': 420,
        'contents': {
            'source': 'data:text/plain;charset=utf-8;base64,' + ca_cert_b64
        }
    })

ignition['storage']['files'] = files;

with open('bootstrap.ign', 'w') as f:
    json.dump(ignition, f)
```


  2. Using the RHOSP CLI, create an image that uses the bootstrap Ignition file: 

```shell-session
$ openstack image create --disk-format=raw --container-format=bare --file bootstrap.ign <image_name>
```


  3. Get the image’s details: 

```shell-session
$ openstack image show <image_name>
```


Make a note of the `file` value; it follows the pattern `v2/images/<image_ID>/file`. 

Note

Verify that the image you created is active. 

  4. Retrieve the image service’s public address: 

```shell-session
$ openstack catalog show image
```


  5. Combine the public address with the image `file` value and save the result as the storage location. The location follows the pattern `<image_service_public_URL>/v2/images/<image_ID>/file`. 
  6. Generate an auth token and save the token ID: 

```shell-session
$ openstack token issue -c id -f value
```


  7. Insert the following content into a file called `$INFRA_ID-bootstrap-ignition.json` and edit the placeholders to match your own values: 

```plaintext
{
  "ignition": {
    "config": {
      "merge": [{
        "source": "<storage_url>",
        "httpHeaders": [{
          "name": "X-Auth-Token",
          "value": "<token_ID>"
        }]
      }]
    },
    "security": {
      "tls": {
        "certificateAuthorities": [{
          "source": "data:text/plain;charset=utf-8;base64,<base64_encoded_certificate>"
        }]
      }
    },
    "version": "3.2.0"
  }
}
```


where: 

`ignition.config.merge.source`
     Replace the value of `ignition.config.merge.source` with the bootstrap Ignition file storage URL. 
`ignition.config.merge.source.httpHeaders.name`
     Specifies `name` in `httpHeaders` to `"X-Auth-Token"`. 
`ignition.config.merge.source.httpHeaders.value`
     Specifies `value` in `httpHeaders` to your token’s ID. 
`security.tls.certificateAuthorities.source`
     If the bootstrap Ignition file server uses a self-signed certificate, include the base64-encoded certificate. 

  8. Save the secondary Ignition config file. 

The bootstrap Ignition data will be passed to RHOSP during installation. 

Warning

The bootstrap Ignition file contains sensitive information, like `clouds.yaml` credentials. Ensure that you store it in a secure place, and delete it after you complete the installation process.
