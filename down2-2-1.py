
import urllib.request as dw

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTA0MjRfMTg2%2FMDAxNTU2MDgyMzkyNDQ1.3T76FdO1bPHLsYDmrGwb58B6OqwHqCMQztDh6eC1LkAg.zeR-C3S2G5ind-7TQ12R1Ik0bgN5VMAP-c5z-vG3pZgg.JPEG.vetmed01%2F002.jpg&type=sc960_832"
htmlURL = "http://google.com"

savePath1 = "d:/aaa/test1.jpg"
savePath2 = "d:/aaa/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료")
