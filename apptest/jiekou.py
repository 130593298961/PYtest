import requests

url="https://www.douban.com/"

header={"Cookie":'XXXXXXXXXXXXXXXX'}
html=requests.get(url,headers=header)
print(html.text)