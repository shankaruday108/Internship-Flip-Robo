#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the 
# location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.
# 

# In[1]:


import selenium as sm
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# Now we have to download the webdriver of the same version which is in our chrome version otherwise it will not work

# In[2]:


# Now connection to the driver which is available in this folder of my laptop
driver = webdriver.Chrome(r"D:\Uday Shankar's Data\Softwares\chromedriver_win32\chromedriver.exe")


# In[3]:


# Now opening the naukri.com website in a new window
driver.get("https://www.naukri.com/")


# In[4]:


designation_first = driver.find_element(By.CLASS_NAME, "suggestor-input ")
designation_first.send_keys("“Data Analyst")


# In[5]:


location = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys("Bangalore")


# In[6]:


search = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()
time.sleep(3)


# In[7]:


start = 0
end = 10
job_titles = []
job_locations = []
company_name = []
experience_required = []


# In[8]:


title = driver.find_elements(By.XPATH, "//a[@class='title ellipsis']")

for i in title[start:end]:
    job_titles.append(i.text)
    
job_titles  


# In[9]:


location = driver.find_elements(By.XPATH, "//span[@class='ellipsis fleft locWdth']")

for i in location[start:end]:
    job_locations.append(i.text)
    
job_locations 


# In[10]:


company = driver.find_elements(By.XPATH, "//a[@class='subTitle ellipsis fleft']")

for i in company[start:end]:
    company_name.append(i.text)
    
company_name  


# In[11]:


experience = driver.find_elements(By.XPATH, "//span[@class='ellipsis fleft expwdth']")

for i in experience[start:end]:
    experience_required.append(i.text)
    
experience_required 


# In[12]:


all_data = pd.DataFrame({'Job Title':job_titles, 'Job Location':job_locations, 'Company Name':company_name, 'Experience Required':experience_required})
all_data


# In[13]:


all_data.to_csv("data_analyst_jobs_in_bangalore.csv", header=False, index=False)


# In[ ]:




