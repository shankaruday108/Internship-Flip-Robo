#!/usr/bin/env python
# coding: utf-8

# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. ProductDescription
# 3. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and 
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the 
# required data asusual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page asusual
# 6. Repeat this until you get data for 100sunglasses.
# Note: That all of the above steps have to be done by coding only and not manually

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


# In[3]:


# Now opening the naukri.com website in a new window
driver.get("https://www.flipkart.com/search?q=sunglass&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
driver.fullscreen_window()
time.sleep(3)


# In[4]:


#brand_search = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[5]/div[2]/div[1]/div[2]")
#brand_search.click()
#time.sleep(3)


# In[5]:


button_start = 0
button_end   = 20
brands = []
product_descriptions = []
prices = []

brand_name= ""
des= ""
pri= ""

time.sleep(5)


# In[6]:


for getdata in range(button_start,button_end):
    brand_name  = driver.find_elements(By.XPATH, "//div[@class='_2WkVRV']")
    time.sleep(3)
    des  = driver.find_elements(By.XPATH, "//a[@class='IRpwTa']")
    time.sleep(3)
    pri = driver.find_elements(By.XPATH, "//div[@class='_30jeq3']")
    time.sleep(3)
    
    if len(brand_name) > 0:
     
        for br  in brand_name:
            brands.append(br.text)

        for de  in des:
            product_descriptions.append(de.text)

        for pr  in pri:
            prices.append(pr.text)

        time.sleep(2)

        if len(brands) < 100:
            # button_end += 1
            next_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
            next_btn.click()
            time.sleep(5)
        else:
            break
        
    else:
        break   
        
time.sleep(3)        
        


# In[7]:


len(product_descriptions)


# In[8]:


len(prices)


# In[9]:


all_data = pd.DataFrame({'Brand':brands, 'Product Description':product_descriptions, 'Price':prices}).iloc[:100]
all_data


# In[10]:


all_data.to_csv("100_Sunglasses_Listings_On_Flipkart.csv", header=False, index=False)


# In[ ]:




