# 12.12. Creating a private DNS zone in Google Cloud

You must configure a private DNS zone in Google Cloud for your OpenShift Container Platform cluster to use. One way to create this component is to modify the provided Infrastructure Manager template. 

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

**Prerequisites**

  * Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in Google Cloud_ sections. 



**Procedure**

  1. Copy the template from the **Infrastructure Manager template for the private DNS** section of this topic and save it as `02_dns.tf` in a folder called `02_dns` on your computer. This template describes the private DNS objects that your cluster requires. 
  2. If you are installing a cluster into a shared VPC, and the host project already has a private DNS zone, skip this step. Create the DNS zone by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <dns_zone_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_domain=${CLUSTER_DOMAIN},cluster_network=${CLUSTER_NETWORK} \
  --project=${PROJECT_NAME} \
  --local-source=./02_dns \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<dns_zone_deployment_name>` specifies the name of the DNS zone deployment you create. 

  3. The templates do not create DNS entries due to limitations of Infrastructure Manager, so you must create them manually: 

     1. Add the internal DNS entries by running the following commands: 

```shell-session
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
```


```shell-session
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
```


```shell-session
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
```


```shell-session
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
```


```shell-session
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
```


     2. For an external cluster, also add the external DNS entries by running the following commands: 

```shell-session
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
```


```shell-session
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
```


```shell-session
$ gcloud dns record-sets transaction add ${CLUSTER_PUBLIC_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
```


```shell-session
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
```


**Verification**

  1. Verify the deployment is active by running the following command: 

```shell-session
$ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
```


Replace `<deployment_name>` with the name of the deployment you created. 

**Example output**

```shell-session
ACTIVE
```


## 12.12.1. Infrastructure Manager template for the private DNS

You can use the following `02_dns.tf` Infrastructure Manager template to deploy the private DNS that you need for your OpenShift Container Platform cluster: 

```plaintext
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_domain" {
  type        = string
  description = "ClusterName.BaseDomain"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

resource "google_dns_managed_zone" "private_zone" {
  provider = google-beta

  name = "${var.infra_id}-private-zone"
  dns_name = "${var.cluster_domain}."
  description = "OpenShift Installer UPI create private DNS zone."
  visibility = "private"
  private_visibility_config {
    networks {
      network_url = "${var.cluster_network}"
    }
  }

  force_destroy = false
}
```
