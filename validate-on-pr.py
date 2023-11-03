import json
import jsonschema
import sys
import os

# Function to validate a single JSON file against the provided schema


def validate_json(file_path, schema_data):
    try:
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

        jsonschema.validate(instance=json_data, schema=schema_data)
        print(f"{file_path} is valid.")
        return True
    except jsonschema.exceptions.ValidationError as ve:
        print(f"{file_path} is invalid: {ve}")
        return False
    except Exception as e:
        print(f"An error occurred with {file_path}: {e}")
        return False

# Main function to orchestrate the validation


def main(schema_file, files_to_check):
    # Load the schema data once
    with open(schema_file, 'r') as schema:
        schema_data = json.load(schema)

    all_files_valid = True

    # Validate each file
    for file_path in files_to_check:
        if not validate_json(file_path, schema_data):
            all_files_valid = False

    return all_files_valid


if __name__ == "__main__":
    # Exit if no files were passed to the script
    if len(sys.argv) < 3:
        print("Usage: python validate_json.py <schema_file> <file_to_validate> ...")
        sys.exit(1)

    schema_file_arg = sys.argv[1]
    files_to_validate = sys.argv[2:]

    if not main(schema_file_arg, files_to_validate):
        sys.exit(1)
