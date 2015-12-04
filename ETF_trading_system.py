# -*- coding: utf-8 -*-
import re
import requests


header = {
    'cookie': '__utmt=1; _hjUserId=616c6415-761e-30fa-b733-1652b38ca9b2; csrftoken=yyhYiazr254BNO8XYYB166LtfZePf2kc; __utma=94914500.1425706763.1448673958.1448673958.1448673958.1; __utmb=94914500.2.10.1448673958; __utmc=94914500; __utmz=94914500.1448673958.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}

print "Billionaire Investors list"
print "0: Warren Buffett, 1: Carl Icahn, 2: George Soros, 3: Ray Dalio, 4: John Paulson, 5: David Tepper"
print "6: Leon Cooperman, 7: Julian Robertson, 8: Daniel Loeb, 9: Steve Mandel, 10: Nelson Peltz"
print "11: Larry Robbins, 12: Bill Ackman, 13: David Einhorn, 14: Chase Coleman, 15: Richard Chilton"

while True:
    ib = raw_input("Input a number between 0 ~ 15: (empty , other numbers or text will quit): ")
    if ib == str(0):
        url = "http://www.ibillionaire.me/funds/1/warren-buffett/berkshire-hathaway"
        name = "Warren Buffett"
    elif ib == str(1):
        url = "http://www.ibillionaire.me/funds/4/carl-icahn/carl-icahn"
        name = "Carl Icahn"
    elif ib == str(2):
        url = "http://www.ibillionaire.me/funds/17/george-soros/soros-fund-management"
        name = "George Soros"
    elif ib == str(3):
        url = "http://www.ibillionaire.me/funds/29/ray-dalio/bridgewater-associates"
        name = "Ray Dalio"
    elif ib == str(4):
        url = "http://www.ibillionaire.me/funds/5/john-paulson/paulson-co"
        name = "John Paulson"
    elif ib == str(5):
        url = "http://www.ibillionaire.me/funds/3/david-tepper/appaloosa-management-lp"
        name = "David Tepper"
    elif ib == str(6):
        url = "http://www.ibillionaire.me/funds/14/leon-cooperman/omega-advisors"
        name = "Leon Cooperman"
    elif ib == str(7):
        url = "http://www.ibillionaire.me/funds/19/julian-robertson/tiger-management"
        name = "Julian Robertson"
    elif ib == str(8):
        url = "http://www.ibillionaire.me/funds/10/daniel-loeb/third-point-capital"
        name = "Daniel Loeb"
    elif ib == str(9):
        url = "http://www.ibillionaire.me/funds/21/steve-mandel/lone-pine-capital"
        name = "Steve Mandel"
    elif ib == str(10):
        url = "http://www.ibillionaire.me/funds/31/nelson-peltz/trian-fund-management"
        name = "Nelson Peltz"
    elif ib == str(11):
        url = "http://www.ibillionaire.me/funds/30/larry-robbins/glenview-capital-management"
        name = "Larry Robbins"
    elif ib == str(12):
        url = "http://www.ibillionaire.me/funds/13/bill-ackman/pershing-square"
        name = "Bill Ackman"
    elif ib == str(13):
        url = "http://www.ibillionaire.me/funds/9/david-einhorn/greenlight-capital"
        name = "David Einhorn"
    elif ib == str(14):
        url = "http://www.ibillionaire.me/funds/11/chase-coleman/tiger-global"
        name = "Chase Coleman"
    elif ib == str(15):
        url = "http://www.ibillionaire.me/funds/23/richard-chilton/chilton-investment-co"
        name = "Richard Chilton"
    else:
        print "wrong parameter, you input " + str(ib)
        print "bye bye!"
        quit()

    # sometimes connection will be rejected, need error handle
    try:
        res = requests.get(url, verify=False, headers=header)
    except Exception as e:
        print "Exception: " + str(e)
        quit()

    # user re to retract Portfolio Value
    match = re.search('\<h2\>([0-9]*.)', res.text)
    if match:
        value = match.group(0)
        if value[-1] == 'M':
            p_value = float(value[4:-1]) / 1000
        else:
            p_value = float(value[4:-1])
    else:
        value = "not get Portfolio Value"

    # use re to extract types and percentages
    m = re.search("data: eval\('\[(.*)\]'", res.text)
    # clean space and remove []
    m2 = m.group(1).replace(" ", "").replace("[", "").replace("]", "")
    # split string by "," and transform to list
    m3 = m2.split(",")

    # final result
    print name
    print "Portfolio Value: " + str(p_value) + " billions"
    for i in range(int(len(m3)/2)):
        print (m3[2*i][1:-1], round(float(m3[2*i + 1]), 2))
