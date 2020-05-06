# A simple script that crawls a random wikipedia page. 
# Prints the name of the wikipedia entry, the date when it was last modified
# and the categories the page belongs to.

import requests
from bs4 import BeautifulSoup

page_url = 'https://en.wikipedia.org/wiki/Special:Random'

response1 = requests.get(page_url) 
soup = BeautifulSoup(response1.text , 'html.parser')

title = soup.find('h1',{'class':'firstHeading'}).text # finding the title

last_mod = soup.find('li',{'id':'footer-info-lastmod'}).get_text(strip=True) # finding when page was last modified

categories = []
categ_links = soup.find('div',{'class':'mw-normal-catlinks'}).findAll('a') # finding the categories

for link in categ_links:
    categories.append(link.text) # each iteration add one categorie to 'categories' list
    
print(title,'\n') # print title
print(last_mod,'\n') # print when page was last modified

if len(categories) != 0: # if there are any categories to print:
    print(*categories, sep = '\n - ') # print categories
    
else:
    print('no categories available') # in case there are no categories
