# coding=utf-8
import re
import requests


def get_html():
    s = requests.session()
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    headers = {"user-agent": ua}
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"

    r = s.get(url, headers=headers)
    return r.text


raw_result = get_html()

raw_result = re.findall(r">({\"page\".+?)<", raw_result)[0]

ret = raw_result.encode().decode('unicode_escape')
ret = ret.replace("\\/", "/")  # 去掉转义字符对URL的影响
with open("result.json", mode='w') as f1:
    f1.write(ret)

print(ret)
