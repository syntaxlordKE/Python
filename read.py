# File Read & Write Challenge + Error Handling Lab

def read_and_modify_file():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, make it uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified file
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ File '{filename}' read successfully!")
        print(f"✍️ Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("⚠️ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_and_modify_file()
