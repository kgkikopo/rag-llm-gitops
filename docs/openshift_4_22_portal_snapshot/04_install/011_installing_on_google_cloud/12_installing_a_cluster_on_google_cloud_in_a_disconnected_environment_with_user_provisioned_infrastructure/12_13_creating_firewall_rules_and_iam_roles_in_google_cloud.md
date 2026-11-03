# 12.13. Creating firewall rules and IAM roles in Google Cloud

You must create firewall rules and IAM roles in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template. 

If you are installing a cluster into a shared VPC and the host project already has the necessary firewall rules and IAM roles, you can skip creating these resources. 

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

**Prerequisites**

  * Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in Google Cloud_ sections. 



**Procedure**

  1. Copy the template from the **Infrastructure Manager template for firewall rules and IAM roles** section of this topic and save it as `03_security.tf` in a folder called `03_security` on your computer. This template describes the security groups that your cluster requires. 
  2. Create the firewall rules and IAM roles by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <security_deployment_name> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./03_security \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},network_cidr=${NETWORK_CIDR} \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<security_deployment_name>` specifies the name of the deployment of firewall rules and IAM roles. 

  3. Configure service account variables based on the roles you created by running the following commands: 

```shell-session
$ export MASTER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-m@${PROJECT_NAME}." --format json | jq -r '.[0].email')
```


```shell-session
$ export WORKER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-w@${PROJECT_NAME}." --format json | jq -r '.[0].email')
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


## 12.13.1. Infrastructure Manager template for firewall rules and IAM roles

You can use the following `03_security.tf` Infrastructure Manager template to deploy the firewall rules and IAM roles that you need for your OpenShift Container Platform cluster: 

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

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "network_cidr" {
  type        = string
  description = "CIDR for network of the cluster."
}

variable "allowed_external_cidr" {
  type        = string
  description = "Allowed external CIDR for firewall rule."
  default     = "0.0.0.0/0"
}

resource "google_compute_firewall" "bootstrap_in_ssh" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-in-ssh"
  source_ranges = [
    "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-bootstrap"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "api" {
  provider = google-beta

  name = "${var.infra_id}-api"
  source_ranges = [
   "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6443"]
  }
}

resource "google_compute_firewall" "health_checks" {
  provider = google-beta

  name = "${var.infra_id}-health-checks"
  source_ranges = [
    "35.191.0.0/16",
    "130.211.0.0/22",
    "209.85.152.0/22",
    "209.85.204.0/22"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6080", "6443", "22624"]
  }
}

resource "google_compute_firewall" "etcd" {
  provider = google-beta

  name = "${var.infra_id}-etcd"
  source_tags = [
    "${var.infra_id}-master"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["2379-2380"]
  }
}

resource "google_compute_firewall" "control_plane" {
  provider = google-beta

  name = "${var.infra_id}-control-plane"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["10257"]
  }
  allow {
    protocol = "tcp"
    ports = ["10259"]
  }
  allow {
    protocol = "tcp"
    ports = ["22623"]
  }
}

resource "google_compute_firewall" "internal_network" {
  provider = google-beta

  name = "${var.infra_id}-internal-network"
  source_ranges = [
    "${var.network_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "internal_cluster" {
  provider = google-beta

  name = "${var.infra_id}-internal-cluster"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "udp"
    ports = ["4789", "6081"]
  }
  allow {
    protocol = "udp"
    ports = ["500", "4500"]
  }
  allow {
    protocol = "esp"
  }
  allow {
    protocol = "tcp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "udp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "tcp"
    ports = ["10250"]
  }
  allow {
    protocol = "tcp"
    ports = ["30000-32767"]
  }
  allow {
    protocol = "udp"
    ports = ["30000-32767"]
  }
}

resource "google_service_account" "master_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-m"
  display_name = "${var.infra_id}-master-node"
}

resource "google_service_account" "worker_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-w"
  display_name = "${var.infra_id}-worker-node"
}
```
