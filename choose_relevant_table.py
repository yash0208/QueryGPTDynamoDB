import os
import boto3
import openai
from dotenv import load_dotenv
from collections import defaultdict

from openai import OpenAI

# Load environment
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def choose_relevant_table(user_query, table_schemas):
    system_prompt = """
You are a helpful assistant. Your task is to choose the most relevant DynamoDB table for a given user query.
You will be provided table schemas and the query. Respond ONLY with the table name that best matches.
"""
    schema_text = "\n".join([f"{k}: {', '.join(v)}" for k, v in table_schemas.items()])
    user_prompt = f"""Table Schemas:
{schema_text}

User Query:
"{user_query}"

Respond only with the table name."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()