# Chapter 13. Pruning objects to reclaim resources

Reclaim cluster storage and optimize API server performance by pruning stale resources. You can run manual CLI commands or configure automated cron jobs to clean up obsolete deployment, build, image, and group records. 

Over time, API objects created in OpenShift Container Platform can accumulate in the cluster’s etcd data store through normal user operations, such as when building and deploying applications. 

Cluster administrators can periodically prune older versions of objects from the cluster that are no longer required. For example, by pruning images you can delete older images and layers that are no longer in use, but are still taking up disk space.

- [13.1. Basic pruning operations](13_01_basic_pruning_operations.md)
- [13.2. Pruning groups](13_02_pruning_groups.md)
- [13.3. Pruning deployment resources](13_03_pruning_deployment_resources.md)
- [13.4. Pruning builds](13_04_pruning_builds.md)
- [13.5. Automatically pruning images](13_05_automatically_pruning_images.md)
- [13.6. Manually pruning images](13_06_manually_pruning_images.md)
- [13.7. Hard pruning the registry](13_07_hard_pruning_the_registry.md)
- [13.8. Pruning cron jobs](13_08_pruning_cron_jobs.md)
