# 8.13. Provisioning your own DNS records

Use your cluster name and base domain to provision your DNS records. Point `api.<cluster_name>.<base_domain>.` to the API server IP address, and point `*.apps.<cluster_name>.<base_domain>.` to the Ingress service IP address. 

Important

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS". 

**Prerequisites**

  * You installed your cluster. 
  * You installed the `gcloud` CLI tool. 



**Procedure**

  1. Determine the infrastructure ID of your cluster by running the following command: 

```shell-session
$ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
```


where: 

`<installation_directory>`
     Specifies the directory where you ran the installation program. 

  2. Find the IP address of the API server: 

     1. If you installed a private cluster, determine the IP address of the API server by running the following command: 

```shell-session
$ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
```


where: 

`<project_name>`
     Specifies the name of your Google Cloud project. 
`<region_name>`
     Specifies the region where you installed your cluster. 

     2. If you installed a public cluster, determine the IP address of the API server by running the following command: 

```shell-session
$ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
```


  3. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. 
  4. Find the IP address of the Ingress service: 

     1. If you installed a private cluster, find the IP address of the Ingress service by running the following command: 

```shell-session
$ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
```


where: 

`<project_name>`
     Specifies the name of your Google Cloud project. 
`<region_name>`
     Specifies the region where you installed your cluster. 
`<compute_subnet_name>`
     Specifies the name of the subnet that contains your compute nodes. 

     2. If you installed a public cluster, find the IP address by using the forwarding rule: 

        1. Find the forwarding rule for the Ingress service by running the following command: 

```shell-session
$ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
```


        2. Use the forwarding rule value to find the IP address of the Ingress service by running the following command: 

```shell-session
$ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
```


where: 

`<region_name>`
     Specifies the region where you installed your cluster. 

  5. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. 



**Additional resources**

  * [Additional Google Cloud configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installation-config-parameters-gcp#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp "14.1.4. Additional Google Cloud configuration parameters")
