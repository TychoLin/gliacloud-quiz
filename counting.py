from os import path
from collections import Counter
from operator import itemgetter

# urls = [
#     # "http://www.google.com/a.txt",
#     # "http://www.google.com.tw/a.txt",
#     "http://www.google.com/download/c.jpg",
#     "http://www.google.co.jp/a.txt",
#     "http://www.google.com/b.txt",
#     "https://facebook.com/movie/b.txt",
#     "http://yahoo.com/123/000/c.jpg",
#     "http://yahoo.com/123/000/c.jpg",
#     "http://yahoo.com/123/000/c.jpg",
#     "http://gliacloud.com/haha.png",
# ]

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

data = []
for url in urls:
    data.append(path.split(url)[1])

data = Counter(data)
data = ((k1, k2) for k1, k2 in data.items())
data = sorted(data, key=itemgetter(0))
data = sorted(data, key=itemgetter(1), reverse=True)

for r in data[:3]:
    k1, k2 = r
    print(k1, k2)
