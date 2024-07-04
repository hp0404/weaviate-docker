# weaviate-docker

This repository provides an example setup for running the Weaviate service using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository:
    ```sh
    git clone https://github.com/hcss-utils/weaviate-docker.git
    cd weaviate-docker
    ```

2. Create a `.env` file with the following content:
    ```env
    API_KEY="test"
    ```

3. Ensure the necessary port (8006) is open in your firewall settings.

## Running the Service

Run the following command to start the service:
```sh
docker-compose up -d
```

The Chroma service will be available on port 8006 of your host machine.

## Files

- `docker-compose.yml`: Docker Compose configuration for the Chroma service.
- `.env`: Environment variables for authentication (not included in the repository, you need to create this file).
- `test_connection.py`: Script to test the connection and verify the service endpoints.
- test with `curl`: curl http://65.109.12.98:8006/v1/meta -H "Authorization: Bearer test"
