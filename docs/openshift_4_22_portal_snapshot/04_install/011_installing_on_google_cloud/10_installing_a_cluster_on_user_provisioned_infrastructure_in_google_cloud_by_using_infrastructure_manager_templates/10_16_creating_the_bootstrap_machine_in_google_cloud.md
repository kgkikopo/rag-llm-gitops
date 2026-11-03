# 10.16. Creating the bootstrap machine in Google Cloud

You must create the bootstrap machine in Google Cloud to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Infrastructure Manager template. 

Note

If you do not use the provided Infrastructure Manager template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs. 

If you need to redeploy the bootstrap machine for any reason, delete the existing bootstrap VM first. If you redeploy the bootstrap machine without deleting the existing VM, Infrastructure Manager will update the metadata and appear to succeed, but the Ignition file will not be executed again. This will result in the VM still being based on the old Ignition data. 

**Prerequisites**

  * Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in Google Cloud_ sections. 



**Procedure**

  1. Copy the template from the **Infrastructure Manager template for the bootstrap machine** section of this topic and save it as `04_bootstrap.tf` in a folder called `04_bootstrap` on your computer. This template describes the bootstrap machine that your cluster requires. 

     * You can edit the `04_bootstrap.tf` file to add additional tags to the bootstrap machine, by modifying the existing `tags` stanza as follows: 

```bash
resource "google_compute_instance" "bootstrap" {
# ...
  tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-bootstrap",
    "custom-tag-example"
  ]
# ...
}
```


  2. Export the location of the Red Hat Enterprise Linux CoreOS (RHCOS) image that the installation program requires by running the following command: 

```shell-session
$ export CLUSTER_IMAGE=(`gcloud compute images describe ${INFRA_ID}-rhcos-image --format json | jq -r .selfLink`)
```


  3. Create a bucket by running the following command: 

```shell-session
$ gcloud storage buckets create "gs://${INFRA_ID}-bootstrap-ignition"
```


  4. Upload the `bootstrap.ign` file by running the following command: 

```shell-session
$ gcloud storage cp bootstrap.ign "gs://${INFRA_ID}-bootstrap-ignition/"
```


  5. Create a signed URL for the bootstrap instance and export the URL from the output as a variable by running the following command: 

```shell-session
$ export BOOTSTRAP_IGN="$(gcloud storage sign-url --duration=2h --private-key-file=service-account-key.json "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign" | grep "^signed_url:" | awk '{print $2}')"
```


  6. Create the bootstrap deployment by running the following command: 

```shell-session
$ gcloud infra-manager deployments apply <bootstrap_deployment_name> \
  --location=${REGION} \
  --project=${PROJECT_NAME} \
  --local-source=./04_bootstrap \
  --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone=${ZONE_0},cluster_network=${CLUSTER_NETWORK},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},bootstrap_ign="${BOOTSTRAP_IGN}",is_public_cluster=<public_cluster_status> \
  --service-account=${INSTALL_SERVICE_ACCOUNT}
```


where: 

`<bootstrap_deployment_name>`
     Specifies the name of the bootstrap deployment. 
`<public_cluster_status>`
     Specifies whether the cluster is public or private. If it is a public cluster, specify `true`. If it is a private cluster, specify `false`. 

  7. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the bootstrap machine manually. 

     1. Add the bootstrap instance to the internal load balancer instance group by running the following command: 

```shell-session
$ gcloud compute instance-groups unmanaged add-instances \
    ${INFRA_ID}-bootstrap-ig --zone=${ZONE_0} --instances=${INFRA_ID}-bootstrap
```


     2. Add the bootstrap instance group to the internal load balancer backend service by running the following command: 

```shell-session
$ gcloud compute backend-services add-backend \
    ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
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


## 10.16.1. Infrastructure Manager template for the bootstrap machine

You can use the following `04_bootstrap.tf` Infrastructure Manager template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster: 

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

variable "zone" {
  type        = string
  description = "Zone inside of the region where the bootstrap node is created."
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
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
  description = "Machine type for the bootstrap machine."
  default     = "n1-standard-4"
}

variable "root_volume_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "bootstrap_ign" {
  type        = string
  description = "Bootstrap ignition data."
}

variable "is_public_cluster" {
  type        = bool
  default     = true
  description = "Whether the publish policy is the default External"
}

resource "google_compute_address" "bootstrap_public_ip" {
  provider = google-beta
  count = var.is_public_cluster ? 1 : 0

  name = "${var.infra_id}-bootstrap-public-ip"
  region = "${var.region}"
}

resource "google_compute_instance" "bootstrap" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap"
  zone = "${var.zone}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-bootstrap"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.root_volume_size}"
      image = "${var.image}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"

    # Dynamic block to conditionally create access_config
    dynamic "access_config" {
      for_each = var.is_public_cluster ? [1] : []
      content {
        nat_ip = google_compute_address.bootstrap_public_ip[0].address
      }
    }
  }
  metadata = {
    user-data = "{\"ignition\":{\"config\":{\"replace\":{\"source\":\"${var.bootstrap_ign}\"}},\"version\":\"3.2.0\"}}"
  }
}

resource "google_compute_instance_group" "bootstrap_ig" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-ig"
  network = "${var.cluster_network}"
  zone = "${var.zone}"
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
