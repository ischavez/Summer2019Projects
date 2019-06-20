# from requests import get
# from requests.exceptions import RequestException
# from contextlib import closing
from bs4 import BeautifulSoup
import urllib
# import time

# URL = input("Input URL: ")
# URL = 'http://web.mta.info/developers/turnstile.html'
# print("URL being used is "+URL)
#
# page = urllib.request.urlopen(URL)
# soup = BeautifulSoup(page, 'html.parser')
# print('Ping1')
#
# for i in range(36, len(soup.findAll('a'))+1): #'a' tags are for links
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']
#     download_url = 'http://web.mta.info/developers/' + link
#     urllib.request.urlretrieve(download_url, './'+link[link.find('/turnstile_')+1:])
#     time.sleep(1) #pause the code for a sec
#     print('ping')

URL = 'https://www.allrecipes.com/recipes/201/meat-and-poultry/chicken/'
print("URL being used is "+URL+'\n')

page = urllib.request.urlopen(URL)
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())

a_tag = soup.findAll('a')

previous = ""
for tag in a_tag:
    link = str(tag.get('href'))
    if "https://www.allrecipes.com/recipe/" in link:
        if link != previous:
            print(link)
            previous = link

# print(a_tag)
# recipies = a_tag.select

# print(soup.select(".ng-isolate-scope"))

# print(soup.findAll("a", {'class':['ng-isolate-scope']}))


# for a in soup.findAll('a', attrs={'href'}):


#favorite ng-isolate-scope

# mydivs = soup.findAll("div", {"class": 'ng-isolate-scope'})#grid-col--subnav ng-isolate-scope'})
# print(mydivs)