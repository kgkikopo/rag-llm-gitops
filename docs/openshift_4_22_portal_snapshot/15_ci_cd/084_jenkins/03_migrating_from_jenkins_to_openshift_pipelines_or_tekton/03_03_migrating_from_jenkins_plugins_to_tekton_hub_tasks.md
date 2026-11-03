# 3.3. Migrating from Jenkins plugins to Tekton Hub tasks

You can extend the capability of Jenkins by using [plugins](https://plugins.jenkinsci.org). To achieve similar extensibility in OpenShift Pipelines, use any of the tasks available from [Tekton Hub](https://hub.tekton.dev). 

For example, consider the [git-clone](https://hub.tekton.dev/tekton/task/git-clone) task in Tekton Hub, which corresponds to the [git plugin](https://plugins.jenkins.io/git/) for Jenkins. 

**Example:`git-clone` task from Tekton Hub**

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
 name: demo-pipeline
spec:
 params:
   - name: repo_url
   - name: revision
 workspaces:
   - name: source
 tasks:
   - name: fetch-from-git
     taskRef:
       name: git-clone
     params:
       - name: url
         value: $(params.repo_url)
       - name: revision
         value: $(params.revision)
     workspaces:
     - name: output
       workspace: source
```
