#Este file Scrapes los comentarios de best.tattoos.style de Instagram, creando un bot que extrae automaticamente las personas tagged y los comentarios

from bs4 import BeautifulSoup
from urllib.request import urlopen

handle = "best.tattoo.styles"
url = "https://www.instagram.com/"
page = urlopen(url+handle).read()
soup = BeautifulSoup(page, features="html.parser")
print(soup.prettify())
string = soup.find("meta",  property="og:description")['content']
print(string)
followers = string.split(" Followers, ")[0].replace(",","").replace("k", "000")
if "." in followers:
   followers = followers.replace(".","")[:-1]
   
following = string.split(" Followers, ")[1].split(" Following, ")[0].replace(",","").replace("k", "000")
if "." in following:
   following = following.replace(".","")[:-1]
   
posts = string.split(" Followers, ")[1].split(" Following, ")[1].split(" Posts")[0].replace(",","").replace("k", "000")
if "." in posts:
   posts = posts.replace(".","")[:-1]
   
print(posts, followers, following)
import time
import re
from selenium import webdriver

url = "https://www.instagram.com/p/BwPjOXCl-TT/"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

time.sleep(1)
if driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div[2]/div[2]/div[3]/div/div/div/button'):
   driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div[2]/div[2]/div[3]/div/div/div/button').click()

hasLoadMore = True
while hasLoadMore:
    time.sleep(1)
    try:
        if driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.KlCQn.EtaWk > ul > li.lnrre > button'):
            driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.KlCQn.EtaWk > ul > li.lnrre > button').click()
    except:
        hasLoadMore = False
users_list = []
users = driver.find_elements_by_class_name('_6lAjh')

for user in users:
    users_list.append(user.text)
    
i = 0
texts_list = []
texts = driver.find_elements_by_class_name('C4VMK')

for txt in texts:
    texts_list.append(txt.text.split(users_list[i])[1].replace("\r"," ").replace("\n"," "))
    i += 1
    comments_count = len(users_list)
    
for i in range(1, comments_count):
    user = users_list[i]
    text = texts_list[i]
    text = text.encode('unicode-escape').decode('utf-8')
    print("User ",user)
    print("Text ",text)
    idxs = [m.start() for m in re.finditer('@', text)]
    for idx in idxs:
        handle = text[idx:].split(" ")[0]
        print(handle)
#problema emojis semi arreglados. Aparece el unicode pero no el emoji
