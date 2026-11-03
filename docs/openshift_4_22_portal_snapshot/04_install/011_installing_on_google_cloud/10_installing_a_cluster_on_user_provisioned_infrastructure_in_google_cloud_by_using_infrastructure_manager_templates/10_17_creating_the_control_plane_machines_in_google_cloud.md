# 10.17. Creating the control plane machines in Google Cloud

You must create the control plane machines in Google Cloud for your cluster to use. One way to create these machines is to modify the provided Infrastructure Manager template. 

Note

If you do not use the provided template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

**Prerequisites**

  * You defined the variables in the _Exporting common variables_ , _Creating load balancers in Google Cloud_ , _Creating IAM roles in Google Cloud_ , and _Creating the bootstrap machine in Google Cloud_ sections. 
  * You created the bootstrap machine. 
  * You created the Ignition configuration files. 



**Procedure**

  1. Copy the template from the **Infrastructure Manager template for control plane machines** section of this topic and save it as `05_control_plane.tf` in a folder called `05_control_plane` on your computer. This template describes the control plane machines that your cluster requires. 

     * You can edit the `05_control_plane.tf` file to add additional tags to the control plane machines, by modifying the existing `tags` stanza. The following example adds a custom tag to the first control plane machine, which is named `master_0`: 

```bash
resource "google_compute_instance" "master_0" {
# ...
  tags = [
    "${var.infra_id}-master",
    "custom_tag_example"
  ]
# ...
}
```


  2. Copy the `master.ign` file from your installation directory into the `05_control_plane` folder by running the following command: 

```shell-session
$ cp <installation_directory>/master.ign 05_control_plane/master.ign
```


`<installation_directory>` specifies the directory where you created the Ignition configuration files. 

  3. Create the control plane deployment by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <control_plane_deployment> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./05_control_plane \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${MASTER_SERVICE_ACCOUNT} \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


`<control_plane_deployment>` specifies the name of the control plane deployment. 

  4. Delete the temporary ignition file from the `05_control_plane` folder by running the following command: 

```shell-session
$ rm 05_control_plane/master.ign
```


  5. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the control plane machines manually. 

     1. Add the first control plane machine to an internal load balancer instance group by running the following command: 

```shell-session
$ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_0}-ig --zone=${ZONE_0} --instances=${INFRA_ID}-master-0
```


     2. Add the second control plane machine to an internal load balancer instance group by running the following command: 

```shell-session
$ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_1}-ig --zone=${ZONE_1} --instances=${INFRA_ID}-master-1
```


     3. Add the third control plane machine to an internal load balancer instance group by running the following command: 

```shell-session
$ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_2}-ig --zone=${ZONE_2} --instances=${INFRA_ID}-master-2
```


  6. For an external cluster, you must also add the control plane machines to external load balancer target pools. 

     1. Add the first control plane machine to an external load balancer pool by running the following command: 

```shell-session
$ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_0}" --instances=${INFRA_ID}-master-0
```


     2. Add the second control plane machine to an external load balancer pool by running the following command: 

```shell-session
$ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_1}" --instances=${INFRA_ID}-master-1
```


     3. Add the third control plane machine to an external load balancer pool by running the following command: 

```shell-session
$ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_2}" --instances=${INFRA_ID}-master-2
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


## 10.17.1. Infrastructure Manager template for control plane machines

You can use the following `05_control_plane.tf` Infrastructure Manager template to deploy the control plane machines that you need for your OpenShift Container Platform cluster: 

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
    local = {
        source = "hashicorp/local",
        version = ">= 2.0.0"
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

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the control plane machine."
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
  description = "Email for the service account attached to the control planes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/master.ign"
}

resource "google_compute_instance" "master_0" {
  provider = google-beta

  name = "${var.infra_id}-master-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
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

resource "google_compute_instance" "master_1" {
  provider = google-beta

  name = "${var.infra_id}-master-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
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

resource "google_compute_instance" "master_2" {
  provider = google-beta

  name = "${var.infra_id}-master-2"
  zone = "${var.zone_2}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
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
