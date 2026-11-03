# 14.2. Collecting data for Red Hat Support

When you submit a support case to Red Hat Support, it is helpful to provide debugging information for OpenShift Container Platform and OpenShift Virtualization. 

You can use the following tools to collect debugging information: 

must-gather tool
     The `must-gather` tool collects diagnostic information, including resource definitions and service logs. 
Prometheus
     Prometheus is a time-series database and a rule evaluation engine for metrics. Prometheus sends alerts to Alertmanager for processing. 
Alertmanager
     The Alertmanager service handles alerts received from Prometheus. The Alertmanager is also responsible for sending the alerts to external notification systems. 

## 14.2.1. Collecting data about your environment

Collecting data about your environment minimizes the time required to analyze and determine the root cause. 

**Prerequisites**

  * You have set the retention time for Prometheus metrics data to a minimum of seven days. 
  * You have configured the Alertmanager to capture relevant alerts and to send alert notifications to a dedicated mailbox so that they can be viewed and persisted outside the cluster. 
  * You have recorded the exact number of affected nodes and virtual machines. 



**Procedure**

  1. Collect must-gather data for the cluster. 
  2. Collect must-gather data for Red Hat OpenShift Data Foundation, if necessary. 
  3. Collect must-gather data for OpenShift Virtualization. 
  4. Collect Prometheus metrics for the cluster. 



## 14.2.2. Collecting data about virtual machines

Collecting data about malfunctioning virtual machines (VMs) minimizes the time required to analyze and determine the root cause. 

**Prerequisites**

  * For Linux VMs, you have installed the latest QEMU guest agent. 
  * For Windows VMs, you have: 

    * Recorded the Windows patch update details. 
    * Installed the latest VirtIO drivers. 
    * Installed the latest QEMU guest agent. 
    * If Remote Desktop Protocol (RDP) is enabled, you have connected by using the desktop viewer to determine whether there is a problem with the connection software. 




**Procedure**

  1. Collect must-gather data for the VMs using the `/usr/bin/gather` script. 
  2. Collect screenshots of VMs that have crashed before you restart them. 
  3. Collect memory dumps from VMs before remediation attempts. 
  4. Record factors that the malfunctioning VMs have in common. For example, the VMs have the same host or network. 



## 14.2.3. Use the must-gather tool for OpenShift Virtualization

You can collect data about OpenShift Virtualization resources by running the `must-gather` command with the OpenShift Virtualization image. 

The default data collection includes information about the following resources: 

  * OpenShift Virtualization Operator namespaces, including child objects 
  * OpenShift Virtualization custom resource definitions 
  * Namespaces that contain virtual machines 
  * Basic virtual machine definitions 



You can add optional environment details and scripts to the `must-gather` command to collect additional information. Use these environment variables and scripts to collect data about specific VMs, images, or instance types. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Run the `must-gather` command to collect data about OpenShift Virtualization: 

```shell-session
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9 \
  -- /usr/bin/gather
```


Note

You can also collect `must-gather` logs for all Operators and products on your cluster by running following command: 

```shell-session
$ oc adm must-gather --all-images
```


    1. Run the following command to modify the number of processes running in parallel when collecting `must-gather` data: 

```shell-session
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9 \
  -- PROS=<number> /usr/bin/gather
```


`PROS` defines the number of parallel processes running to collect data. The default number of processes is 5. Increasing the number of processes may result in faster data collection, but uses more resources. Increasing the maximum number of parallel processes is not recommended. 

    2. Run the following command to collect detailed information for a specific VM in a specific namespace: 

```shell-session
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9 \
  -- NS=<namespace name> VM=<VM name> /usr/bin/gather --vms_details
```


`NS` is the environment variable for `namespace`. It is mandatory when using the `VM` environment variable. 

    3. Run the following command to collect image, image-stream, and image-stream-tags information from the cluster: 

```shell-session
$ oc adm must-gather \
 --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9 \
 /usr/bin/gather --images
```


    4. Run the following command to collect information about instance types from the cluster: 

```shell-session
$ oc adm must-gather \
 --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9 \
 /usr/bin/gather --instancetypes
```


### 14.2.3.1. must-gather tool options

To troubleshoot complex issues and collect specific data beyond the default logs, add optional parameters to the `must-gather` command when gathering information from your cluster. 

