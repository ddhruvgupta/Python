import re

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    y = re.findall('\@(.*?)\.',pieces[1])
    print(y[0])
    # email = pieces[1].split('@')
    # org = email[1].split('.')
    # print(org[0])
