import boto3
import os


dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION")
)


def execute_generated_code(code, table_name):
    """
    Executes GPT-generated DynamoDB boto3 code in a safe context.
    The `table` variable is pre-bound to the selected table.
    Supports use of Attr/Key from boto3.dynamodb.conditions.
    """
    from boto3.dynamodb.conditions import Attr, Key

    # Provide a clean namespace for execution
    local_vars = {
        "boto3": boto3,
        "table": dynamodb.Table(table_name),
        "Attr": Attr,
        "Key": Key,
    }

    try:
        print("Executing generated query code...\n")
        exec(code, {}, local_vars)
        if 'response' in local_vars:
            return local_vars['response']
        else:
            print("No 'response' variable found in executed code.")
            return None
    except Exception as e:
        print(f"Error while executing generated code: {e}")
