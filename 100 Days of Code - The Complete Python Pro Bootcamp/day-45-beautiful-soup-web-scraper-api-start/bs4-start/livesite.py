from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
# print(soup.select_one(selector=".storylink").string)

articles = soup.find_all(name="a",class_="storylink")
print(articles)
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

print(article_texts)
print(article_links)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
highest = article_upvotes.index(max(article_upvotes))
print(highest)
print(article_texts[highest], article_links[highest],article_upvotes[highest])