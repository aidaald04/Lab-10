file_name = input("Enter the file name: ")
if "." in file_name:
    extension = file_name.split(".")[-1]
    print("File extension:", extension)
else:
    print("Error: File  cannot be determined.")
