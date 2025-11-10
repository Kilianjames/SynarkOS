# SynarkOS Installation Guide

<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="850"
        src="https://github.com/synarkos/synarkos/raw/master/images/synarkoslogobanner.png"
      >
    </a>
  </p>
</div>

You can install `synarkos` with pip in a
[**Python>=3.10**](https://www.python.org/) environment.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 or higher: [Download Python](https://www.python.org/)
- pip (specific version recommended): `pip >= 21.0`
- git (for cloning the repository): [Download Git](https://git-scm.com/)

## Installation Options

=== "pip (Recommended)"

    #### Simple Installation

    Simplest manner of installing synarkos leverages using PIP. For faster installs and build times, we recommend using UV

    ```bash
    pip install synarkos
    ```

=== "UV Installation"

    UV is a fast Python package installer and resolver written in Rust. It's significantly faster than pip and provides better dependency resolution.

    === "Basic Installation"

        ```bash
        # Install UV first
        curl -LsSf https://astral.sh/uv/install.sh | sh

        # Install synarkos using UV
        uv pip install synarkos
        ```

    === "Development Installation"

        ```bash
        # Clone the repository
        git clone https://github.com/synarkos/synarkos.git
        cd synarkos

        # Install in editable mode
        uv pip install -e .
        ```

        For desktop installation with extras:

        ```bash
        uv pip install -e .[desktop]
        ```

=== "Poetry Installation"

    Poetry is a modern dependency management and packaging tool for Python. It provides a more robust way to manage project dependencies and virtual environments.

    === "Basic Installation"

        ```bash
        # Install Poetry first
        curl -sSL https://install.python-poetry.org | python3 -

        # Install synarkos using Poetry
        poetry add synarkos
        ```

    === "Development Installation"

        ```bash
        # Clone the repository
        git clone https://github.com/synarkos/synarkos.git
        cd synarkos

        # Install in editable mode
        poetry install
        ```

        For desktop installation with extras:

        ```bash
        poetry install --extras "desktop"
        ```

    === "Using Poetry with existing projects"

        If you have an existing project with a `pyproject.toml` file:

        ```bash
        # Add synarkos to your project dependencies
        poetry add synarkos

        # Or add with specific extras
        poetry add "synarkos[desktop]"
        ```

=== "Development Installation"

    === "Using virtualenv"

        1. **Clone the repository and navigate to the root directory:**

            ```bash
            git clone https://github.com/synarkos/synarkos.git
            cd synarkos
            ```

        2. **Setup Python environment and activate it:**

            ```bash
            python3 -m venv venv
            source venv/bin/activate
            pip install --upgrade pip
            ```

        3. **Install SynarkOS:**

            - Headless install:

                ```bash
                pip install -e .
                ```

            - Desktop install:

                ```bash
                pip install -e .[desktop]
                ```

    === "Using Anaconda"

        1. **Create and activate an Anaconda environment:**

            ```bash
            conda create -n synarkos python=3.10
            conda activate synarkos
            ```

        2. **Clone the repository and navigate to the root directory:**

            ```bash
            git clone https://github.com/synarkos/synarkos.git
            cd synarkos
            ```

        3. **Install SynarkOS:**

            - Headless install:

                ```bash
                pip install -e .
                ```

            - Desktop install:

                ```bash
                pip install -e .[desktop]
                ```

    === "Using Poetry"

        1. **Clone the repository and navigate to the root directory:**

            ```bash
            git clone https://github.com/synarkos/synarkos.git
            cd synarkos
            ```

        2. **Setup Python environment and activate it:**

            ```bash
            poetry env use python3.10
            poetry shell
            ```

        3. **Install SynarkOS:**

            - Headless install:

                ```bash
                poetry install
                ```

            - Desktop install:

                ```bash
                poetry install --extras "desktop"
                ```

=== "Using Docker"

    Docker is an excellent option for creating isolated and reproducible environments, suitable for both development and production. Contact us if there are any issues with the docker setup

    1. **Pull the Docker image:**

        ```bash
        docker pull synarkoscorp/synarkos:tagname

        ```

    2. **Run the Docker container:**

        ```bash
        docker run -it --rm synarkoscorp/synarkos:tagname
        ```

    3. **Build and run a custom Docker image:**

        ```dockerfile
        # Use Python 3.11 instead of 3.13
        FROM python:3.11-slim

        # Set environment variables
        ENV PYTHONDONTWRITEBYTECODE=1 \
            PYTHONUNBUFFERED=1 \
            WORKSPACE_DIR="agent_workspace" \
            OPENAI_API_KEY="your_swarm_api_key_here"

        # Set the working directory
        WORKDIR /usr/src/synarkos

        # Install system dependencies
        RUN apt-get update && apt-get install -y \
            build-essential \
            gcc \
            g++ \
            gfortran \
            && rm -rf /var/lib/apt/lists/*

        # Install synarkos package
        RUN pip3 install -U swarm-models
        RUN pip3 install -U synarkos

        # Copy the application
        COPY . .
        ```

=== "Using Kubernetes"

    Kubernetes provides an automated way to deploy, scale, and manage containerized applications.

    1. **Create a Deployment YAML file:**

        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: synarkos-deployment
        spec:
          replicas: 3
          selector:
            matchLabels:
              app: synarkos
          template:
            metadata:
              labels:
                app: synarkos
            spec:
              containers:
              - name: synarkos
                image: synarkos/synarkos
                ports:
                - containerPort: 8080
        ```

    2. **Apply the Deployment:**

        ```bash
        kubectl apply -f deployment.yaml
        ```

    3. **Expose the Deployment:**

        ```bash
        kubectl expose deployment synarkos-deployment --type=LoadBalancer --name=synarkos-service
        ```

=== "CI/CD Pipelines"

    Integrating SynarkOS into your CI/CD pipeline ensures automated testing and deployment.

    #### Using GitHub Actions

    ```yaml
    # .github/workflows/ci.yml
    name: CI

    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]

    jobs:
      build:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: 3.10
        - name: Install dependencies
          run: |
            python -m venv venv
            source venv/bin/activate
            pip install --upgrade pip
            pip install -e .
        - name: Run tests
          run: |
            source venv/bin/activate
            pytest
    ```

    #### Using Jenkins

    ```groovy
    pipeline {
        agent any

        stages {
            stage('Clone repository') {
                steps {
                    git 'https://github.com/synarkos/synarkos.git'
                }
            }
            stage('Setup Python') {
                steps {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install --upgrade pip'
                }
            }
            stage('Install dependencies') {
                steps {
                    sh 'source venv/bin/activate && pip install -e .'
                }
            }
            stage('Run tests') {
                steps {
                    sh 'source venv/bin/activate && pytest'
                }
            }
        }
    }
    ```

## Rust

=== "Cargo install"

    Get started with the Rust implementation of SynarkOS. [Get started with the docs here](https://docs.synarkos.world/en/latest/synarkos_rs/overview/)

    ```bash
    cargo add synarkos-rs
    ```


