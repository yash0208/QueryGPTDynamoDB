from table_schema import infer_attribute_schema
from tables_finder import list_all_tables


def get_table_schemas_for_prompt():
    all_tables = list_all_tables()
    schema_dict = {}

    for table in all_tables:
        print(f"Scanning table: {table}")
        attrs = infer_attribute_schema(table)
        if attrs:
            schema_dict[table] = attrs

    return schema_dict