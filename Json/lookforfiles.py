import os

def enumerate_folder(folder_path):
    try:
        if os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                print(f"Folder: {root}")
                print("Files found: \n")
                for file in files:
                    """
                    Use this if you want the paths as well
                    print(f"File: {os.path.join(root, file)}")
                    
                    """
                    print(f"[+] {file}")
        else:
            print(f"{folder_path} is not a valid directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
folder_path = str(input("Please enter your desired path to look for json: "))  # Replace with the path to your folder
enumerate_folder(folder_path)
