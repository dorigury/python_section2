from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.inflearn.com/courses"
#url = "https://finance.daum.net/domestic/all_quotes"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

#print('soup >> ', soup.prettify())

contents = soup.select("div.courses_container > div > div")

#print("top >> ", top)
#titles = soup.select("div.courses_container div.course_title")

i = 0
for content in contents:
    i = i + 1
    print("title >> ", content.select_one("div.course_title").string)
    print("instructor >> ", content.select_one("div.instructor").string)
    print("price >> ", content.select_one("div.price"))
    print("check >> " , i)
