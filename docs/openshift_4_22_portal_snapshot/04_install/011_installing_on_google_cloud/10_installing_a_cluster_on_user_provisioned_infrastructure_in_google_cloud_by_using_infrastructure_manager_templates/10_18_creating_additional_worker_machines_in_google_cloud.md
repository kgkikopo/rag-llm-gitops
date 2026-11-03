# 10.18. Creating additional worker machines in Google Cloud

You can create worker machines in Google Cloud for your cluster by using the Infrastructure Manager template. You can adjust the number of machines by modifying the number of `google_compute_instance` resources in the provided template. 

Note

If you do not use the provided Infrastructure Manager template to create your compute machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines. 

**Prerequisites**

  * Ensure you defined the variables in the _Exporting common variables_ , _Creating load balancers in Google Cloud_ , and _Creating the bootstrap machine in Google Cloud_ sections. 
  * Create the bootstrap machine. 
  * Create the control plane machines. 



**Procedure**

  1. Copy the template from the **Infrastructure Manager template for worker machines** section of this topic and save it as `06_worker.tf` in a folder called `06_worker` on your computer. This template describes the worker machines that your cluster requires. 

     * You can edit the `06_worker.tf` file to add additional tags to the compute machines, by modifying the existing `tags` stanza as follows: 

```bash
resource "google_compute_instance" "worker_0" {
# ...
  tags = [
    "${var.infra_id}-worker-0",
    "custom-tag-example"
  ]
# ...
}
```


  2. Copy the `worker.ign` file from your installation directory into the `06_worker` folder by running the following command: 

```shell-session
$ cp <installation_directory>/worker.ign 06_worker/worker.ign
```


`<installation_directory>` specifies the directory where you created the Ignition configuration files. 

  3. Create the deployment by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <worker_deployment_name> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./06_worker \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},subnet=${COMPUTE_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${WORKER_SERVICE_ACCOUNT} \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<worker_deployment_name>` specifies the name of the deployment. 

  4. Remove the `worker.ign` file by running the following command: 

```shell-session
$ rm 06_worker/worker.ign
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


## 10.18.1. Infrastructure Manager template for worker machines

You can use the following `06_worker.tf` Infrastructure Manager template to deploy the worker machines that you need for your OpenShift Container Platform cluster: 

```plaintext
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
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

variable "subnet" {
  type        = string
  description = "Compute subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the compute machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the compute nodes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/worker.ign"
}


resource "google_compute_instance" "worker_0" {
  provider = google-beta

  name = "${var.infra_id}-worker-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "worker_1" {
  provider = google-beta

  name = "${var.infra_id}-worker-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```
