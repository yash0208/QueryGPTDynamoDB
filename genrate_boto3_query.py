import os
import boto3
import openai
from dotenv import load_dotenv
from collections import defaultdict

from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_boto3_query_code(user_query, table_name, attributes):
    """
    Uses OpenAI GPT to generate boto3 Python code for querying DynamoDB
    based on the user_query and table schema.
    """
    system_prompt = f"""
You are a helpful Python assistant.
Your task is to generate Python code using boto3 to query a DynamoDB table based on the user's request.

Only generate code that:
- Uses boto3
- Uses either `scan()` with FilterExpression, or `query()` if a partition key is clearly involved
- Uses attributes from this table only
- Does not include explanations, comments, or extra text
- Is wrapped in a markdown Python code block like this:

```python
# your code here
Table name: {table_name}
Available attributes: {', '.join(attributes)}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    raw_content = response.choices[0].message.content
    return extract_python_code(raw_content)

def extract_python_code(text):
    """
    Extracts Python code from a markdown code block.
    """
    if "```python" in text:
        return text.split("```python")[1].split("```")[0].strip()
    elif "```" in text:
        return text.split("```")[1].split("```")[0].strip()
    return text.strip()