You can specify a combination of scripts and environment variables for the following options: 

  * Collecting detailed virtual machine (VM) information from a namespace 
  * Collecting detailed information about specified VMs 
  * Collecting image, image-stream, and image-stream-tags information 
  * Limiting the maximum number of parallel processes used by the `must-gather` tool 



#### 14.2.3.1.1. Environment variables

You can specify environment variables for a compatible script. 

`NS=<namespace_name>`
     Collect virtual machine information, including `virt-launcher` pod details, from the namespace that you specify. The `VirtualMachine` and `VirtualMachineInstance` CR data is collected for all namespaces. 
`VM=<vm_name>`
     Collect details about a particular virtual machine. To use this option, you must also specify a namespace by using the `NS` environment variable. 
`PROS=<number_of_processes>`
    

Modify the maximum number of parallel processes that the `must-gather` tool uses. The default value is `5`. 

Important

Using too many parallel processes can cause performance issues. Increasing the maximum number of parallel processes is not recommended. 

#### 14.2.3.1.2. Scripts

Each script is compatible only with certain environment variable combinations. 

`/usr/bin/gather`
     Use the default `must-gather` script, which collects cluster data from all namespaces and includes only basic VM information. This script is compatible only with the `PROS` variable. 
`/usr/bin/gather --vms_details`
     Collect VM log files, VM definitions, control-plane logs, and namespaces that belong to OpenShift Virtualization resources. Specifying namespaces includes their child objects. If you use this parameter without specifying a namespace or VM, the `must-gather` tool collects this data for all VMs in the cluster. This script is compatible with all environment variables, but you must specify a namespace if you use the `VM` variable. 
`/usr/bin/gather --images`
     Collect image, image-stream, and image-stream-tags custom resource information. This script is compatible only with the `PROS` variable. 
`/usr/bin/gather --instancetypes`
     Collect instance types information. This information is not currently collected by default; you can, however, optionally collect it. 

#### 14.2.3.1.3. Usage and examples

You can run a script by itself or with one or more compatible environment variables. 

**must-gather syntax with optional parameters**

```shell-session
$ oc adm must-gather \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.22.9 \
  -- <environment_variable_1> <environment_variable_2> <script_name>
```


Table 14.2. Compatible parametersScript| Compatible environment variable  
---|---  
`/usr/bin/gather` |  * `PROS=<number_of_processes>`  
`/usr/bin/gather --vms_details` |  * For a namespace: `NS=<namespace_name>` * For a VM: `VM=<vm_name> NS=<namespace_name>` * `PROS=<number_of_processes>`  
`/usr/bin/gather --images` |  * `PROS=<number_of_processes>`  
Show more

## 14.2.4. Generate a VM memory dump

When a virtual machine (VM) terminates unexpectedly, you can run the `virtctl memory-dump` command to output a VM memory dump and save it on a persistent volume claim (PVC). Afterward, you can analyze the memory dump to diagnose and troubleshoot issues on the VM. 

**Procedure**

  1. Optional: You have an existing PVC on which you want to save the memory dump. 

     * The PVC volume mode must be `FileSystem`. 
     * The PVC must be large enough to contain the memory dump. 

The formula for calculating the PVC size is `(VMMemorySize + 100Mi) * (1 + FileSystemOverhead)`, where `100Mi` is the memory dump overhead, and `FileSystemOverhead` is defined in the `HCO` object. 

  2. Create a memory dump of the required VM: 

     * If you have an existing PVC selected on which you want to save the memory dump: 

```shell-session
$ virtctl memory-dump get <vm_name> --claim-name=<pvc_name>
```


     * If you want to create a new PVC for the memory dump: 

```shell-session
$ virtctl memory-dump get <vm_name> --claim-name=<new_pvc_name> --create-claim
```


  3. Download the memory dump: 

```shell-session
$ virtctl memory-dump download <vm_name> --output=<output_file>
```


  4. Attach the memory dump to a Red Hat Support case. 

Alternatively, you can inspect the memory dump, for example by using the volatility3 tool. 

  5. Optional: Remove the memory dump: 

```shell-session
$ virtctl memory-dump remove <vm_name>
```


## 14.2.5. Self-service Technical Supportability Review

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices. 

Note

