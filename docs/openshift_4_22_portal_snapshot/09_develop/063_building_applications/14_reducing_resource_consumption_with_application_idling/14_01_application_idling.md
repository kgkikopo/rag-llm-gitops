# 14.1. Application idling

Identify the scalable resources for one or more services, such as deployment configurations and replication controllers, and scale them down to zero replicas to optimize cluster capacity. 

You can use the `oc idle` command to idle a single service, or use the `--resource-names-file` option to idle multiple services. 

## 14.1.1. Idling a single service

Scale down the scalable resources of a specific service to zero replicas to reduce cluster consumption. 

**Procedure**

  1. To idle a single service, run: 

```shell-session
$ oc idle <service>
```


## 14.1.2. Idling multiple services

Scale multiple inactive services down to zero replicas to optimize cluster capacity. 

Idling multiple services is helpful if an application spans across a set of services within a project, or when idling multiple services in conjunction with a script to idle multiple applications in bulk within the same project. 

**Procedure**

  1. Create a file containing a list of the services, each on their own line. 
  2. Idle the services using the `--resource-names-file` option: 

```shell-session
$ oc idle --resource-names-file <filename>
```


Note

The `idle` command is limited to a single project. For idling applications across a cluster, run the `idle` command for each project individually.
