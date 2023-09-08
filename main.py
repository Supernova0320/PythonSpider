import requests
import re
import bs4

# 拿到源代码
start = "0"
url = f"https://movie.douban.com/top250?start={start}"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69"
}
res = requests.get(url, headers=headers)
content = res.text

# 解析数据1：正则表达式
obj = re.compile(r'<li>.*?<span class="title">(?P<film_name>.*?)</span>.*?' # 利用惰性匹配保证匹配到第一个span标签（只有第一个才是中文电影名）
                 r'导演: (?P<film_director>.*?)\s.*?'
                 r'<br>(?P<film_year>.*?)&nbsp', re.S)  # re.S让.可以匹配换行符
result = obj.finditer(content)  # 把content传给既定的表达式，返回一个包含所有匹配结果的可迭代对象
for i in result:
    print(i.group("film_name"))
    print(i.group("film_director"))
    print(i.group("film_year").strip())

# 解析数据2：BeautifulSoup

res.close()
