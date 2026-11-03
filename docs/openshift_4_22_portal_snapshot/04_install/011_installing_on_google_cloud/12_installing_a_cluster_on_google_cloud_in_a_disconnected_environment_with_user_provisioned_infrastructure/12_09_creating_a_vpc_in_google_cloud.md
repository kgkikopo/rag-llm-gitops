# 12.9. Creating a VPC in Google Cloud

You must create a VPC in Google Cloud for your OpenShift Container Platform cluster to use. You can customize the VPC to meet your requirements. One way to create the VPC is to modify the provided Infrastructure Manager template. 

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

**Prerequisites**

  * You have defined the variables in the _Exporting common variables_ section. 



**Procedure**

  1. Copy the template from the **Infrastructure Manager template for the VPC** section of this topic and save it as `01_vpc.tf` in a directory called `01_vpc` on your computer. This template describes the VPC that your cluster requires. 
  2. Create a VPC by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <vpc_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},master_subnet_cidr=${MASTER_SUBNET_CIDR},worker_subnet_cidr=${WORKER_SUBNET_CIDR} \
  --project=${PROJECT_NAME} \
  --local-source=./01_vpc \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<vpc_deployment_name>` specifies the name of the VPC deployment you create. 

  3. Configure environment variables that will be used to create other cluster infrastructure. 

     1. Configure the `CLUSTER_NETWORK` environment variable by running the following command: 

```shell-session
$ export CLUSTER_NETWORK=$(gcloud compute networks describe ${INFRA_ID}-network --format json | jq -r .selfLink)
```


     2. Configure the `CONTROL_SUBNET` environment variable by running the following command: 

```shell-session
$ export CONTROL_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-master-subnet --region=${REGION} --format json | jq -r .selfLink)
```


     3. Configure the `COMPUTE_SUBNET` environment variable by running the following command: 

```shell-session
$ export COMPUTE_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink)
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


## 12.9.1. Infrastructure Manager template for the VPC

You can use the following `01_vpc.tf` Infrastructure Manager template to deploy the VPC that you need for your OpenShift Container Platform cluster: 

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

variable "master_subnet_cidr" {
  type        = string
  description = "CIDR for the control plane subnet."
}

variable "worker_subnet_cidr" {
  type        = string
  description = "CIDR for the compute subnet."
}

resource "google_compute_network" "cluster_network" {
  provider = google-beta

  name = "${var.infra_id}-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "master_subnet" {
  provider = google-beta

  name = "${var.infra_id}-master-subnet"
  ip_cidr_range = "${var.master_subnet_cidr}"
  region = "${var.region}"
  network = google_compute_network.cluster_network.self_link
}

resource "google_compute_subnetwork" "worker_subnet" {
  provider = google-beta

  name = "${var.infra_id}-worker-subnet"
  ip_cidr_range = "${var.worker_subnet_cidr}"
  region = "${var.region}"
  network = google_compute_network.cluster_network.self_link
}

#tfimport-terraform import google_compute_router._router  __project__//-router
resource "google_compute_router" "router" {
  provider = google-beta

  name = "${var.infra_id}-router"
  network = google_compute_network.cluster_network.self_link
  region = "${var.region}"
}
resource "google_compute_router_nat" "master_nat" {
  provider = google-beta

  name = "${var.infra_id}-nat-master"
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  nat_ip_allocate_option = "AUTO_ONLY"
  min_ports_per_vm = 7168
  subnetwork {
    name = google_compute_subnetwork.master_subnet.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  router = google_compute_router.router.name
  region = "${var.region}"

  depends_on = [
    google_compute_router.router
  ]
}
resource "google_compute_router_nat" "worker_nat" {
  provider = google-beta

  name = "${var.infra_id}-nat-worker"
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  nat_ip_allocate_option = "AUTO_ONLY"
  min_ports_per_vm = 512
  subnetwork {
    name = google_compute_subnetwork.worker_subnet.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  router = google_compute_router.router.name
  region = "${var.region}"

  depends_on = [
    google_compute_router.router
  ]
}
```
