### Build application
FROM node:lts as build

# Set arguments and environment variables
ARG APP
ARG APP_BUILD
ARG APP_PORT
ENV MODE=dev

# Set working directory
RUN mkdir -p $APP_BUILD
RUN mkdir -p $APP
WORKDIR ${APP}

# Copy package
COPY package*.json .

# Install dependencies
RUN npm install

# Copy project
COPY . .

# Expose port
EXPOSE ${APP_PORT}

# Build local version
ENTRYPOINT npm run ${MODE}
