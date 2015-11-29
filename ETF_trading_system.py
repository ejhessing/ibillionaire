# -*- coding: utf-8 -*-
import re
import json
import requests
from pprint import pprint

header = {
    'cookie': '__utmt=1; _hjUserId=616c6415-761e-30fa-b733-1652b38ca9b2; csrftoken=yyhYiazr254BNO8XYYB166LtfZePf2kc; __utma=94914500.1425706763.1448673958.1448673958.1448673958.1; __utmb=94914500.2.10.1448673958; __utmc=94914500; __utmz=94914500.1448673958.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
res = requests.get("http://www.ibillionaire.me/funds/1/warren-buffett/berkshire-hathaway", verify=False, headers=header)

# use re to extract types and percentages
m = re.search("data: eval\('\[(.*)\]'", res.text)
# clean space and remove []
m2 = m.group(1).replace(" ", "").replace("[", "").replace("]", "")
# split string by "," and transform to list
m3 = m2.split(",")

for i in range(int(len(m3)/2)):
    print (m3[2*i], round(float(m3[2*i + 1]), 2))
