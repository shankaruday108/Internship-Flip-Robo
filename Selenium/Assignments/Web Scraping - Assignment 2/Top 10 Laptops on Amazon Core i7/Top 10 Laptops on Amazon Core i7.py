#!/usr/bin/env python
# coding: utf-8

# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then 
# set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[1]:


import selenium as sm
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[2]:


# Now connection to the driver which is available in this folder of my laptop
driver = webdriver.Chrome(r"D:\Uday Shankar's Data\Softwares\chromedriver_win32\chromedriver.exe")
time.sleep(3)


# In[3]:


# Now opening the given website in a new window
driver.get("https://www.amazon.in/")
# driver.fullscreen_window()
time.sleep(3)


# In[4]:


writing_search = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
writing_search.send_keys("Laptop")
time.sleep(2)


# In[5]:


search = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()
time.sleep(3)


# In[6]:


search_i7 = driver.find_element(By.XPATH, "//span[normalize-space()='Intel Core i7']")
search_i7.click()
time.sleep(3)


# In[7]:


pri_sign  = driver.find_element(By.XPATH, "//span[@class='a-price-symbol']")
pri_sign = pri_sign.text


# In[8]:


button_start = 0
button_end   = 20
all_titles = []
all_ratings = []
all_prices = []

title= ""
rating= ""
pri= ""

time.sleep(5)

for getdata in range(button_start,button_end):
    title  = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    time.sleep(3)
    rating  = driver.find_elements(By.XPATH, "//span[@class='a-icon-alt']")
    time.sleep(3)
    pri  = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    time.sleep(3)
    
    if len(title) > 0:
     
        for a  in title:
            all_titles.append(a.text)

        for b  in rating:
            all_ratings.append(b.text)

        for c  in pri:
            all_prices.append(pri_sign+c.text)

        time.sleep(2)

        if len(all_titles) < 10 and len(all_ratings) < 10 and len(all_prices) < 10:
            # button_end += 1
            next_btn = driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
            next_btn.click()
            time.sleep(5)
        else:
            break
    else:
        break
        
time.sleep(3)        
        


# In[ ]:





# In[9]:


len(all_titles)


# In[10]:


len(all_ratings)


# In[11]:


len(all_prices)


# In[12]:


all_data = pd.DataFrame({'Title':all_titles[:10], 'Ratings':all_ratings[:10], 'Price':all_prices[:10]})
all_data


# In[13]:


all_data.to_csv("top_10_first_laptops_i7_amazon.csv", header=False, index=False)


# In[ ]:





# In[ ]:




