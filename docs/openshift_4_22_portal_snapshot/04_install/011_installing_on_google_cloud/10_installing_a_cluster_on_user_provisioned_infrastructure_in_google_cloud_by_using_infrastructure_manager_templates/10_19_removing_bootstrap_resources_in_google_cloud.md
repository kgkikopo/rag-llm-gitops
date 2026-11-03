# 10.19. Removing bootstrap resources in Google Cloud

After the bootstrap process completes on your Google Cloud infrastructure, you can remove the bootstrap resources to reclaim the capacity that they consume, because the cluster no longer requires them. 

**Prerequisites**

  * Ensure you defined the variables in the _Exporting common variables_ and _Creating load balancers in Google Cloud_ sections. 
  * Create the bootstrap machine. 
  * Create the control plane machines. 



**Procedure**

  1. Change to the directory that includes the installation program and run the following command: 

```shell-session
$ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \
    --log-level info
```


where: 

`<installation_directory>`
     Specifies the path to the directory where you stored the installation files. 
`--log-level`
     Specifies the log level. To view different installation details, specify `warn`, `debug`, or `error` instead of `info`. 

If the command exits without a `FATAL` warning, your production control plane has initialized. 

  2. To remove the bootstrap instance group from the backend services' backends, run the following commands: 

```shell-session
$ gcloud compute backend-services remove-backend ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
```


```shell-session
$ ingress_backendservice=$(gcloud compute backend-services list --filter="backends.group~${INFRA_ID}" --format='value(name)' | grep -v "${INFRA_ID}")
```


     1. If `ingress_backendservice` is not empty, run the following `describe` command for the bootstrap group: 

```shell-session
$ gcloud compute backend-services describe ${ingress_backendservice} --region=${REGION}
```


     2. If the `describe` command displays that the bootstrap group is one of its backends, run the following `remove-backend` command to remove the bootstrap group from the backends: 

```shell-session
$ gcloud compute backend-services remove-backend ${ingress_backendservice} --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
```


     3. To remove the bucket and the deployment, run the following commands: 

```shell-session
$ gcloud storage rm "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign"
```


```shell-session
$ gcloud storage rm --recursive "gs://${INFRA_ID}-bootstrap-ignition/"
```


```shell-session
$ gcloud infra-manager deployments delete <bootstrap_deployment_name> \
    --project=${PROJECT_NAME} --location=${REGION} --quiet
```


Specify the name of the bootstrap deployment you created for `<bootstrap_deployment_name>`.
