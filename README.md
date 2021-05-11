
# Devops Interview


## Virtualization
* Dockerize the application
  - https://docs.docker.com/engine/reference/builder/
* Write K8 manifests for deploying the dockerized app to kubernetes
  - https://kubernetes.io/docs/home/


## Infrastructure As Code (IAC)
* Write a terraform script to provision Linode instance
  - https://registry.terraform.io/providers/linode/linode/latest/docs
* Write ansible script to ssh into Linode instance
    * clone the repository
    * run the application


## Scripting (Python or Shell)
* Implement a simple CLI calculator

```
# usage

./calculator.py --add 5 10
./calculator.py --divide 15 3
```

## Cloud platforms
* Lets say we want to deploy this into AWS or other cloud platform
* Provide recommendation on the following
  - What all components form the cloud provider do we need
  - How will networking work
  - How will the security be taken care of
  - Monitoring