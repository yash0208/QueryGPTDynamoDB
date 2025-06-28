import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize DynamoDB client
dynamodb = boto3.client(
    'dynamodb',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION")
)

def list_all_tables():
    table_names = []
    response = dynamodb.list_tables()

    table_names.extend(response.get('TableNames', []))

    # If there are more tables (pagination)
    while 'LastEvaluatedTableName' in response:
        response = dynamodb.list_tables(ExclusiveStartTableName=response['LastEvaluatedTableName'])
        table_names.extend(response.get('TableNames', []))

    print("DynamoDB Tables in your account:")
    for name in table_names:
        print(f" - {name}")

    return table_names

# List them
all_tables = list_all_tables()
