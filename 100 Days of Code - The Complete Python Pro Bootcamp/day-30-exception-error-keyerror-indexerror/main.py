# file not found

try:
    file = open("afile.txt")
    dic = {"key": "value"}
    print(dic["key"])

except FileNotFoundError:
    file = open("afile.txt",mode="w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    # file.close()
    # print("file was closed")
    # raise TypeError("This is an error that i made up.")
    pass


height = float(input("height: "))
weight = float(input("weight: "))


if height > 3:
    raise ValueError("Human height should not be over 3m")
bmi = weight / height **2
print(bmi)