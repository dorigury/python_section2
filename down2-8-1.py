from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath = "D:\\bbb\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid")
print("test >> ", img_list)
