#!/usr/bin/env python
# coding: utf-8

# Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results. 
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get thewebpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the searchbutton.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results youget.
# 6. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

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
driver.get("https://www.naukri.com/")


# In[4]:


designation_first = driver.find_element(By.CLASS_NAME, "suggestor-input ")
designation_first.send_keys("Data Scientist")


# In[5]:


search = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()
time.sleep(3)


# In[6]:


# Searching salary for 3-6 Lakhs
salary_search = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
salary_search.click()
time.sleep(4)


# In[7]:


# Searching location for Delhi/NCR
location_search = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[3]/label/i")
location_search.click()
time.sleep(4)


# In[19]:


start = 0
end = 10
job_titles = []
job_locations = []
company_name = []
experience_required = []


# In[20]:


title = driver.find_elements(By.XPATH, "//a[@class='title ellipsis']")

for i in title[start:end]:
    job_titles.append(i.text)
    
job_titles  


# In[21]:


location = driver.find_elements(By.XPATH, "//span[@class='ellipsis fleft locWdth']")

for i in location[start:end]:
    job_locations.append(i.text)
    
job_locations


# In[22]:


company = driver.find_elements(By.XPATH, "//a[@class='subTitle ellipsis fleft']")

for i in company[start:end]:
    company_name.append(i.text)
    
company_name 


# In[23]:


experience = driver.find_elements(By.XPATH, "//span[@class='ellipsis fleft expwdth']")

for i in experience[start:end]:
    experience_required.append(i.text)
    
experience_required 


# In[24]:


all_data = pd.DataFrame({'Job Title':job_titles, 'Job Location':job_locations, 'Company Name':company_name, 'Experience Required':experience_required})
all_data


# In[25]:


all_data.to_csv("data_scientist_jobs_in_delhi_ncr.csv", header=False, index=False)


# In[ ]:




