#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install requests


# In[3]:


from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd


# In[4]:


page = rq.get('https://www.dineout.co.in/delhi-restaurants')


# In[5]:


page


# In[6]:


soup = bs(page.content)


# In[7]:


soup


# In[8]:


first_title = soup.find("a",class_="restnt-name ellipsis")
first_title


# In[9]:


title = first_title.text
title


# In[13]:


titles = []

for title in soup.find_all("a",class_="restnt-name ellipsis"):
    titles.append(title.text)
    
titles    


# In[14]:


locations = []

for location in soup.find_all("div",class_="restnt-loc ellipsis"):
    locations.append(location.text)
    
locations


# In[16]:


prices = []

for price in soup.find_all("span",class_="double-line-ellipsis"):
    prices.append(price.text.split('|')[0])
    
prices


# In[17]:


images = []

for img in soup.find_all("img",class_="no-img"):
    images.append(img.get('data-src'))
    
images


# In[18]:


all_data = pd.DataFrame({'Title':titles, 'Location':locations, 'Price':prices, 'Image':images})
all_data


# In[19]:


# saving the dataframe
all_data.to_csv('beautiful_soup.csv', header=True, index=False)


# In[ ]:




