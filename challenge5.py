# 12345
# 44827
# 45439
# 94485
# 72198
# 80992
# 8880
# 40961

from urllib.parse import urlencode
from urllib.request import urlopen
import re

def nextNothing(nothing):
    params = urlencode({'nothing': nothing})
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?{0}'.format(params)
    f = urlopen(url)
    body = f.read().decode('utf-8')
    m = re.search('(\d*)$', body)
    print(body)
    return m.group(1)

nothing = 12345
for i in range(0, 400):
    new_nothing = nextNothing(nothing)
    if new_nothing:
        nothing = new_nothing
    else:
        nothing = int(nothing)//2
    print(i, new_nothing, nothing)
#http://www.pythonchallenge.com/pc/def/peak.html
