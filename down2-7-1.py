from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.inflearn.com/courses"
#url = "https://finance.daum.net/domestic/all_quotes"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

#print('soup >> ', soup.prettify())

top = soup.select("div.courses_container")
titles = soup.select("div.courses_container div.course_title")

for title in titles:
    print("title >> ", title.string)
