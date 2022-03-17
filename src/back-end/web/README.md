# Back-end API Server

## Prerequisite

### Create a virtual environment
```shell
$ python -m venv env
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
