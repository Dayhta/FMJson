import json

def read_json_file(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Failed to decode JSON data in file {file_path}.")
        return None

# Example usage
file_path = "data.json"  # Replace with the path to your JSON file
json_data = read_json_file(file_path)

if json_data:
    # Do something with the JSON data
    print(json_data)
else:
    print("Failed to read JSON file.")
    