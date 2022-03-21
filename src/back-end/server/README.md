# Back-end API Server

## Prerequisite

### Install python
Requires Python Version `3.9.10`


### Create a virtual environment
```shell
$ python3.9 -m venv env
```

#### In window
Case 1. Use CMD
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

#### In window
Case 1. Use CMD
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
```shell
$ pip install -r requirements.txt
```

## Precautions
### If dependency is added,
```shell
$ pip freeze > requirements.txt
```
And don't forget to commit the file(`requirements.txt`)!
