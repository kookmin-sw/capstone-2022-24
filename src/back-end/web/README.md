
## Prerequisite

### Install python
Requires Python Version `3.9.10`

### Create a virtual environment
```shell
$ python3.9 -m venv env
```

#### In window
Case 1. CMD
```shell
& python -m venv env
```
Case 2. Windows PowerShell
```shell
& python -m venv env
```


### Activate the virtual environment
```shell
$ source env/bin/activate
```
cf) deactivate: `$ deactivate`

#### In window
Case 1. CMD
```shell
& .\env\Scripts\activate.bat
```
Case 2. Windows PowerShell
```shell
& .\env\Scripts\Activate.ps1
```
cf1) If the ps1 file does not run, run PowerShell administrator mode : `& Set-ExecutionPolicy RemoteSigned`

cf2) deactivate: `$ deactivate`


### Install dependent modules
Change working directory to `web`
```shell
$ cd [repository path]/src/back-end/web
```

Install dependencies
```shell
$ pip install -r requirements.txt
```

### Set up github hook scripts
When you clone this repository, run **only for the first time**
```shell
$ pre-commit install
```

### Create a environment file
[About Format](ENV_FILE_FORMAT.md)
File must be in `src/back-end/environment/.env.local`

### Install docker
[Download and Install docker](https://docs.docker.com/get-started/#download-and-install-docker) according to your operating system.

---

## How to run

### Change working directory
```shell
$ cd [repository path]/src/back-end
```

### Run containers
Builds, (re)creates, starts, and attaches to containers for the back-end server.
```shell
$ docker-compose -f docker-compose-local.yml --env-file environment/.env.local up --build
```

### cf) Run containers in the background: use `-d` option
```shell
$ docker-compose -f docker-compose-local.yml --env-file environment/.env.local up -d --build
```


---
---
---

## Precautions

### If dependency is added,
```shell
$ pip freeze > requirements.txt
```
And don't forget to commit the file(`requirements.txt`)!
