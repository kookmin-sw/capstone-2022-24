# Back-end API Server

## Prerequisite

### Install python
Requires Python Version `3.9.10`


### Create a virtual environment
```shell
$ python3.9 -m venv env
```

### Activate the virtual environment
```shell
$ source env/bin/activate
```
cf) deactivate: `$ deactivate`


### Install dependent modules
```shell
$ pip install -r requirements.txt
```

## Precautions
### If dependency is added,
```shell
$ pip freeze > requirements.txt
```
And don't forget to commit the file(`requirements.txt`)!
