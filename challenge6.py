from urllib.parse import urlencode
from urllib.request import urlopen
import pickle

res = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
body = res.read()

data = pickle.loads(body)

# From internet
for line in data:
    print("".join([k * v for k, v in line]))
#http://www.pythonchallenge.com/pc/def/channel.html
