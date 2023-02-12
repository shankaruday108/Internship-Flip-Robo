#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[18]:


import selenium as sm
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# Now we have to download the webdriver of the same version which is in our chrome version otherwise it will not work

# In[25]:


# Now connection to the driver which is available in this folder of my laptop
driver = webdriver.Chrome(r"D:\Uday Shankar's Data\Softwares\chromedriver_win32\chromedriver.exe")


# In[26]:


# Now opening the naukri.com website in a new window
driver.get("https://www.naukri.com/")


# In[27]:


designation_first = driver.find_element(By.CLASS_NAME, "suggestor-input ")
designation_first.send_keys("Python")


# In[28]:


location = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys("Delhi")


# In[29]:


search = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()


# In[37]:


start = 
job_titles = []
job_locations = []
company_name = []
experience_required = []


# In[38]:


title = driver.find_elements(By.XPATH, "//a[@class='title ellipsis']")
end = len(title)

for i in title[start:end]:
    job_titles.append(i.text)
    
job_titles    


# In[39]:


location = driver.find_elements(By.XPATH, "//span[@class='ellipsis fleft locWdth']")
end = len(location)

for i in location[start:end]:
    job_locations.append(i.text)
    
job_locations   


# In[40]:


company = driver.find_elements(By.XPATH, "//a[@class='subTitle ellipsis fleft']")
end = len(company)

for i in company[start:end]:
    company_name.append(i.text)
    
company_name  


# In[41]:


experience = driver.find_elements(By.XPATH, "//span[@class='ellipsis fleft expwdth']")
end = len(experience)

for i in experience[start:end]:
    experience_required.append(i.text)
    
experience_required 


# In[42]:


all_data = pd.DataFrame({'Job Title':job_titles, 'Job Location':job_locations, 'Company Name':company_name, 'Experience Required':experience_required})
all_data


# In[43]:


all_data.to_csv("selenium_naukri_dot_com_data.csv", header=True, index=False)


# In[ ]:




