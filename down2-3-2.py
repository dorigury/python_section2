
import urllib.request as req
from urllib.parse import urlencode

API = "https://api.ipify.org"

values = {
    'format': 'json'
}

print('before', values)
params = urlencode(values)

print('after', params)

url = API + "?" + params
print("request url ", url )

reqData = req.urlopen(url).read().decode('utf-8')

print("result", reqData)
