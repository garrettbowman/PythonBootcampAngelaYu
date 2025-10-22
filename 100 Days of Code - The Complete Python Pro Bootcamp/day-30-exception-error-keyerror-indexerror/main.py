# file not found

try:
    file = open("afile.txt")
    dic = {"key": "value"}
    print(dic["erwer"])

except FileNotFoundError:
    file = open("afile.txt",mode="w")
except KeyError:
    print("That file does not exist")
