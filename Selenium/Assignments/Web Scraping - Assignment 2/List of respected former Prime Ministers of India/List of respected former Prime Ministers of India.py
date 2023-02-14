#!/usr/bin/env python
# coding: utf-8

# Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[7]:


import selenium as sm
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[11]:


# Now connection to the driver which is available in this folder of my laptop
driver = webdriver.Chrome(r"D:\Uday Shankar's Data\Softwares\chromedriver_win32\chromedriver.exe")


# In[12]:


# Now opening the naukri.com website in a new window
driver.get("https://www.jagranjosh.com/")
driver.fullscreen_window()
time.sleep(3)


# In[13]:


gk_search = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[6]/div/div[1]/header/div[3]/ul/li[9]/a")
gk_search.click()
time.sleep(3)


# In[17]:


pm_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[14]/div/div/ul/li[3]/a")
pm_search.click()
time.sleep(3)


# In[24]:


pm_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[6]/td[2]/p/strong/a")


# In[27]:


start = 0
end = 10
names = []
born_deads = []
term_of_offices = []
remarks = []


# In[ ]:


# No class name only a tag


# In[ ]:





# In[ ]:




