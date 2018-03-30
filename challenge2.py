text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
code = 'map'

def transalate(str):
    out = ''
    for i in str:
        if i.isalpha():
            new_char = ord(i) + 2
            out += chr((new_char - 97)%26 + 97)
        else:
            out += i
    return out

print(transalate(text))
print(transalate(code))
# http://www.pythonchallenge.com/pc/def/ocr.html
