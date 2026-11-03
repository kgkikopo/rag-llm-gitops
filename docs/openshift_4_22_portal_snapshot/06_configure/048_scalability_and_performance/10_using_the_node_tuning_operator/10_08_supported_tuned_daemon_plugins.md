# 10.8. Supported TuneD daemon plugins

Excluding the `[main]` section, the following TuneD plugins are supported when using custom profiles defined in the `profile:` section of the Tuned CR: 

  * audio 
  * cpu 
  * disk 
  * eeepc_she 
  * modules 
  * mounts 
  * net 
  * scheduler 
  * scsi_host 
  * selinux 
  * sysctl 
  * sysfs 
  * usb 
  * video 
  * vm 
  * bootloader 



There is some dynamic tuning functionality provided by some of these plugins that is not supported. The following TuneD plugins are currently not supported: 

  * script 
  * systemd 



Note

The TuneD bootloader plugin only supports Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. 

**Additional resources**

  * [Available TuneD Plugins](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/customizing-tuned-profiles_monitoring-and-managing-system-status-and-performance#available-tuned-plug-ins_customizing-tuned-profiles)
  * [Getting Started with TuneD](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/getting-started-with-tuned_monitoring-and-managing-system-status-and-performance)
