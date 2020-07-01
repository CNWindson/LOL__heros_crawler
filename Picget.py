import requests
import pprint

json_url = "https://yz.lol.qq.com/v1/zh_cn/search/index.json"
response = requests.get(json_url)
data = response.json()
#html = response.text
pprint.pprint(data)
print(data)
# print(data['champions'])
hero = []
# test = data['champions'][0]
# print(test)
hero_name = []
# hero = test['name']
# print(hero)
for i in range(148):
    hero = data['champions'][i]
    hero_name.append(hero['name'])
    print(hero["image"]["uri"])
    img_data = requests.get(hero["image"]["uri"]).content
    with open(hero_name[i] + '.jpg', mode="wb") as f:
        f.write(img_data)

