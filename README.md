
# Devops Interview

Before starting please create a fork of this repo in your account

## Automation pipelines
* Setup a pipeline in [Travis CI](https://docs.travis-ci.com/user/languages/python/) for this application to do the following
  - check code format using [black](https://github.com/psf/black)
  - perform static code analysis using [pylint](https://www.pylint.org/)


## Virtualization
* Dockerize this application
  - You can use [docker labs](https://labs.play-with-docker.com/) for compute
  - [Documentation](https://docs.docker.com/engine/reference/builder/)
* Write K8 manifests for deploying the dockerized app to kubernetes
  - You can use [k8s labs](https://labs.play-with-k8s.com/) for compute
  - [Documentation](https://kubernetes.io/docs/home/)


## Infrastructure As Code
* Write a terraform script to provision Linode instance
  - [Documentation](https://registry.terraform.io/providers/linode/linode/latest/docs)
* Write [ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#intro-to-playbooks) to ssh into Linode instance and do the following
    * install python
    * clone the repository and install dependencies
    * run the application


## Scripting (Python or Shell)
* Implement a simple CLI calculator
  - [Documentation](https://click.palletsprojects.com/en/8.0.x/#documentation)

```
# usage

./calculator.py --add --param 5  --param 10
./calculator.py --divide --param 15  --param 3
```

## Cloud platforms
* Lets say we want to deploy this into AWS or other cloud platform
* Provide recommendation on the following
  - What all components from the cloud provider do we need
  - How will networking work
  - How will the security be taken care of
  - Monitoring & Feedback

## Zero down time deployment
* How can we achieve zero down time deployment for this application
* what is the recommended strategy
