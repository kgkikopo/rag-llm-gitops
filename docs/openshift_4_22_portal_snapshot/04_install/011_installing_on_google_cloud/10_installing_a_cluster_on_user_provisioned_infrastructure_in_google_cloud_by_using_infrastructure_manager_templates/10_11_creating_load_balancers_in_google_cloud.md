# 10.11. Creating load balancers in Google Cloud

You must configure load balancers in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template. 

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

**Prerequisites**

  * You have defined the variables in the _Exporting common variables_ section. 
  * If you are not installing a cluster into a shared VPC, you have defined the variables in the _Creating a VPC in Google Cloud_ section. 



**Procedure**

  1. If you are installing a cluster into a shared VPC, set environment variables for the cluster network and control plane subnet. 

     1. Determine the shared VPC network name by running the following command: 

```shell-session
$ gcloud compute networks list
```


     2. Set the `CLUSTER_NETWORK` variable by running the following command: 

```shell-session
$ export CLUSTER_NETWORK=$(gcloud compute networks describe <network_name> --format json | jq -r .selfLink)
```


`<network_name>` specifies the name of the network you determined. 

     3. List the available network subnets by running the following command: 

```shell-session
$ gcloud compute networks subnets list --network=<network_name>
```


`<network_name>` specifies the name of the network you determined. 

     4. Select a subnet from the list, and set the `CONTROL_SUBNET` variable by running the following command: 

```shell-session
$ export CONTROL_SUBNET=<control_subnet>
```


`<control_subnet>` specifies the name of the subnet you selected from the list of subnets. 

  2. Copy the template from the **Infrastructure Manager template for the internal load balancer** section of this topic and save it as `02_lb_int.tf` in a directory called `02_lb_int` on your computer. This template describes the internal load balancing objects that your cluster requires. 

     1. Create an internal load balancer by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <internal_lb_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},control_subnet=${CONTROL_SUBNET},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2} \
  --project=${PROJECT_NAME} \
  --local-source=./02_lb_int \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<internal_lb_deployment_name>` specifies the name of the internal load balancer deployment you create. 

     2. Export the `CLUSTER_IP` variable by running the following command: 

```shell-session
$ export CLUSTER_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-ip --region=${REGION} --format json | jq -r .address)
```


  3. Optional: For a public or externally available cluster, copy the template from the **Infrastructure Manager template for the external load balancer** section of this topic and save it as `02_lb_ext.tf` in a directory called `02_lb_ext` on your computer. This template describes the external load balancing objects that your cluster requires. 

     1. Create an external load balancer by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <external_lb_deployment_name> \
  --location=${REGION} \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./02_lb_ext \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<external_lb_deployment_name>` specifies the name of the external load balancer deployment you create. 

     2. Export the `CLUSTER_PUBLIC_IP` variable by running the following command: 

```shell-session
$ export CLUSTER_PUBLIC_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-public-ip --region=${REGION} --format json | jq -r .address)
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


## 10.11.1. Infrastructure Manager template for the external load balancer

You can use the following `02_lb_ext.tf` Infrastructure Manager template to deploy the external load balancer that you need for your OpenShift Container Platform cluster: 

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

resource "google_compute_address" "cluster_public_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-public-ip"
  region = "${var.region}"
}

resource "google_compute_http_health_check" "api_http_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-http-health-check"
  port = 6080
  request_path = "/readyz"
}

resource "google_compute_target_pool" "api_target_pool" {
  provider = google-beta

  name = "${var.infra_id}-api-target-pool"
  region = "${var.region}"
  health_checks = [
    google_compute_http_health_check.api_http_health_check.id
  ]
}

resource "google_compute_forwarding_rule" "api_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-forwarding-rule"
  ip_address = google_compute_address.cluster_public_ip.address
  port_range = "6443"
  region = "${var.region}"
  target = google_compute_target_pool.api_target_pool.id
}
```


## 10.11.2. Infrastructure Manager template for the internal load balancer

You can use the following `02_lb_int.tf` Infrastructure Manager template to deploy the internal load balancer that you need for your OpenShift Container Platform cluster: 

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
variable "control_subnet" {
  type        = string
  description = "Subnet for the control plane instances."
}
variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

locals {
  zones = ["${var.zone_0}", "${var.zone_1}", "${var.zone_2}"]
}

resource "google_compute_address" "cluster_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-ip"
  address_type = "INTERNAL"
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_health_check" "api_internal_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-health-check"
  https_health_check {
    port = 6443
  }
}

resource "google_compute_region_backend_service" "api_internal" {
  provider = google-beta

  name = "${var.infra_id}-api-internal"
  timeout_sec = 120
  protocol = "TCP"
  region = "${var.region}"
  load_balancing_scheme = "INTERNAL"
  health_checks = [
    google_compute_health_check.api_internal_health_check.id
  ]

  dynamic "backend" {
    for_each = google_compute_instance_group.master_ig

    content {
      balancing_mode = "CONNECTION"
      group = backend.value.self_link
    }
  }
}

resource "google_compute_forwarding_rule" "api_internal_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-forwarding-rule"
  ip_address = google_compute_address.cluster_ip.address
  backend_service = google_compute_region_backend_service.api_internal.id
  load_balancing_scheme = "INTERNAL"
  ports = [
    "6443",
    "22623"
  ]
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_instance_group" "master_ig" {
  provider = google-beta

  for_each = toset(local.zones)

  name = "${var.infra_id}-master-${each.key}-ig"
  network = "${var.cluster_network}"
  zone = "${each.key}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```
