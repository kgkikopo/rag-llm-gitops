# Test Cases for End-to-End Demo

- [Provisioning of GPU Node](https://github.com/validatedpatterns-sandbox/rag-llm-gitops/blob/main/GPU_provisioning.md)

  - MachineSet is created.
    - Name of the machine set `<clustername>-gpu-<AWSregion>`.
    - Machine set has taint section:

      ```yaml
      taints:
        - effect: NoSchedule
          key: odh-notebook
          value: 'true'
      ```

    - MachineSet has a label:

      ```yaml
       metadata:
         labels:
           node-role.kubernetes.io/odh-notebook: ''
      ```

    - MachineSet instance type:

      ```yaml
       providerSpec:
         value:
           instanceType: g4dn.xlarge # or g5.2xlarge
      ```

    - The nodes are provisioned with the proper label.
    - NVIDIA pods should be running on the nodes.

  - Verify Node Feature Discovery Operator is installed:
    - Select Installed Operators from the left Navigation Bar and under Projects, select All Projects. Node Feature Discovery Operator should be installed.
    - Click on the Node Feature Discovery Operator. Under NodeFeatureDiscovery an instance should be created. Status should be Available.

  - Verify NVIDIA GPU Operator is installed:
    - NVIDIA GPU Operator is installed.
    - Click on the NVIDIA GPU Operator and click on ClusterPolicy. A `gpu-cluster-policy` should exist.
    - The YAML should contain the tolerations:

      ```yaml
       tolerations:
         - effect: NoSchedule
           key: odh-notebook
           value: 'true'
      ```

- Application provisioned correctly:
  - Check the `rag-llm` namespace:
    - PGVector PostgreSQL pod is running (`pgvector-postgresql-...`).
    - Documentation population job completes successfully (`populate-vectordb-...`).
    - Assistant UI pod is running (`llm-ui-...`).
  - Check the `vllm` namespace:
    - vLLM model server pod is running with GPU allocation (`hf-text-generation-server-...`).
  - Access the UI:
    - Click on **Networking** → **Routes** in the `rag-llm` namespace. The `llm-ui` route should exist.
    - Click on the Location URL to launch the **OpenShift 4.22 Documentation Assistant**.

- Query Verification Test Cases:
  - Verify Edge Route creation:
    - Query: *"How do I expose my web application service frontend-svc on port 8080 with edge TLS termination?"*
    - Verify RAG returns OpenShift `Route` resource (`spec.tls.termination: edge`) or `oc create route edge`.
  - Verify Security Context Constraints:
    - Query: *"How do I allow a pod running under service account deploy-sa to access host path mounts or run privileged?"*
    - Verify RAG returns `oc adm policy add-scc-to-user privileged -z deploy-sa`.
  - Verify ImageStreams:
    - Query: *"How do I track and deploy container image updates automatically in a namespace?"*
    - Verify RAG returns OpenShift `ImageStream` guidance and `oc import-image`.
