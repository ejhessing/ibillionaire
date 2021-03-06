# -*- coding: utf-8 -*-
import requests
import os
import time
import json
import operator
from pprint import pprint
from bs4 import BeautifulSoup

if not os.path.exists("output"):
    os.mkdir("output")

header = {
    'cookie': '__utmt=1; _hjUserId=616c6415-761e-30fa-b733-1652b38ca9b2; csrftoken=yyhYiazr254BNO8XYYB166LtfZePf2kc; __utma=94914500.1425706763.1448673958.1448673958.1448673958.1; __utmb=94914500.2.10.1448673958; __utmc=94914500; __utmz=94914500.1448673958.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}

urls = ["http://www.dataroma.com/m/holdings.php?m=AIM",
        "http://www.dataroma.com/m/holdings.php?m=AV",
        "http://www.dataroma.com/m/holdings.php?m=CMAFX",
        "http://www.dataroma.com/m/holdings.php?m=psc",
        "http://www.dataroma.com/m/holdings.php?m=HRSVX",
        "http://www.dataroma.com/m/holdings.php?m=oaklx",
        "http://www.dataroma.com/m/holdings.php?m=fairx",
        "http://www.dataroma.com/m/holdings.php?m=ic",
        "http://www.dataroma.com/m/holdings.php?m=ARFFX",
        "http://www.dataroma.com/m/holdings.php?m=DJCO",
        "http://www.dataroma.com/m/holdings.php?m=cfimx",
        "http://www.dataroma.com/m/holdings.php?m=AC",
        "http://www.dataroma.com/m/holdings.php?m=tp",
        "http://www.dataroma.com/m/holdings.php?m=abc",
        "http://www.dataroma.com/m/holdings.php?m=GLRE",
        "http://www.dataroma.com/m/holdings.php?m=WP",
        "http://www.dataroma.com/m/holdings.php?m=AM",
        "http://www.dataroma.com/m/holdings.php?m=WA",
        "http://www.dataroma.com/m/holdings.php?m=DODGX",
        "http://www.dataroma.com/m/holdings.php?m=YAFFX",
        "http://www.dataroma.com/m/holdings.php?m=EL",
        "http://www.dataroma.com/m/holdings.php?m=ca",
        "http://www.dataroma.com/m/holdings.php?m=CCM",
        "http://www.dataroma.com/m/holdings.php?m=aq",
        "http://www.dataroma.com/m/holdings.php?m=SSHFX",
        "http://www.dataroma.com/m/holdings.php?m=oc",
        "http://www.dataroma.com/m/holdings.php?m=FEVAX",
        "http://www.dataroma.com/m/holdings.php?m=VA",
        "http://www.dataroma.com/m/holdings.php?m=br",
        "http://www.dataroma.com/m/holdings.php?m=CAAPX",
        "http://www.dataroma.com/m/holdings.php?m=KB",
        "http://www.dataroma.com/m/holdings.php?m=hc",
        "http://www.dataroma.com/m/holdings.php?m=mc",
        "http://www.dataroma.com/m/holdings.php?m=oa",
        "http://www.dataroma.com/m/holdings.php?m=LUK",
        "http://www.dataroma.com/m/holdings.php?m=SQ",
        "http://www.dataroma.com/m/holdings.php?m=hcmax",
        "http://www.dataroma.com/m/holdings.php?m=LLPFX",
        "http://www.dataroma.com/m/holdings.php?m=MVALX",
        "http://www.dataroma.com/m/holdings.php?m=GFT",
        "http://www.dataroma.com/m/holdings.php?m=MFP",
        "http://www.dataroma.com/m/holdings.php?m=PI",
        "http://www.dataroma.com/m/holdings.php?m=FFH",
        "http://www.dataroma.com/m/holdings.php?m=pzfvx",
        "http://www.dataroma.com/m/holdings.php?m=SEQUX",
        "http://www.dataroma.com/m/holdings.php?m=OFALX",
        "http://www.dataroma.com/m/holdings.php?m=jensx",
        "http://www.dataroma.com/m/holdings.php?m=muhlx",
        "http://www.dataroma.com/m/holdings.php?m=lmvtx",
        "http://www.dataroma.com/m/holdings.php?m=BAUPOST",
        "http://www.dataroma.com/m/holdings.php?m=LPC",
        "http://www.dataroma.com/m/holdings.php?m=FPACX",
        "http://www.dataroma.com/m/holdings.php?m=MKL",
        "http://www.dataroma.com/m/holdings.php?m=GR",
        "http://www.dataroma.com/m/holdings.php?m=TWEBX",
        "http://www.dataroma.com/m/holdings.php?m=WVALX",
        "http://www.dataroma.com/m/holdings.php?m=brk",
        "http://www.dataroma.com/m/holdings.php?m=t2",
        "http://www.dataroma.com/m/holdings.php?m=MPGFX",
        "http://www.dataroma.com/m/holdings.php?m=TVAFX",
        "http://www.dataroma.com/m/holdings.php?m=cc"
        ]

# Portfolio
ConsumerGoods = 0
Financials = 0
InformationTechnology = 0
Technology = 0
ConsumerDiscretionary = 0
Energy = 0
Industrials = 0
HealthCare = 0
TelecommunicationsServices = 0
Materials = 0
Utilities = 0
Services = 0
IndustrialGoods = 0
ConsumerStaples = 0
Portfolio = [ConsumerGoods, Financials, InformationTechnology, Technology, ConsumerDiscretionary, Energy, Industrials,
             HealthCare, TelecommunicationsServices, Materials, Utilities, Services, IndustrialGoods, ConsumerStaples
             ]

# use bs4 to extract date
try:
    res = requests.get(urls[0], verify=False, headers=header)
except Exception as e:
    print "Check Portfolio Date occurs Exception: " + str(e)
    quit()

soup = BeautifulSoup(res.content, "html.parser")
spans = []
for span in soup.find_all('span'):
    spans.append(span.text)
date = spans[1]
print "Portfolio Date: " + date

print "Continue? (y = yes, empty or others will exit)"
go = raw_input("")
if go != 'y':
    print "you input " + str(go)
    print "bye bye!"
    quit()
print "Roger that! This will take some minutes..."
print ""

for i in range(0, len(urls)):
    # sometimes connection will be rejected, need error handle
    try:
        print urls[i]
        res = requests.get(urls[i], verify=False, headers=header)
    except Exception as e:
        print "Get data occurs Exception: " + str(e)
        print urls[i]
        quit()
    soup = BeautifulSoup(res.content, "html.parser")
    # user bs4 to retract Portfolio Value
    # clean out list
    spans[:] = []
    for span in soup.find_all('span'):
        spans.append(span.text)
    try:
        p_value = float(spans[3][1:].replace(",", "")) / 1000000000
    except ValueError:
        # if not get the Portfolio Value, try another location
        try:
            p_value = float(spans[5][1:].replace(",", "")) / 1000000000
        except ValueError:
            print "get Portfolio Value fail, only got:"
            print spans[5][1:].replace(",", "")
            print "exit..."
            exit()
    print str(p_value) + "B"

    # use BS4 to extract types and percentages
    div = soup.find_all(id='sect')
    data = []
    for trs in div:
        for td in trs.find_all('td'):
            data.append(td.text)

    for i in range(0, len(data)/3):
        sector = data[i*3]
        percentage = float(data[i*3+1]) / 100

        if sector == u'Consumer Goods':
            ConsumerGoods += p_value * percentage
            print "Consumer Goods: " + str(ConsumerGoods)
        elif sector == u'Financials':
            Financials += p_value * percentage
            print "Financials: " + str(Financials)
        elif sector == u'Information Technology':
            InformationTechnology += p_value * percentage
            print "Information Technology: " + str(InformationTechnology)
        elif sector == u'Technology':
            Technology += p_value * percentage
            print "Technology: " + str(Technology)
        elif sector == u'Consumer Discretionary':
            ConsumerDiscretionary += p_value * percentage
            print "Consumer Discretionary: " + str(ConsumerDiscretionary)
        elif sector == u'Energy':
            Energy += p_value * percentage
            print "Energy: " + str(Energy)
        elif sector == u'Industrials':
            Industrials += p_value * percentage
            print "Industrials: " + str(Industrials)
        elif sector == u'Health Care':
            HealthCare += p_value * percentage
            print "Health Care: " + str(HealthCare)
        elif sector == u'Telecommunications Services':
            TelecommunicationsServices += p_value * percentage
            print "Telecommunications Services: " + str(TelecommunicationsServices)
        elif sector == u'Materials':
            Materials += p_value * percentage
            print "Materials: " + str(Materials)
        elif sector == u'Utilities':
            Utilities += p_value * percentage
            print "Utilities: " + str(Utilities)
        elif sector == u'Consumer Staples':
            ConsumerStaples += p_value * percentage
            print "Consumer Staples: " + str(ConsumerStaples)
        elif sector == u'Services':
            Services += p_value * percentage
            print "Services: " + str(Services)
        elif sector == u'Industrial Goods':
            IndustrialGoods += p_value * percentage
            print "Industrial Goods: " + str(IndustrialGoods)
    time.sleep(1)

# save to dict
dic = {"Consumer Goods": ConsumerGoods, "Financials": Financials, "Technology": Technology,
       "Information Technology": InformationTechnology, "ConsumerDiscretionary": ConsumerDiscretionary,
       "Energy": Energy, "Industrials": Industrials, "Health Care": HealthCare,
       "Telecommunications Services": TelecommunicationsServices, "Materials": Materials,
       "Utilities": Utilities, "Consumer Staples": ConsumerStaples, "Service": Services,
       "Industrial Goods": IndustrialGoods
       }
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
pprint(sorted_dic)

# save to json , name by date
with open("output/dataroma: " + date + ".json", "w") as js:
    json.dump(sorted_dic, js)
print ""
print "Tango Down."
