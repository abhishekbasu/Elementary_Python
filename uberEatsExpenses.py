import re

f = open('uberEats.txt', 'r')
content = f.read()
sum([float(x[1:]) for x in re.findall("[\$]{1}[\d,]+\.?\d{0,2}", string=content)])