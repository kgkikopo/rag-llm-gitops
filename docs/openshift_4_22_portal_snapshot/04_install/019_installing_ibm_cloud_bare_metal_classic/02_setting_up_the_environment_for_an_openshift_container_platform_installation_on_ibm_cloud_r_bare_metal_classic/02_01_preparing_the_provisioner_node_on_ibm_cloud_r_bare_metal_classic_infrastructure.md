# 2.1. Preparing the provisioner node on IBM Cloud(R) Bare Metal (Classic) infrastructure

Before you install OpenShift Container Platform on IBM Cloud® Bare Metal (Classic) infrastructure, prepare the provisioner node by creating a non-root user, configuring network bridges, registering the node, installing required packages, and downloading the pull secret. 

**Procedure**

  1. Log in to the provisioner node via `ssh`. 
  2. Create a non-root user (`kni`) and give that user `sudo` privileges: 

```shell-session
# useradd kni
```


```shell-session
# passwd kni
```


```shell-session
# echo "kni ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/kni
```


```shell-session
# chmod 0440 /etc/sudoers.d/kni
```


  3. Create an `ssh` key for the new user: 

```shell-session
# su - kni -c "ssh-keygen -f /home/kni/.ssh/id_rsa -N ''"
```


  4. Log in as the new user on the provisioner node: 

```shell-session
# su - kni
```


  5. Use Red Hat Subscription Manager to register the provisioner node: 

```shell-session
$ sudo subscription-manager register --username=<user> --password=<pass> --auto-attach
```


```shell-session
$ sudo subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms \
                                  --enable=rhel-8-for-x86_64-baseos-rpms
```


Note

For more information about Red Hat Subscription Manager, see [Registering a RHEL system with command-line tools](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/basic-reg-rhel-cli). 

  6. Install the following packages: 

```shell-session
$ sudo dnf install -y libvirt qemu-kvm mkisofs python3-devel jq ipmitool
```


  7. Change the user to add the `libvirt` group to the newly created user: 

```shell-session
$ sudo usermod --append --groups libvirt kni
```


  8. Start `firewalld`: 

```shell-session
$ sudo systemctl start firewalld
```


  9. Enable `firewalld`: 

```shell-session
$ sudo systemctl enable firewalld
```


  10. Start the `http` service: 

```shell-session
$ sudo firewall-cmd --zone=public --add-service=http --permanent
```


```shell-session
$ sudo firewall-cmd --reload
```


  11. Start and enable the `libvirtd` service: 

```shell-session
$ sudo systemctl enable libvirtd --now
```


  12. Set the ID of the provisioner node: 

```shell-session
$ PRVN_HOST_ID=<ID>
```


You can view the ID with the following `ibmcloud` command: 

```shell-session
$ ibmcloud sl hardware list
```


  13. Set the ID of the public subnet: 

```shell-session
$ PUBLICSUBNETID=<ID>
```


You can view the ID with the following `ibmcloud` command: 

```shell-session
$ ibmcloud sl subnet list
```


  14. Set the ID of the private subnet: 

```shell-session
$ PRIVSUBNETID=<ID>
```


You can view the ID with the following `ibmcloud` command: 

```shell-session
$ ibmcloud sl subnet list
```


  15. Set the provisioner node public IP address: 

```shell-session
$ PRVN_PUB_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | jq .primaryIpAddress -r)
```


  16. Set the CIDR for the public network: 

```shell-session
$ PUBLICCIDR=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .cidr)
```


  17. Set the IP address and CIDR for the public network: 

```shell-session
$ PUB_IP_CIDR=$PRVN_PUB_IP/$PUBLICCIDR
```


  18. Set the gateway for the public network: 

```shell-session
$ PUB_GATEWAY=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .gateway -r)
```


  19. Set the private IP address of the provisioner node: 

```shell-session
$ PRVN_PRIV_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | \
                 jq .primaryBackendIpAddress -r)
```


  20. Set the CIDR for the private network: 

```shell-session
$ PRIVCIDR=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .cidr)
```


  21. Set the IP address and CIDR for the private network: 

```shell-session
$ PRIV_IP_CIDR=$PRVN_PRIV_IP/$PRIVCIDR
```


  22. Set the gateway for the private network: 

```shell-session
$ PRIV_GATEWAY=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .gateway -r)
```


  23. Set up the bridges for the `baremetal` and `provisioning` networks: 

```shell-session
$ sudo nohup bash -c "
    nmcli --get-values UUID con show | xargs -n 1 nmcli con delete
    nmcli connection add ifname provisioning type bridge con-name provisioning
    nmcli con add type bridge-slave ifname eth1 master provisioning
    nmcli connection add ifname baremetal type bridge con-name baremetal
    nmcli con add type bridge-slave ifname eth2 master baremetal
    nmcli connection modify baremetal ipv4.addresses $PUB_IP_CIDR ipv4.method manual ipv4.gateway $PUB_GATEWAY
    nmcli connection modify provisioning ipv4.addresses 172.22.0.1/24,$PRIV_IP_CIDR ipv4.method manual
    nmcli connection modify provisioning +ipv4.routes \"10.0.0.0/8 $PRIV_GATEWAY\"
    nmcli con down baremetal
    nmcli con up baremetal
    nmcli con down provisioning
    nmcli con up provisioning
    init 6
"
```


Note

For `eth1` and `eth2`, substitute the appropriate interface name, as needed. 

  24. If required, SSH back into the `provisioner` node: 

```shell-session
# ssh kni@provisioner.<cluster_name>.<domain>
```


  25. Verify the connection bridges have been properly created: 

```shell-session
$ sudo nmcli con show
```


**Example output**

```shell-session
NAME               UUID                                  TYPE      DEVICE
baremetal          4d5133a5-8351-4bb9-bfd4-3af264801530  bridge    baremetal
provisioning       43942805-017f-4d7d-a2c2-7cb3324482ed  bridge    provisioning
virbr0             d9bca40f-eee1-410b-8879-a2d4bb0465e7  bridge    virbr0
bridge-slave-eth1  76a8ed50-c7e5-4999-b4f6-6d9014dd0812  ethernet  eth1
bridge-slave-eth2  f31c3353-54b7-48de-893a-02d2b34c4736  ethernet  eth2
```


  26. Create a `pull-secret.txt` file: 

```shell-session
$ vim pull-secret.txt
```


Go to [Install on Bare Metal with user-provisioned infrastructure](https://console.redhat.com/openshift/install/metal/user-provisioned). In step 1, click **Download pull secret**. Paste the contents into the `pull-secret.txt` file and save the contents in the `kni` user’s home directory.
