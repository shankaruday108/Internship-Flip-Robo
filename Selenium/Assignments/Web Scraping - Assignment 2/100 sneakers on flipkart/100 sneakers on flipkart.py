#!/usr/bin/env python
# coding: utf-8

# Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

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


# Now opening the naukri.com website in a new window
driver.get("https://www.flipkart.com/")
# driver.fullscreen_window()
time.sleep(3)


# In[4]:


writing_search = driver.find_element(By.CLASS_NAME, "_3704LK")
writing_search.send_keys("sneakers")
time.sleep(2)


# In[5]:


remove_login_popup = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
remove_login_popup.click()
time.sleep(3)


# In[6]:


search = driver.find_element(By.CLASS_NAME, "L0Z3Pu")
search.click()
time.sleep(3)


# In[8]:


button_start = 0
button_end   = 20
all_brands = []
all_descriptions = []
all_prices = []

brand= ""
desc= ""
pri= ""

time.sleep(5)

for getdata in range(button_start,button_end):
    brand  = driver.find_elements(By.XPATH, "//div[@class='_2WkVRV']")
    time.sleep(3)
    desc  = driver.find_elements(By.XPATH, "//a[@class='IRpwTa']")
    time.sleep(3)
    pri  = driver.find_elements(By.XPATH, "//div[@class='_30jeq3']")
    time.sleep(3)
    
    if len(brand) > 0:
     
        for a  in brand:
            all_brands.append(a.text)

        for b  in desc:
            all_descriptions.append(b.text)

        for c  in pri:
            all_prices.append(c.text)

        time.sleep(2)

        if len(brand) < 100 and len(all_descriptions) < 100 and len(all_prices) < 100:
            # button_end += 1
            next_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
            next_btn.click()
            time.sleep(5)
        else:
            break
    else:
        break
        
time.sleep(3)        
        


# In[9]:


len(all_brands)


# In[10]:


len(all_descriptions)


# In[11]:


len(all_prices)


# In[12]:


all_data = pd.DataFrame({'Brand':all_brands[:100], 'Product Description':all_descriptions[:100], 'Price':all_prices[:100]})
all_data


# In[13]:


all_data.to_csv("_100_sneakers.csv", header=False, index=False)


# In[ ]:





# In[ ]:




