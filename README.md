# DevOps Automation with AI

This repository contains a series of demos showcasing the use of AI in DevOps tasks using Python and OpenAI libraries. Each demo demonstrates a specific use case where AI can enhance and automate DevOps processes.

## Setup

1. Clone the repository:

2. Install the required Python packages:
    ```sh
    pip install openai argparse logging
    ```

3. Set your OpenAI API key as an environment variable:
    ```sh
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

### Demo 01: Generate Terraform Files

This demo generates Terraform configuration files based on a given specification using OpenAI's GPT model.

Run the script with the required arguments:
```sh
python generate-tf.py -p "your terraform specification" -o "output-file.tf"
```

### Demo 02: Check Validity of Kubernetes Manifest

This demo validates a Kubernetes manifest in a yaml file using OpenAI's GPT model.

Run the script with the required arguments:
```sh
python check-man.py -f "manifest-to-check"
```

### Demo 03: Generate Incident Reports

This demo generates four reports (summary, actions log, runbook and post mortem) based on a given incident file using OpenAI's GPT model.

Run the script with the required arguments:
```sh
python create-report.py -f "incident_file" -o "output-directory.tf"
```

### Demo 04: Generate API Tests in Python

This demo generates pytest tests to test an API on a given api specs file using OpenAI's GPT model.

Run the script with the required arguments:
```sh
python create-test.py -f "api_spec_file" -o "api_tests.py"
```
