# 3.5. Self-service Technical Supportability Review

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices. 

Note

The `must-gather` tool collects diagnostic information about your cluster, including resource definitions, service logs, and configuration data. For more information, see "Gathering data about your cluster" in the OpenShift Container Platform documentation. 

The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary of recommendations. This serves as a starting point to help you identify and resolve potential issues before they impact your environment. 

The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization. Coverage is continually expanding. 

## 3.5.1. When to use the self-service TSR tool

Integrating the self-service TSR into your regular operational workflow can be helpful in the following scenarios: 

Routine benchmarking
     Use the TSR quarterly to benchmark cluster health and plan for routine maintenance activities. 
Pre-flight checks
     Validate your cluster configuration before major structural changes, including upgrades, migrations, and expansions. 
Critical event preparation
     Confirm cluster stability ahead of high-traffic business events, such as seasonal peaks, or operational milestones, such as year-end shutdowns, business continuity drills, and compliance audits. 

## 3.5.2. How to access the TSR

To run a self-service review, upload your cluster’s `must-gather` data to the **Analyze** tab in the **Support** section of the Red Hat Customer Portal. For a direct link, see "Technical Supportability Review with AI tool" in the Additional resources section. The **Analyze** feature generates a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. Review the recommendations and implement the suggested corrective actions to address the identified risks. 

The self-service TSR provides a solid baseline for cluster health. If you need additional guidance or a more comprehensive review, contact your Red Hat account team to arrange an assisted review through a Technical Account Manager (TAM) or Red Hat consultant. An assisted review includes human analysis, deeper coverage, and access to checks that are updated more frequently than the self-service version. 

## 3.5.3. Additional resources

  * [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze)
  * [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255)
