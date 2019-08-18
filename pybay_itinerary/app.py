from lxml import html
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = requests.get('https://pybay.com/schedule/')
tree = html.fromstring(page.content)

# <div title="buyer-name">Carson Busses</div>
# <span class="item-price">$29.95</span>


# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

#
# #This will create a list of buyers:
# dates = tree.xpath('//div[@class="sch-day-title"]/text()')

# < h2 class ="sch-day-title" > Aug.15, 2019 < / h2 >

dates = [ h2.strip() for h2 in tree.xpath('//h2[@class="sch-day-title"]/text()') ]

# < h3 class ="sch-timeslot-time" > 8:45 a.m. < / h3 >

times = [ h3.strip() for h3 in tree.xpath('//h3[@class="sch-timeslot-time"]/text()') ]

# <p class="sch-speaker">Daniel Chen</p>

speakers = [ p.strip() for p in tree.xpath('//p[@class="sch-speaker"]/text()') ]


descriptions = [ div.strip() for div in tree.xpath('//div[@class="sch-description"]/text()') ]
#
# rooms = [ p.strip() for p in tree.xpath('//p[@class="sch-room"]/text()') ]

test = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "sch-timeslot-time", " " ))]')
#This will create a list of prices
# prices = tree.xpath('//tag[@class="sch-timeslot-time"]/text()')

# print(dates)
# print(times)
# print(speakers)
print(test)
# print(descriptions)
# print(rooms)



# url = 'http://web.mta.info/developers/turnstile.html'
# response = requests.get(url)
#
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # soup.findAll('h4','sch-day-title')
#
# day = soup.findAll("sch-day-title")[:]
#
# one_a_tag = soup.findAll('h4')[:]
#
# print(one_a_tag)