#!/usr/bin/env python
# coding: utf-8

# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[14]:


import selenium as sm
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[15]:


# Now connection to the driver which is available in this folder of my laptop
driver = webdriver.Chrome(r"D:\Uday Shankar's Data\Softwares\chromedriver_win32\chromedriver.exe")


# In[16]:


# Now opening the naukri.com website in a new window
driver.get("https://www.azquotes.com/")
# driver.fullscreen_window()
time.sleep(3)


# In[17]:


search_quotes = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]")
search_quotes.click()
time.sleep(3)


# In[18]:


# Counting the data in first tab
quotes  = driver.find_elements(By.XPATH, "//a[@class='title']")
len(quotes)


# In[5]:


button_start = 0
button_end   = 9
all_quotes = []
all_authors = []
all_type_of_quotes = []

quotes= ""
authors= ""
type_of_quotes= ""

time.sleep(5)

for getdata in range(button_start,button_end):
    quotes  = driver.find_elements(By.XPATH, "//a[@class='title']")
    time.sleep(3)
    authors  = driver.find_elements(By.XPATH, "//div[@class='author']")
    time.sleep(3)
    type_of_quotes = driver.find_elements(By.XPATH, "//div[@class='tags']")
    time.sleep(3)
    
    if len(quotes) > 0:
     
        for a  in quotes:
            all_quotes.append(a.text)

        for b  in authors:
            all_authors.append(b.text)

        for c  in type_of_quotes:
            all_type_of_quotes.append(c.text)

        time.sleep(2)

        if len(all_quotes) < 1000:
    #         button_end += 1
            next_btn = driver.find_element(By.XPATH, "//li[@class='next']")
            next_btn.click()
            time.sleep(5)
        else:
            break
    else:
        break
        
time.sleep(3)        
        
button_end


# In[6]:


len(all_quotes)


# In[7]:


len(all_authors)


# In[8]:


len(all_type_of_quotes)


# In[11]:


all_data = pd.DataFrame({'Quote':all_quotes[:1000], 'Author ':all_authors[:1000], 'Type Of Quotes':all_type_of_quotes[:1000]})
all_data


# In[12]:


all_data = pd.DataFrame({'Quote':all_quotes, 'Author ':all_authors, 'Type Of Quotes':all_type_of_quotes}).iloc[:1000]
all_data


# In[13]:


all_data.to_csv("TopQuotes_1000_Quotes.csv", header=False, index=False)


# In[ ]:




