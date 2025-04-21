import os
import sys
import anthropic
from anthropic import Anthropic

def convert_oracle_to_sql(oracle_script, api_key):
    """Convert Oracle script to SQL Server using Claude API"""
    # Create Anthropic client with the correct initialization
    client = Anthropic(api_key=api_key)

    prompt = f"""
    Convert this Oracle SQL script to SQL Server syntax.
    Make these specific conversions:
    - SYSDATE to GETDATE()
    - NUMBER to INT or DECIMAL
    - VARCHAR2 to VARCHAR
    - NVL to ISNULL
    - Only provide the converted SQL code without explanations

    Oracle Script:
    {oracle_script}
    """

    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1500,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.content
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return None

def main():
    # Get paths from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Get API key from environment
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    # Read input file
    try:
        with open(input_file, 'r') as f:
            oracle_script = f.read()
    except Exception as e:
        print(f"Error reading input file: {str(e)}")
        sys.exit(1)

    # Convert script
    sql_script = convert_oracle_to_sql(oracle_script, api_key)
    if not sql_script:
        print("Conversion failed")
        sys.exit(1)

    # Write output file
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(sql_script)
        print(f"Converted script saved to {output_file}")
    except Exception as e:
        print(f"Error writing output file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
