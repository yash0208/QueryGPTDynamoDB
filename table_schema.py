import boto3
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

# Initialize DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION")
)

def infer_attribute_schema(table_name, sample_limit=100):
    table = dynamodb.Table(table_name)
    response = table.scan(Limit=sample_limit)

    attribute_types = defaultdict(set)

    for item in response.get('Items', []):
        for attr, value in item.items():
            attribute_types[attr].add(type(value).__name__)

    print(f"\n📋 Inferred schema from sample ({len(response['Items'])} items):\n")
    for attr, types in attribute_types.items():
        print(f" - {attr}: {', '.join(sorted(types))}")

    return attribute_types

# Call it on your table
schema = infer_attribute_schema("companies_data")
