# QueryGPTDynamoDB

A Python application that allows you to query DynamoDB tables using natural language. This tool leverages OpenAI's GPT-4 to automatically generate and execute boto3 DynamoDB queries based on your plain English descriptions.

## Overview

QueryGPTDynamoDB bridges the gap between natural language and DynamoDB queries by:

1. **Automatically discovering** all DynamoDB tables in your AWS account
2. **Inferring table schemas** by analyzing sample data from each table
3. **Intelligently selecting** the most relevant table for your query using GPT-4
4. **Generating optimized boto3 code** for your specific query requirements
5. **Safely executing** the generated queries and returning results

## Features

- **Natural Language Interface**: Query your DynamoDB tables using plain English
- **Automatic Table Selection**: GPT-4 intelligently chooses the most relevant table for your query
- **Schema Inference**: Automatically discovers table structure and data types
- **Safe Code Execution**: Generated boto3 code runs in a controlled environment
- **Support for Complex Queries**: Handles both scan operations with filters and query operations with partition keys
- **Real-time Results**: Execute queries immediately and see results

## Prerequisites

- Python 3.7 or higher
- AWS account with DynamoDB tables
- OpenAI API key
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd QueryGPTDynamoDB
```

2. Install required dependencies:
```bash
pip install boto3 openai python-dotenv
```

3. Create a `.env` file in the project root with your credentials:
```
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=your_aws_region
OPENAI_API_KEY=your_openai_api_key
```

## Usage

Run the main application:
```bash
python app.py
```

The application will guide you through the following steps:

1. **Enter your query**: Type your natural language query (e.g., "Find all users with age greater than 25")
2. **Table discovery**: The app will scan your AWS account for DynamoDB tables
3. **Schema analysis**: Each table's structure will be analyzed to understand available attributes
4. **Table selection**: GPT-4 will choose the most relevant table for your query
5. **Code generation**: GPT-4 will generate appropriate boto3 code for your query
6. **Query execution**: The generated code will be executed and results displayed

## Example Queries

- "Find all products with price less than $100"
- "Get users who registered after January 2023"
- "Show me all orders with status 'pending'"
- "Find customers in California with premium membership"

## Project Structure

- `app.py`: Main application entry point
- `choose_relevant_table.py`: Uses GPT-4 to select the most relevant table for a query
- `genrate_boto3_query.py`: Generates boto3 DynamoDB query code using GPT-4
- `get_relevent_schema.py`: Orchestrates table discovery and schema inference
- `table_schema.py`: Infers table schemas by analyzing sample data
- `tables_finder.py`: Discovers all DynamoDB tables in your AWS account
- `exec_genrated_code.py`: Safely executes generated boto3 code

## How It Works

1. **Table Discovery**: The application lists all DynamoDB tables in your AWS account
2. **Schema Inference**: For each table, it samples data to understand the structure and data types
3. **Query Processing**: Your natural language query is analyzed by GPT-4
4. **Table Selection**: GPT-4 compares your query against available table schemas to find the best match
5. **Code Generation**: GPT-4 generates appropriate boto3 code based on the selected table and query
6. **Safe Execution**: The generated code runs in a controlled environment with pre-bound variables
7. **Result Display**: Query results are formatted and displayed

## Security Considerations

- AWS credentials are loaded from environment variables
- Generated code runs in a sandboxed environment
- Only boto3 operations are allowed in generated code
- No arbitrary code execution is permitted

## Limitations

- Requires OpenAI API access and credits
- Query performance depends on table size and complexity
- Complex joins across multiple tables are not supported
- Generated queries may not always be optimal for large datasets

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
