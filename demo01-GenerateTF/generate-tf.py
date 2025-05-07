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

def generate_terraform_spec(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Generate Terraform configuration using OpenAI's API.
    """
    openai.api_key = load_api_key()

    logging.info("Sending request to OpenAI API...")
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": """You are a Terraform script generator that receives a specification of a terraform
                  template. Do not wrap the code in backticks or any other formatting. It needs all the components in a typical terraform main file.
                  Do not include Markdown, explanations, or commentary—only the raw tf code."""},
                {"role": "user", "content": prompt}
            ]
        )

        terraform_config = ""
        for choice in response.choices:
            if choice.message.content is not None:
                terraform_config += choice.message.content

        logging.info("Terraform configuration generated successfully.")
        return terraform_config

    except Exception as e:
        logging.error(f"Error generating Terraform configuration: {e}")
        raise

def save_to_file(content: str, output_file: str):
    """
    Save generated content to a specified file.
    """
    try:
        with open(output_file, "w") as file:
            file.write(content)
        logging.info(f"Terraform configuration saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving file {output_file}: {e}")
        raise

def main():
    """
    Main function to handle command-line arguments and run the automation.
    """
    parser = argparse.ArgumentParser(description="Generate Terraform configuration using OpenAI GPT.")
    parser.add_argument(
        "-p", "--prompt", type=str, required=True, help="Specification for the Terraform configuration."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="main.tf", help="Output file name (default: main.tf)."
    )
    parser.add_argument(
        "-m", "--model", type=str, default="gpt-4o-mini", help="OpenAI model to use (default: gpt-4o-mini)."
    )
    args = parser.parse_args()

    # Generate Terraform configuration
    terraform_config = generate_terraform_spec(prompt=args.prompt, model=args.model)

    # Save to file
    save_to_file(content=terraform_config, output_file=args.output)

if __name__ == "__main__":
    main()
