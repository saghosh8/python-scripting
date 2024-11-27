# Specify the path where you want to create the file
file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Scripting\Test-Files\example.txt'

# Open the file in write mode ('w'), creating it if it doesn't exist
with open(file_path, 'w') as file:
    file.write("This is a newly created file.\n")
    file.write("You can now add more content here.")

print(f"File created at: {file_path}")
