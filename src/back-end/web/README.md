# Getting started
in local environment

## Prerequisite
### Create a environment file
[About Format](ENV_FILE_FORMAT.md)
File must be in `[repository path]/src/back-end/environment/.env.local`

### Install docker
[Download and Install docker](https://docs.docker.com/get-started/#download-and-install-docker) according to your operating system.

---

## How to run

### Change working directory
to back-end ROOT directory
```shell
$ cd [repository path]/src/back-end
```

### Run containers
Build, (re)create, start, attach, and run containers for the back-end server.
```shell
$ docker-compose -f docker-compose-local.yml --env-file environment/...env.local up --build
```

cf) Run in the background: add `-d` option
```shell
$ docker-compose -f docker-compose-local.yml --env-file environment/...env.local up -d --build
```
