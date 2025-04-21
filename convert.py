import os
import sys
from anthropic import Anthropic

def convert_oracle_to_sql(oracle_script, api_key):
    """Convert Oracle script to SQL Server using Claude API"""
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
        # Extract the content from the response
        if isinstance(response.content, list):
            for content in response.content:
                if hasattr(content, 'type') and content.type == 'text':
                    return content.text
            return None
        else:
            return response.content
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return None

def append_readme(oracle_file, sql_file, oracle_script, sql_script):
    readme_path = os.path.join(os.path.dirname(sql_file), "README.md")
    with open(readme_path, "a") as readme:
        readme.write(f"\n## Conversion: {os.path.basename(oracle_file)} → {os.path.basename(sql_file)}\n")
        readme.write("\n**Oracle SQL:**\n")
        readme.write("```sql\n")
        readme.write(oracle_script.strip() + "\n")
        readme.write("```\n")
        readme.write("\n**SQL Server:**\n")
        readme.write("```sql\n")
        readme.write(sql_script.strip() + "\n")
        readme.write("```\n")
        readme.write("\n**Key Differences:**\n")
        readme.write("""
| Feature/Function         | Oracle SQL Example                | SQL Server Equivalent         |
|------------------------- |-----------------------------------|------------------------------|
| Date/Time Functions      | SYSDATE                           | GETDATE()                    |
| Data Types               | NUMBER, VARCHAR2                  | INT, DECIMAL, VARCHAR        |
| NULL Handling            | NVL(expr1, expr2)                 | ISNULL(expr1, expr2)         |
| String Functions         | TO_CHAR(date, format)             | CONVERT(VARCHAR, date, style)|
| Sequences                | CREATE SEQUENCE ...               | IDENTITY or SEQUENCE         |
| Triggers                 | Oracle PL/SQL trigger syntax      | SQL Server T-SQL trigger     |
| PL/SQL Blocks            | BEGIN ... END;                    | BEGIN ... END                |
| Dual Table               | FROM DUAL                         | (No equivalent needed)       |
""")
        readme.write("\n---\n")

def main():
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

        # Append to README
        append_readme(input_file, output_file, oracle_script, sql_script)

    except Exception as e:
        print(f"Error writing output file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
