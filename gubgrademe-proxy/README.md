# Gubgrademe Proxy

This is the proxy service for the Gubgrademe project. It acts as an intermediary between the client and the backend services, providing additional functionality and security. It built using Flask

## Features

- **Authentication**: The proxy service handles user authentication and authorization, ensuring that only authorized users can access the backend services.
- **Request Routing**: It routes incoming requests to the appropriate backend service based on the request path or other criteria.
- **Caching**: The proxy service can cache responses from the backend services to improve performance and reduce load on the backend.
- **Rate Limiting**: It can enforce rate limits on incoming requests to prevent abuse and ensure fair usage of the backend services.
- **Logging and Monitoring**: The proxy service logs incoming requests and responses, providing visibility into the system's behavior. It also integrates with monitoring tools to track performance and detect issues.

## Getting Started

To run the Gubgrademe Proxy locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/gubgrademe-proxy.git`

## Configuration

The proxy service can be configured using the `service-config.json` file. 

## Deployment with Docker

To deploy the Gubgrademe Proxy using Docker, follow these steps:

1. Build the Docker image using the provided Dockerfile:
    ```bash
    docker build -t gubgrademe-proxy .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8080:8080 gubgrademe-proxy
    ```

    This will start the proxy service on port 8080.

## Configuration

The proxy service can be configured using environment variables. Here are some of the available configuration options:

- `PORT`: The port on which the proxy service should listen for incoming requests.
- `BACKEND_URL`: The URL of the backend service to which requests should be forwarded.
- `AUTHENTICATION_PROVIDER`: The authentication provider to use for user authentication.
- `AUTHENTICATION_CREDENTIALS`: The credentials required for authentication.

You can set these environment variables when running the Docker container, for example:
docker run -p 8080:8080 -e PORT=8080 -e BACKEND_URL=<backend_url> -e AUTHENTICATION_PROVIDER=<authentication_provider> -e AUTHENTICATION_CREDENTIALS=<authentication_credentials> gubgrademe-proxy