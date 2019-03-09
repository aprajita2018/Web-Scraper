#!/usr/bin/env python
# coding: utf-8

# In[2]:


#libraries to perform webscraping

from urllib.request import urlopen
from bs4 import BeautifulSoup # used to extract data from the html page


# In[3]:


# specifying url for the page, and open the html using urlopen() method

url = "https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex#tab-contract-documents"
html = urlopen(url)


# In[4]:


import json,urllib.request
import urllib.parse
import re
data = urllib.request.urlopen("https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex").read()


# In[5]:


#parse the page using BeautifulSoup() function which returns python object of type bs4.BeautifulSoup()

soup = BeautifulSoup(data, 'lxml')
type(soup)


# In[57]:


import requests

response = requests.get("https://www.sourcewell-mn.gov/cooperative-purchasing/022217-wex")
html1 = response.content
soup = BeautifulSoup(html1)
result = {}
vendor = {}

for contract in soup.find_all('div', class_='vendor-contract-header__content'):
    title = contract.find('p', class_='lead').text
    contract_number = contract.find_all('p')[1].text
    result["title"] = title
    result["contract_number"] = contract_number.split()[0][1:]
    result["expiration"] = contract_number.split()[3]
    vendor["name"] = contract.find('h1').text
    
files = []
contracts = soup.find('div',id ='tab-contract-documents').find_all('div', class_='field--item')[1].find('a').get('href')
file_obj = {}
file_obj["contract-forms"] = contracts
files.append(file_obj)
result["files"] = files

contacts = []
contacts_obj = {}
contacts_obj["name"] = soup.find('div', id = 'tab-contact-information').find_all('article', role = 'article')[0].find('div').find_all('div')[0].strong.text
contacts_obj["phone"] = soup.find('div', id = 'tab-contact-information').find_all('article', role = 'article')[0].find('div').find_all('div', class_= "field field--label-inline")[0].find('div', class_='field--item').text
contacts_obj["email"] = soup.find('div', id = 'tab-contact-information').find_all('article', role = 'article')[0].find('div').find_all('div', class_= "field field--label-inline")[1].find('div', class_='field--item').text
contacts.append(contacts_obj)
vendor["contacts"] = contacts
result["vendor"] = vendor

print(result)


# In[59]:


import json

print(json.dumps(result, indent = 2))


# In[ ]:




