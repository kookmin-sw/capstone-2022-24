### Build application
FROM node:lts as build

# Set environment variables
ENV APP=/
ENV APP_BUILD=/dist
ENV MODE=dev

# Set working directory
RUN mkdir -p $APP_BUILD
WORKDIR ${APP}

# Copy package
COPY ./package.json ./package.json
COPY ./package-lock.json ./package-lock.json

# Install dependencies
RUN npm install

# Copy project
COPY . .

# Build local version
ENTRYPOINT npm run ${MODE}
