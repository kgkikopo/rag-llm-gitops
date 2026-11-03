# 3.7. Dependency

An Operator may have a _dependency_ on another Operator being present in the cluster. For example, the Vault Operator has a dependency on the etcd Operator for its data persistence layer. 

OLM resolves dependencies by ensuring that all specified versions of Operators and CRDs are installed on the cluster during the installation phase. This dependency is resolved by finding and installing an Operator in a catalog that satisfies the required CRD API, and is not related to packages or bundles.
