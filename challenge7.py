import re
from zipfile import ZipFile

nothing = 90052
nothings = []
with ZipFile('channel.zip', 'r') as myzip:
    def get_path(nothing):
        return '{0}.txt'.format(nothing)

    def get_next_nothing(nothing):
        data = myzip.read(get_path(nothing)).decode('utf-8')
        m = re.search('(\d*)$', data)
        next_nothing = m.group(1)
        return next_nothing

    def get_comment(nothing):
        return myzip.getinfo(get_path(nothing)).comment.decode('utf-8')

    while(1):
        try:
            if nothing:
                nothings.append(nothing)
            nothing = get_next_nothing(nothing)
        except:
            break

print("".join([get_comment(n) for n in nothings]))
#http://www.pythonchallenge.com/pc/def/oxygen.html
