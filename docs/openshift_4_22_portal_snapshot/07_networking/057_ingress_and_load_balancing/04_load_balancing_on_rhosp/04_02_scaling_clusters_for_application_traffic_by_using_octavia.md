# 4.2. Scaling clusters for application traffic by using Octavia

To distribute traffic across multiple virtual machines (VMs), configure your cluster that runs on Red Hat OpenStack Platform (RHOSP) to use the Octavia load balancing service. By using this feature, you can mitigate the bottleneck that single machines or addresses create. 

You must create your own Octavia load balancer to use it for application network scaling. 

## 4.2.1. Scaling clusters by using Octavia

If you want to use multiple API load balancers, create an Octavia load balancer and then configure your cluster to use it. 

**Prerequisites**

  * Octavia is available on your Red Hat OpenStack Platform (RHOSP) deployment. 



**Procedure**

  1. From the command-line interface (CLI), create an Octavia load balancer that uses the Amphora driver: 

```shell-session
$ openstack loadbalancer create --name API_OCP_CLUSTER --vip-subnet-id <id_of_worker_vms_subnet>
```


You can use a name of your choice instead of `API_OCP_CLUSTER`. 

  2. After the load balancer becomes active, create listeners: 

```shell-session
$ openstack loadbalancer listener create --name API_OCP_CLUSTER_6443 --protocol HTTPS--protocol-port 6443 API_OCP_CLUSTER
```


Note

To view the status of the load balancer, enter `openstack loadbalancer list`. 

  3. Create a pool that uses the round-robin algorithm and has session persistence enabled: 

```shell-session
$ openstack loadbalancer pool create --name API_OCP_CLUSTER_pool_6443 --lb-algorithm ROUND_ROBIN --session-persistence type=<source_IP_address> --listener API_OCP_CLUSTER_6443 --protocol HTTPS
```


  4. To ensure that control-plane machines are available, create a health monitor: 

```shell-session
$ openstack loadbalancer healthmonitor create --delay 5 --max-retries 4 --timeout 10 --type TCP API_OCP_CLUSTER_pool_6443
```


  5. Add the control plane machines as members of the load balancer pool: 

```shell-session
$ for SERVER in $(MASTER-0-IP MASTER-1-IP MASTER-2-IP)
do
  openstack loadbalancer member create --address $SERVER  --protocol-port 6443 API_OCP_CLUSTER_pool_6443
done
```


  6. Optional: To reuse the cluster API floating IP address, unset it: 

```shell-session
$ openstack floating ip unset $API_FIP
```


  7. Add either the unset `API_FIP` or a new address to the created load balancer VIP: 

```shell-session
$ openstack floating ip set  --port $(openstack loadbalancer show -c <vip_port_id> -f value API_OCP_CLUSTER) $API_FIP
```


Your cluster now uses Octavia for load balancing.
