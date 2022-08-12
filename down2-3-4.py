
import urllib.request as req

imgUrl = "https://ssl.pstatic.net/melona/libs/1398/1398931/528cbdcf3198f008f4cc_20220805141207920.jpg"

savePath = "d:/aaa/test2.jpg"

req.urlretrieve(imgUrl, savePath)

print("done")
