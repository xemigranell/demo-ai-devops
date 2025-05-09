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

def generate_incident_reports(log_file, output_dir, model):
    """
    Generating incident reports using OpenAI's API.
    """

    openai.api_key = load_api_key()

    logging.info("Sending request to OpenAI API...")
    try:
        # Read incident details
        with open(log_file, "r") as file:
            incident_details = file.read()
    
        # Define document types and prompts
        documents = {
            "summary_report.txt": f"Generate a detailed summary report for the following incident:\n{incident_details}\nInclude:\n- Summary of the issue\n- Key timelines\n- Initial actions taken\n- Current status.",
            "action_log.txt": f"Create an action log from the following incident details:\n{incident_details}\nInclude:\n- Timestamped actions taken\n- Responsible teams or individuals for each action.",
            "runbook.txt": f"Generate a runbook to handle future occurrences of a similar incident based on the following details:\n{incident_details}\nInclude:\n- Identification steps\n- Immediate remediation steps\n- Post-recovery tasks.",
            "post_mortem.txt": f"Draft a post-mortem analysis for the following incident:\n{incident_details}\nInclude:\n- Root cause analysis\n- Timeline of events\n- Impact analysis\n- Lessons learned\n- Preventive measures.",
        }

        # Generate each document using OpenAI
        for file_name, prompt in documents.items():
            response = openai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response.choices[0].message.content if response.choices[0].message.content else ""
    
            # Save the document to the output directory
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w") as file:
                file.write(content)
            print(f"Generated: {file_name}")
            logging.info(f"Generated: {file_name} successfully.")
        logging.info("Incident reports generated successfully.")
    except Exception as e:
        logging.error(f"Error generating incident reports: {e}")
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
        "-o", "--output", type=str, default="./incident_documents", help="Specification for directory to save generated documents (default: ./incident_documents)."
    )
    parser.add_argument(
        "-m", "--model", type=str, default="gpt-4o-mini", help="OpenAI model to use (default: gpt-4o-mini)."
    )
    args = parser.parse_args()

    # Generate Terraform configuration
    generate_incident_reports(log_file=args.file, output_dir=args.output, model=args.model)

if __name__ == "__main__":
    main()