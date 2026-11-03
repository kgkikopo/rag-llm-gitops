# Chapter 7. Understanding OpenShift Container Platform development

To fully use the capability of containers when developing and running enterprise-quality applications, ensure your environment is supported by tools that provide key operational characteristics. 

These container characteristics tools allow containers to have following characteristics: 

  * Created as discrete microservices that can be connected to other containerized, and non-containerized, services. For example, you might want to join your application with a database or attach a monitoring application to your application. 
  * Resilient, so if a server crashes or needs to go down for maintenance or to be decommissioned, containers can start on another machine. 
  * Automated to pick up code changes automatically and then start and deploy new versions of themselves. 
  * Scaled up, or replicated, to have more instances serving clients as demand increases and then spun down to fewer instances as demand declines. 
  * Run in different ways, depending on the type of application. For example, one application might run once a month to produce a report and then exit. Another application might need to run constantly and be highly available to clients. 
  * Managed so you can watch the state of your application and react when something goes wrong. 



As containers became widely adopted, the need for enterprise-ready tools led to a variety of management options. 

The section explains options for assets you can create when you build and deploy containerized Kubernetes applications in OpenShift Container Platform. The section also describes which approaches you might use for different kinds of applications and development requirements.

- [7.1. Containerized application development](07_01_containerized_application_development.md)
- [7.2. Simple container build process](07_02_simple_container_build_process.md)
- [7.3. Operators development](07_03_operators_development.md)
