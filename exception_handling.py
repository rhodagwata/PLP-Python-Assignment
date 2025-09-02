# Asking the user for a filename
filename = input("Enter the filename to read: ")

try:
    
    with open(filename, "r") as f:
        content = f.read()

    # Modifying the content by converting it to uppercase
    modified_content = content.upper()

    # Writing the modified content to new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as f:
        f.write(modified_content)

    print(f"File read successfully! Modified version saved as '{new_filename}'")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
