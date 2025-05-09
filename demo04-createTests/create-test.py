import openai
import os
import argparse
import logging
from openai.types.chat.chat_completion import ChatCompletion

def load_api_key():
    """
    Load OpenAI API key from environment variable.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY environment variable not set.")
        raise ValueError("OpenAI API key is missing. Set the 'OPENAI_API_KEY' environment variable.")
    return api_key

def generate_api_tests(api_spec_file, output_file, model):
    """
    Generating API tester using OpenAI's API.
    """

    openai.api_key = load_api_key()

    logging.info("Sending request to OpenAI API...")
    try:
        # Read API specifications
        with open(api_spec_file, "r") as file:
            api_spec = file.read()
        response: ChatCompletion = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": """You are pytest generator that gets specifications input and replies with only the pytest code.
                 Do not wrap the code in backticks or any other formatting. Do not include Markdown, explanations, 
                 or commentary—only the raw tf code."""},
                {"role": "user", "content": f"""
                 Generate a pytest-compatible Python script to test the following API server.
                 Ensure the tests include:
                 - Validation of status codes.
                 - Checks for expected response data.
                 - Parameterized tests for dynamic endpoints.
                 API Specifications:
                 {api_spec}
                 """}
            ]
        )
        
        # Extract the test code
        test_code = response.choices[0].message.content if response.choices[0].message.content else ""
        # Save the test code to a file
        with open(output_file, "w") as file:
            file.write(test_code)        
        print(f"API tests saved to {output_file}.")
        logging.info(f"Generated: {output_file} successfully.")
    
    except Exception as e:
        logging.error(f"Error generating API tests: {e}")
        raise

def main():
    """
    Main function to handle command-line arguments and run the automation.
    """
    parser = argparse.ArgumentParser(description="Generate incident reports using OpenAI GPT.")
    parser.add_argument(
        "-f", "--file", type=str, required=True, help="Specification for the incident details file."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="test_api_server.py", help="Specification for directory to save generated documents (default: test_api_server.py)."
    )
    parser.add_argument(
        "-m", "--model", type=str, default="gpt-4o-mini", help="OpenAI model to use (default: gpt-4o-mini)."
    )
    args = parser.parse_args()

    # Generate Terraform configuration
    generate_api_tests(api_spec_file=args.file, output_file=args.output, model=args.model)

if __name__ == "__main__":
    main()