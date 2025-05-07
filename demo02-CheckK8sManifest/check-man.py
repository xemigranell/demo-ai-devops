import openai
import os
import argparse
import logging

def load_api_key():
    """
    Load OpenAI API key from environment variable.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY environment variable not set.")
        raise ValueError("OpenAI API key is missing. Set the 'OPENAI_API_KEY' environment variable.")
    return api_key

def validate_kubernetes_manifest(manifest_path, model):
    openai.api_key = load_api_key()

    logging.info("Sending request to OpenAI API...")
    try:
        # Read the existing manifest file
        with open(manifest_path, "r") as file:
            manifest_content = file.read()
        
        # Send the manifest for validation
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": """You are a Kubernetes Manifest validation expert. 
                You will receive a Kubernetes manifest in YAML format. Validate it for correctness and only reply with "The manifest is valid" if it is valid or "The manifest is not valid" if it is invalid."""},
                {"role": "user", "content": manifest_content}
            ]
        )
        
        # Extract and print the validation result
        #validation_result = response.choices[0].message.content
        #print(validation_result)
        validation_result = response.choices[0].message.content.strip()
        print(f"::set-output name=validation_result::{validation_result}")
        return validation_result
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to handle command-line arguments and run the automation.
    """
    parser = argparse.ArgumentParser(description="Validate Kubernetes manisfest using OpenAI GPT.")
    parser.add_argument(
        "-f", "--file", type=str, required=True, help="Specification for the Kubernetes manifest file."
    )
    parser.add_argument(
        "-m", "--model", type=str, default="gpt-4o-mini", help="OpenAI model to use (default: gpt-4o-mini)."
    )
    args = parser.parse_args()

    # Generate Terraform configuration
    validate_kubernetes_manifest(manifest_path=args.file, model=args.model)

if __name__ == "__main__":
    main()