The `must-gather` tool collects diagnostic information about your cluster, including resource definitions, service logs, and configuration data. For more information, see "Gathering data about your cluster" in the OpenShift Container Platform documentation. 

The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary of recommendations. This serves as a starting point to help you identify and resolve potential issues before they impact your environment. 

The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization. Coverage is continually expanding. 

### 14.2.5.1. When to use the self-service TSR tool

Integrating the self-service TSR into your regular operational workflow can be helpful in the following scenarios: 

Routine benchmarking
     Use the TSR quarterly to benchmark cluster health and plan for routine maintenance activities. 
Pre-flight checks
     Validate your cluster configuration before major structural changes, including upgrades, migrations, and expansions. 
Critical event preparation
     Confirm cluster stability ahead of high-traffic business events, such as seasonal peaks, or operational milestones, such as year-end shutdowns, business continuity drills, and compliance audits. 

### 14.2.5.2. How to access the TSR

To run a self-service review, upload your cluster’s `must-gather` data to the **Analyze** tab in the **Support** section of the Red Hat Customer Portal. For a direct link, see "Technical Supportability Review with AI tool" in the Additional resources section. The **Analyze** feature generates a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. Review the recommendations and implement the suggested corrective actions to address the identified risks. 

The self-service TSR provides a solid baseline for cluster health. If you need additional guidance or a more comprehensive review, contact your Red Hat account team to arrange an assisted review through a Technical Account Manager (TAM) or Red Hat consultant. An assisted review includes human analysis, deeper coverage, and access to checks that are updated more frequently than the self-service version. 

### 14.2.5.3. Additional resources

  * [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze)
  * [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255)



## 14.2.6. Additional resources

  * [VM support overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/support#virt-support-overview "14.1. Support overview")
  * [How to provide log files to Red Hat Support (Red Hat Knowledgebase)](https://access.redhat.com/solutions/2112)
  * [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring)
  * [Install the QEMU guest agent on a Linux VM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-installing-qemu-guest-agent-on-linux-vm_virt-installing-qemu-guest-agent "8.2.1. Install the QEMU guest agent on a Linux VM")
  * [Install VirtIO drivers from a SATA CD on an existing VM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-installing-virtio-drivers-existing-windows_virt-install-virtio-drivers-on-windows-vms "8.3.6. Install VirtIO drivers from a SATA CD on an existing VM")
  * [Connect to the desktop viewer by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-connecting-desktop-viewer-web_virt-accessing-vm-consoles "8.5.9. Connect to the desktop viewer by using the web console")
  * [Generate a VM memory dump](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/support#virt-generating-a-vm-memory-dump_virt-collecting-virt-data "14.2.4. Generate a VM memory dump")
  * [Submitting a support case](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#support-submitting-a-case_getting-support)
  * [Modifying retention time and size for Prometheus metrics data](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_user_workload_monitoring/storing-and-recording-data-uwm#modifying-retention-time-and-size-for-prometheus-metrics-data_storing-and-recording-data-uwm)
  * [Configuring the Alertmanager to capture relevant alerts and to send alert notifications to a dedicated mailbox](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_user_workload_monitoring/storing-and-recording-data-uwm#modifying-retention-time-and-size-for-prometheus-metrics-data_storing-and-recording-data-uwm)
  * [Modifying retention time and size for Prometheus metrics data](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_core_platform_monitoring/storing-and-recording-data#modifying-retention-time-and-size-for-prometheus-metrics-data_storing-and-recording-data)
  * [Configuring alerts and notifications](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_core_platform_monitoring/configuring-alerts-and-notifications)
  * [Downloading log files and diagnostic information](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/latest/html-single/troubleshooting_openshift_data_foundation/index#downloading-log-files-and-diagnostic-information_rhodf)
  * [Querying metrics for all projects with the monitoring dashboard](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/accessing_metrics/accessing-metrics-as-an-administrator#querying-metrics-for-all-projects-with-mon-dashboard_accessing-metrics-as-an-administrator)
  * [Installing the latest VirtIO drivers](https://access.redhat.com/solutions/6957701)
  * [Volatility3 tool](https://github.com/volatilityfoundation/volatility3)
  * [Customer Support](https://access.redhat.com/support/cases/#/case/list)
  * [Create issue](https://redhat.atlassian.net/secure/CreateIssue.jspa)
