file_path = r'D:\All Documents\Resume and interview preparation\GitHub\Python Scripting\Test-Files\example.txt'

# Read lines into a list
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes trailing newline
