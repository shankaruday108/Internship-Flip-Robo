#!/usr/bin/env python
# coding: utf-8

# Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

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
driver.get("https://www.jagranjosh.com/")
# driver.fullscreen_window()
time.sleep(3)


# In[4]:


gk_search = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[6]/div/div[1]/header/div[3]/ul/li[9]/a")
gk_search.click()
time.sleep(3)


# In[6]:


pm_search = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[14]/div/div/ul/li[4]")
pm_search.click()
time.sleep(3)


# In[7]:


pm_names = driver.find_element(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[2]/p")
pm_names.text


# In[34]:


pm_office = driver.find_element(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[4]/p")
pm_office.text


# In[44]:


button_start = 0
button_end = 1

names = []
born_deads = []
term_of_offices = []
remarks = []
years_months = []

pmnames= ""
born= ""
term= ""
remk= ""
pm_years= ""

time.sleep(5)

for getdata in range(button_start,button_end):
    
    pmnames  = driver.find_elements(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[2]/p")
    time.sleep(3)
    
    born  = driver.find_elements(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[3]/p")
    time.sleep(3)
    
    term  = driver.find_elements(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[4]/p[1]")
    time.sleep(3)
    
    pm_years  = driver.find_elements(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[4]/p[2]")
    time.sleep(3)
    
    remk  = driver.find_elements(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[5]/p")
    time.sleep(3)
    
#     pm_years = driver.find_elements(By.XPATH, "//div[@class='table-box']/table/tbody/tr/td[4]/p[2]")
#     time.sleep(3)
    
    if len(pmnames) > 0:
     
        for a  in pmnames:
            names.append(a.text)

        for b  in born:
            born_deads.append(b.text)

        for c  in term:
            term_of_offices.append(c.text)
            
        for e  in pm_years:
            years_months.append(e.text)   
                
        for d  in remk:
            remarks.append(d.text)

        time.sleep(2)

    else:
        break
        
time.sleep(3)   


# In[45]:


names


# In[46]:


len(names)


# In[47]:


born_deads


# In[48]:


len(born_deads)


# In[49]:


term_of_offices


# In[50]:


len(term_of_offices)


# In[58]:


# years_months


# In[52]:


len(years_months)


# In[53]:


remarks


# In[54]:


len(remarks)


# In[59]:


all_data = pd.DataFrame({'Name':names[:18], 'Born-Dead':born_deads[:18], 'Term of Office':term_of_offices[:18], 'Remark':remarks[:18], 'Remark':remarks[:18]})
all_data


# In[ ]:




