from choose_relevant_table import choose_relevant_table
from exec_genrated_code import execute_generated_code
from genrate_boto3_query import generate_boto3_query_code
from get_relevent_schema import get_table_schemas_for_prompt


def main():
    try:
        user_query = input("Enter your natural language query: ").strip()
        if not user_query:
            print("Please enter a valid query.")
            return

        print("\nStep 1: Fetching all table schemas...")
        schemas = get_table_schemas_for_prompt()
        if not schemas:
            print("No DynamoDB tables or attributes found.")
            return

        print("\nStep 2: Choosing the best matching table...")
        selected_table = choose_relevant_table(user_query, schemas)
        if selected_table not in schemas:
            print(f"GPT selected an unknown table: '{selected_table}'")
            return
        print(f"Selected Table: {selected_table}")

        print("\nStep 3: Generating DynamoDB query code with GPT...")
        code = generate_boto3_query_code(user_query, selected_table, schemas[selected_table])
        if not code:
            print("Failed to generate query code.")
            return
        print("\nGenerated Code:\n")
        print(code)

        print("\nStep 4: Executing the generated query...\n")
        response = execute_generated_code(code, selected_table)
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()