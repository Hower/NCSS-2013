import re
match = re.compile(r'<img .*?>')
src = re.compile(r'(?<=src=").*?(?=")')
for x in match.findall(open('site.html').read()):
    if src.search(x):
        print(src.search(x).group())