# DevOps Automation with AI

This repository contains a series of demos showcasing the use of AI in DevOps tasks using Python and OpenAI libraries. Each demo demonstrates a specific use case where AI can enhance and automate DevOps processes.

## Setup

### Necessity of an OpenAI API Key

To leverage the powerful capabilities of OpenAI's models in your DevOps applications, you need an OpenAI API key. This key is essential for authenticating your requests to OpenAI's API, allowing you to access various AI functionalities such as natural language processing, code generation, and more. Without an API key, you won't be able to interact with OpenAI's services.

### How to Get an OpenAI API Key

1. **Sign Up or Log In**: Go to [OpenAI's Platform](https://platform.openai.com/) and sign up for a new account or log in using your existing credentials.
2. **Navigate to API Keys**: Once logged in, click on your profile icon at the top-right corner of the page and select "View API Keys".
3. **Create a New API Key**: Click on "Create new secret key" to generate a new API key. Make sure to copy and store this key securely, as you won't be able to view it again once the window is closed.
4. **Set Up Billing**: OPTIONAL: If you haven't already, you may need to set up billing information to continue using the API after any free credits are exhausted.

Remember to keep your API key secure and never share it publicly or include it directly in your codebase. Instead, use environment variables or a secure vault to manage your keys.

### Steps

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
