# IT Document for Automated Dev Environment for atlassian webpages

## Summary

- We have developed an automation tool to reduce the local development setup time for all the developers in org `myOrg`
- We have developed a CLI `myCli` and a service `myService` in order to achieve this, we need your help to approve this request.

There are two part of my application CLI and REST service, here are the detailed information about them -

## CLI

### summary

CLI is designed to pass on the parameters (e.g. create/sync/delete) to myService.

### Codebase

codebase for this service can be found here - `<link to repo>`.

### Build

- CLI codebase can be built with cloning the source code and running `cargo build`.
- CLI is configured to be built via bitbucket pipeline build step which is invoked after each merge to dev branch.
- CLI uses `macos` runner for building the binary as end user is going to use it in their macbooks.

### Deployment
  
- CLI is a Binary deployed to Atlassian approved internal CLI management tool `atlas`.  checkout my PR for adding this to  approved plugin repo <link to atlas repo>.
- CLI codebase can be released manually with cloning the source code and running `cargo build --release`.
- CLI is configured to be deployed after merge to main via bitbucket pipeline.

### Testing

- CLI deployment is tested via making a test run on macos runner with sanity check of running with `--help` option after building

### Restriction

- Currently CLI is configured to run only for atlassian approved internal IPs.

## MyService

### Summary

- MyService is a REST api service which interacts with CLI and responds with output as success/error of that command.
- MyService creates/deletes/updates EC2 instances in AWS ABC account
- MyService once receive create call it uses it's pre

### Codebase

codebase for this service can be found here - `<link to repo>`.

### Build

- MyService codebase can be built with cloning the source code and running `cargo build` inside `myservice` folder.
- MyService is configured to be built via bitbucket pipeline build step which is invoked after each merge to dev branch.

### Deployment
  
- MyService is a http microservice deployed to Atlassian approved AWS account ABC.  checkout my PR for adding this to  approved plugin repo `<link to atlas repo>`.
- MyService is configured to be deployed after merge to main via bitbucket pipeline.

### Testing

MyService deployment is tested via making a call to `<endpoint>/healthcheck` with ensuring `200` http reposne.

### Restriction

Currently MyService is configured to run only for atlassian approved internal IPs.

### Server

MyService is using `t3.medium` aws instance type and it's security group is configured to use the VPC which is internal to Atlassian.

## How does it work all together

### Scenario -

#### CLI passes parameter `atlas magnolia create —name <instace_name>

- myService creates AWinstance by popullating the pre-defined terraform template and create EC2 instance.
- It also pulls down the latest snapshot of staging env and uses docker compose to bring up the services by checking .running the healthcheck ( admin and frontend being up).

#### CLI passes parameter `atlas magnolia sync —name <instace_name>

- myservice uses dockerfile in my local repo and builds an image, pushes to the artifactory.
- AWS instance pulls down the images and run docker compose up again.

## Why do we need this ?

- This will reduce time required of the setting up the local dev environment by 90%.
- This will help us move faster with website page approval by stakeholders.
