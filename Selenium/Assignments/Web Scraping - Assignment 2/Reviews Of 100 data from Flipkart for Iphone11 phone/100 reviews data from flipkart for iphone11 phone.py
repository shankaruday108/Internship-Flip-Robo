#!/usr/bin/env python
# coding: utf-8

# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market 
# place=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# Note: All the steps required during scraping should be done through code only and not manually.

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
driver.get("https://www.google.com/search?q=ttps%3A%2F%2Fwww.flipkart.com%2Fapple-iphone-11-black-64-gb%2Fproduct%02reviews%2Fitm4e5041ba101fd%3Fpid%3DMOBFWQ6BXGJCEYNY%26lid%3DLSTMOBFWQ6BXGJCEYNYZXSHRJ%26marketplace%3DFLIPKART&rlz=1C1CHBF_enIN1002IN1002&oq=ttps%3A%2F%2Fwww.flipkart.com%2Fapple-iphone-11-black-64-gb%2Fproduct%02reviews%2Fitm4e5041ba101fd%3Fpid%3DMOBFWQ6BXGJCEYNY%26lid%3DLSTMOBFWQ6BXGJCEYNYZXSHRJ%26marketplace%3DFLIPKART&aqs=chrome..69i57j69i58.847j0j4&sourceid=chrome&ie=UTF-8")
# driver.fullscreen_window()
time.sleep(3)


# In[4]:


search_quotes = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a")
search_quotes.click()
time.sleep(3)


# In[5]:


# Clicking on all review link
search_review = driver.find_element(By.XPATH, "//div[@class='_3UAT2v _16PBlm']")
search_review.click()
time.sleep(3)


# In[6]:


# Counting the data in first tab
star_rating  = driver.find_elements(By.XPATH, "//div[@class='_3LWZlK _1BLPMq']")
len(star_rating)


# In[7]:


button_start = 0
button_end   = 20
all_ratings = []
all_review_summeries = []
all_full_reviews = []

star_rating= ""
half_review= ""
full_review= ""

time.sleep(5)

for getdata in range(button_start,button_end):
    star_rating  = driver.find_elements(By.XPATH, "//div[@class='_3LWZlK _1BLPMq']")
    time.sleep(3)
    half_review  = driver.find_elements(By.XPATH, "//p[@class='_2-N8zT']")
    time.sleep(3)
    full_review  = driver.find_elements(By.XPATH, "//div[@class='t-ZTKy']")
    time.sleep(3)
    
    if len(star_rating) > 0:
     
        for a  in star_rating:
            all_ratings.append(a.text)

        for b  in half_review:
            all_review_summeries.append(b.text)

        for c  in full_review:
            all_full_reviews.append(c.text)

        time.sleep(2)

        if len(all_ratings) < 100:
            # button_end += 1
            # next_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]")
            next_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
            next_btn.click()
            time.sleep(5)
        else:
            break
    else:
        break
        
time.sleep(3)        
        


# In[8]:


len(all_ratings)


# In[9]:


len(all_review_summeries)


# In[10]:


len(all_full_reviews)


# In[11]:


all_data = pd.DataFrame({'Rating':all_ratings[:100], 'Review summary ':all_review_summeries[:100], 'Full review':all_full_reviews[:100]})
all_data


# In[14]:


# By using iloc  
#all_data = pd.DataFrame({'Rating':all_ratings, 'Review summary ':all_review_summeries, 'Full review':all_full_reviews}).iloc[:100]
#all_data


# In[15]:


all_data.to_csv("_100_reviews_iphone_11.csv", header=False, index=False)


# In[ ]:





# In[ ]:




