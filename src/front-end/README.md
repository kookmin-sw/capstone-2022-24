# Getting started

## How to run
Choose **ENV_KEYWORD** by deploy type
- `local`: local environment
- `dev`: development environment
- `prod`: production environment

### Create an environment file
> in `[repository path]/src/front-end/.env.[ENV_KEYWORD].local`

for example: local deploy -> .env.local.local


### With docker
- Install [docker](https://docs.docker.com/get-started/#download-and-install-docker)
- Change working directory
  ```shell
  cd [repository path]/src/front-end
  ```
- Run container
  ```shell
  docker-compose -f docker-compose.yml --env-file .env.[ENV_KEYWORD].local up --build -d --force-recreate
  ```


### Without docker
- Install [npm](https://nodejs.org/ko/download/)
- Install dependencies
  ```shell
  npm install
  ```

- Compiles and hot-reloads for development
  ```shell
  npm run [ENV_TYPE]
  ```


## Other setups
### Compiles and minifies for production
```shell
npm run build
```

### Run your unit tests
```shell
npm run test:unit
```

### Run your end-to-end tests
```shell
npm run test:e2e
```

### Lints and fixes files
```shell
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
