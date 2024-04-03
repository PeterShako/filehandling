
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("Second line here with numbers: 12345\n")
        file.write("Third line with some special characters: @#$%\n")
        print("File created and written successfully.")
except FileNotFoundError:
    print("Error: File not found or cannot be created.")
except PermissionError:
    print("Error: Permission denied to create or write to the file.")
finally:
    print("File Creation task completed.\n")

try:
    with open("my_file.txt", 'r') as file:
        file_content = file.read()
        print("Contents of my_file.txt:")
        print(file_content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to read the file.")
finally:
    print("\nFile Reading task completed.\n")



