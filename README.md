# TBD To-Do App

This is a demonstration of Trunk-Based Development (TBD) principles with multiple environments (dev, staging, prod).

## Features
- Simple To-Do List App
- Feature toggles for new UI
- Multi-environment support with CI/CD

## Usage
1. Install Docker and Docker Compose.
2. Run `docker-compose --env-file .env.dev up` for the dev environment.
3. Use CI/CD pipeline for automated deployments.

## Environments
- **Dev**: http://localhost:5001
- **Staging**: http://localhost:5002
- **Prod**: http://localhost:5003
