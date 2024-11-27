# Specify the path where you want to create the file
file_path = '/home/username/python_scripting_files/example.txt'  # Adjust the path as needed

# Open the file in write mode ('w'), creating it if it doesn't exist
with open(file_path, 'w') as file:
    file.write("This is a newly created file.\n")
    file.write("You can now add more content here.")

print(f"File created at: {file_path}")
