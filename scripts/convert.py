import os
import sys
import anthropic

def convert_oracle_to_sql(oracle_script, api_key):
    client = anthropic.Client(api_key)
    prompt = f"""
    Convert this Oracle SQL script to SQL Server syntax.
    - SYSDATE to GETDATE()
    - NUMBER to INT or DECIMAL
    - VARCHAR2 to VARCHAR
    - NVL to ISNULL
    - Only provide the converted SQL code without explanations

    Oracle Script:
    {oracle_script}
    """
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1500,
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    api_key = os.getenv('CLAUDE_API_KEY')
    if not api_key:
        print("CLAUDE_API_KEY environment variable not set")
        sys.exit(1)
    with open(input_file, 'r') as f:
        oracle_script = f.read()
    sql_script = convert_oracle_to_sql(oracle_script, api_key)
    with open(output_file, 'w') as f:
        f.write(sql_script)
    print(f"Converted script saved to {output_file}")

if __name__ == "__main__":
    main()
