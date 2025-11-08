from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    content = file.read()
    # print(content)

soup = BeautifulSoup(content, "html.parser")
# soup = BeautifulSoup(content, "lxml")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchor = soup.find_all("a")
print(soup.find_all("a"))

text = []
for tag in all_anchor:
    text.append(tag.getText())

print(text)

for tag in all_anchor:
    # text.append(tag.getText())
    print(tag.get("href"))

heading = soup.find_all(name = "h1", id = "name")
print(heading)
print(heading[0].getText())

class_heading = soup.find_all(class_ = "heading")
# needs underscore because python
print(class_heading)

company_url = soup.select_one(selector= "p a")
print(company_url)
