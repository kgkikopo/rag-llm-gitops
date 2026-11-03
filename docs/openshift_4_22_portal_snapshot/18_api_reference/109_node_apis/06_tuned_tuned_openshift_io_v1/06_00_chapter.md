# Chapter 6. Tuned [tuned.openshift.io/v1]

Description
     Tuned is a collection of rules that allows cluster-wide deployment of node-level sysctls and more flexibility to add custom tuning specified by user needs. These rules are translated and passed to all containerized Tuned daemons running in the cluster in the format that the daemons understand. The responsibility for applying the node-level tuning then lies with the containerized Tuned daemons. More info: <https://github.com/openshift/cluster-node-tuning-operator>
Type
     `object`

- [6.1. Specification](06_01_specification.md)
- [6.2. API endpoints](06_02_api_endpoints.md)
