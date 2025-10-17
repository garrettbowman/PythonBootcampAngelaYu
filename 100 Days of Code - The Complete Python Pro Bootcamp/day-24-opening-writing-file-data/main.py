with open("../../../../Desktop/new_file.txt") as file:
    contents = file.read()
    file.close()
    print(contents)

with open("new_file.txt",mode="a") as file:
    file.write("abc123")
    print(contents)