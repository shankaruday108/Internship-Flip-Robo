#!/usr/bin/env python
# coding: utf-8

# # ANSWER OF 1st QUESTION

# 1. Write a python program which searches all the product under a particular product from www.amazon.in. The 
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
# guitars.

# In[1]:


import selenium as sm
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time
import requests


# In[23]:


# Now connection to the driver which is available in this folder of my laptop
driver = webdriver.Chrome(r"D:\Uday Shankar's Data\Softwares\chromedriver_win32\chromedriver.exe")
time.sleep(3)    


# In[3]:


# Function for browsing url
def openUrlInWindow(urlpath,showfullwindow,sleeptime):
    
    if urlpath:
        driver.get(urlpath)
    
    if showfullwindow.lower() == 'yes':
        time.sleep(sleeptime)
        driver.fullscreen_window()
    
    if sleeptime:
        time.sleep(sleeptime)


# In[4]:


# Now opening the given website in the same window
openUrlInWindow("https://www.amazon.in/","no",3)


# In[5]:


searchvalue = str(input("Enter the search value: "))
time.sleep(3)


# In[6]:


searchud  = driver.find_element(By.ID, "twotabsearchtextbox")
time.sleep(3)
searchud.send_keys(searchvalue)
time.sleep(3)
searchud  = driver.find_element(By.ID, "nav-search-submit-text")
searchud.click()
time.sleep(3)


# # ANSWER OF 2nd QUESTION

# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search 
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
# scrape all the products available under that product name. Details to be scraped are: "Brand 
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[7]:


product_urls       = []
start              = 0
end                = 3
brand_names        = []
product_name       = []
product_price      = []
return_exchange    = []
expected_delivery  = []
availability       = []
product_url        = []


# In[8]:


# Getting all the top 10 products url from tab 1 to 3
for i in range(start, end):
#     driver.execute_script("window.scrollBy(0,10)")
    getting_product_urls = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    time.sleep(3)
    
    for urls in getting_product_urls[0:10]:
        product_urls.append(urls.get_attribute("href"))
    
    time.sleep(3)
    
    if len(product_urls) < 30:
        next_btn = driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
        next_btn.click()
        time.sleep(5)
    else:
        break


# In[9]:


len(product_urls)


# In[10]:


# Getting all the product details by using it's url which was got above
time.sleep(2)
for product in product_urls:
    driver.get(product) # 
    time.sleep(2)
    pri_sign  = driver.find_element(By.XPATH, "//span[@class='a-price-symbol']")
    pri_sign = pri_sign.text
    
    time.sleep(2)
    
    try:
        brand_names1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[44]/div/table/tbody/tr[1]/td[2]/span")
        brand_names.append(brand_names1.text)
    except NoSuchElementException:    
        brand_names.append("-")
        
    try:
        product_names1 = driver.find_element(By.ID, "productTitle")
        product_name.append(product_names1.text)
    except NoSuchElementException:    
        product_name.append("-")
    
    try:
        product_price1 = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")
        product_price.append(pri_sign+product_price1.text)
    except NoSuchElementException:    
        product_price.append("-")
        
    try:
        return_exchange1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[22]/div[2]/div/div/div/div[3]/span/div[2]/a")
        return_exchange.append(return_exchange1.text)
    except NoSuchElementException:    
        return_exchange.append("-")
        
    try:
        expected_delivery1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[2]/div[9]/div[1]/div/div/div[1]/span/span")
        expected_delivery.append(expected_delivery1.text)
    except NoSuchElementException:    
        expected_delivery.append("-")
        
    try:
        availability1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[4]/div/div[1]/span")
        availability.append(availability1.text)
    except NoSuchElementException:    
        availability.append("-")
        
    try:
        product_url.append(product)
    except NoSuchElementException:    
        product_url.append("-")    
    
    


# In[11]:


all_data = pd.DataFrame({'Brand Name':brand_names[:30], 'Name of the Product':product_name[:30], 'Price':product_price[:30], 'Return/Exchange':return_exchange[:30], 'Expected Delivery':expected_delivery[:30], 'Availability':availability[:30], 'Product URL':product_url[:30]})
all_data


# In[12]:


all_data.to_csv("product_details_on_amazon.csv", header=False, index=False)


# In[13]:


def goBack():
    # This is for go back 
    time.sleep(3)
    driver.back()


# # ANSWER OF 3rd QUESTION

# 3. Write a python program to access the search bar and search button on images.google.com and scrape 10 
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 

# In[24]:


# Now opening the given website in the same window
openUrlInWindow("https://www.google.com/","no",3)


# In[25]:


# This is for finding and searching images by it's given name which is passed in it's parameter
def searchImages(keyname):
    
    searchud = ''

    searchud  = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
    time.sleep(3)
    # Searching by it's name
    searchud.send_keys(keyname)
    searchud  = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center/input[1]")
    searchud.click()
    time.sleep(3)

    
    time.sleep(3)
    
    # Now clicking on image icon given above and searching only images
    imageSearch  = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a")
    imageSearch.click()
    time.sleep(3)
    
    return True
    


# In[26]:


imagesOf = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']
searchItemName = imagesOf[0]
searchImages(searchItemName)


# In[28]:


time.sleep(3)
driver.execute_script("window.scrollBy(0,200)")
imageLinks  = driver.find_elements(By.XPATH, "//img[@class='rg_i Q4LuWd']")

image_urls = []
image_data = []

for link in imageLinks:
    if link:
        source = link.get_attribute("src")
        if source is not None:
            if(source[0:4] == 'http'):
                image_urls.append(source)      

time.sleep(3) 

#     return image_urls

for imge in range(len(image_urls)):
    if imge < 10:
        print("Downloading {0} of {1} images".format((imge+1), 10))
        response = requests.get(image_urls[imge])
        file = open(r"D:\xampp\htdocs\Dropbox\Uday\Python\Data Trained\flip robo\Selenium\web-scraping-assignment-3--1---1-\googleimg"+str((imge+1))+".jpeg", "wb")
        file.write(response.content)
        file.close()
    else:
        break


# # ANSWER OF 4th QUESTION

# 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
# details is missing then replace it by “- “. Save your results in a dataframe and CSV. 

# In[29]:


# Now opening the given website in the same window
openUrlInWindow("https://www.flipkart.com/","no",3)


# In[30]:


# Removing the comming popup on home screen for login
remove_login_popup = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
remove_login_popup.click()
time.sleep(3)


# In[31]:


# Getting the search command by the user
searchKeywords = str(input("Enter your search command: "))


# In[32]:


# Writing the search command on search bar
writing_search = driver.find_element(By.CLASS_NAME, "_3704LK")
writing_search.send_keys(searchKeywords)
time.sleep(2)


# In[33]:


# Clicking on the search 
search = driver.find_element(By.CLASS_NAME, "L0Z3Pu")
search.click()
time.sleep(3)


# In[34]:


# Getting all the products url from tab 1
#     driver.execute_script("window.scrollBy(0,10)")
product_urls = []
getting_product_urls = driver.find_elements(By.XPATH, "//a[@class='_1fQZEK']")
time.sleep(3)

for urls in getting_product_urls:
    product_urls.append(urls.get_attribute("href"))

time.sleep(3)


# In[35]:


len(product_urls)


# In[36]:


brand_names              = []
product_name             = []
product_price            = []
product_colour           = []
product_ram              = []
product_storage_rom      = []
product_primary_camera   = []
product_secondary_camera = []
product_display_size     = []
product_battery_capacity = []
product_url              = []


# In[ ]:





# In[37]:


# Getting all the product details by using it's url which was got above
time.sleep(2)
for product in product_urls:
    driver.get(product) # This is for opening all the urls got previously of the product one by one
    time.sleep(2)
    
    read_more = ''
    readyes   = ''
    try:
        read_more = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _1FH0tX']")
        readyes   = 'yes'
    except NoSuchElementException:    
        readyes   = 'no'
    
    if 'yes' in readyes:
        read_more.click()
        time.sleep(2)
        
    try:
        brand_names1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/ul/li")
        brand_names.append(brand_names1.text)
    except NoSuchElementException:    
        brand_names.append("-")
        
    try:
        product_names1 = driver.find_element(By.XPATH, "//span[@class='B_NuCI']")
        product_name.append(product_names1.text)
    except NoSuchElementException:    
        product_name.append("-")
    
    try:
        product_price1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
        product_price.append(product_price1.text)
    except NoSuchElementException:    
        product_price.append("-")
        
    try:
        product_colour1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[1]/table/tbody/tr[4]/td[2]/ul/li")
        product_colour.append(product_colour1.text)
    except NoSuchElementException:    
        product_colour.append("-")
        
    try:
        product_ram1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[2]/ul/li")
        product_ram.append(product_ram1.text)
    except NoSuchElementException:    
        product_ram.append("-")
        
    try:
        product_storage_rom1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/ul/li")
        product_storage_rom.append(product_storage_rom1.text)
    except NoSuchElementException:    
        product_storage_rom.append("-")
        
    try:
        product_primary_camera1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[5]/table/tbody/tr[2]/td[2]/ul/li")
        product_primary_camera.append(product_primary_camera1.text)
    except NoSuchElementException:    
        product_primary_camera.append("-")
        
    try:
        product_secondary_camera1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[5]/table/tbody/tr[5]/td[2]/ul/li")
        product_secondary_camera.append(product_secondary_camera1.text)
    except NoSuchElementException:    
        product_secondary_camera.append("-") 
        
    try:
        product_display_size1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/ul/li")
        product_display_size.append(product_display_size1.text)
    except NoSuchElementException:    
        product_display_size.append("-") 
        
    try:
        product_battery_capacity1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[10]/table/tbody/tr/td[2]/ul/li")
        product_battery_capacity.append(product_battery_capacity1.text)
    except NoSuchElementException:    
        product_battery_capacity.append("-")    
        
    try:
        product_url.append(product)
    except NoSuchElementException:    
        product_url.append("-")    
    
    


# In[38]:


len(brand_names)
len(product_name)
len(product_price)
len(product_colour)
len(product_ram)
len(product_storage_rom)
len(product_primary_camera)
len(product_secondary_camera)
len(product_display_size)
len(product_battery_capacity)
len(product_url)


# In[39]:


all_data = pd.DataFrame({'Brand Name':brand_names, 'Smartphone Name':product_name, 'Colour':product_colour, 'RAM':product_ram, 'Storage(ROM)':product_storage_rom, 'Primary Camera':product_primary_camera, 'Secondary Camera':product_secondary_camera, 'Display Size':product_display_size, 'Battery Capacity':product_battery_capacity, 'Price':product_price, 'Product URL':product_url})
all_data


# In[40]:


all_data.to_csv("product_details_on_flipkart.csv", header=False, index=False)


# # ANSWER OF 5th QUESTION

# 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. 

# In[49]:


# Now opening the given website in the same window
openUrlInWindow("https://www.google.com/","no",3)


# In[50]:


# This is for finding and searching google map by it's given name which is passed in it's parameter
def searchMap(keyname,cityState):
    
    searchud  = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
    time.sleep(3)
    # Searching by it's name
    searchud.send_keys(keyname)
    searchud  = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center/input[1]")
    searchud.click()
    time.sleep(3)

    time.sleep(3)
    
    # Now clicking on google map link given above and searching only maps
    search_map  = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite")
    search_map.click()
    time.sleep(3)
    
    searchud  = driver.find_element(By.ID, "searchboxinput")
    time.sleep(3)
    # Searching by it's name
    searchud.send_keys(cityState)
    searchud  = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
    searchud.click()
    time.sleep(3)
    
    return True
    


# In[51]:


# Passing search command in function
searchMap('google maps', 'Bihar')


# In[52]:


def gettingLongLat():
    # Getting current URL
    get_url = driver.current_url
    time.sleep(2)
    return get_url.split('@')


# In[53]:


alldata = gettingLongLat()


# In[54]:


alldata


# In[55]:


alldata[1].split('/')


# In[56]:


# getting longitude & latitude
long_lat = alldata[1].split(',')
long_lat


# In[57]:


# latitude
long_lat[0]


# In[58]:


# longitude
long_lat[1]


# # ANSWER OF 6th QUESTION

# 6. Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[59]:


# Now opening the given website in the same window
openUrlInWindow("https://www.digit.in/","no",3)


# In[60]:


# Clicking on the gamming menu
clicking_on_gamming  = driver.find_element(By.XPATH, "//a[@class='arrow_down gaming']")
clicking_on_gamming.click()
time.sleep(3)


# In[61]:


# Clicking on the gamming laptop
# clicking_on_gamming_laptop  = driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[5]/div[6]/div/div[2]/div/ul[3]/li[4]")
# clicking_on_gamming_laptop.click()

# Now opening the given website in the same window
openUrlInWindow("https://www.digit.in/gaming-mart/topten/gaming-laptops/","no",3)


# In[62]:


# Getting all the details of the laptop
titles       = []
descriptions = []

def gettingAllDetails():
    
    titles1       = driver.find_elements(By.XPATH, "//div[@class='article_row']/h2/a")
    descriptions1 = driver.find_elements(By.XPATH, "//div[@class='article_row']/p")
    
    for title in titles1:
        try:
            titles.append(title.text)
        except NoSuchElementException:    
            titles.append("-")
    
    for description in descriptions1:
        try:
            descriptions.append(description.text)
        except NoSuchElementException:    
            descriptions.append("-")    


# In[63]:


gettingAllDetails()


# In[64]:


all_data = pd.DataFrame({'Title':titles, 'Descriptions':descriptions})
all_data


# # ANSWER OF 7th QUESTION

# 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 

# In[65]:


# Now opening the given website in the same window
openUrlInWindow("https://www.forbes.com/real-time-billionaires/#1f08e2793d78","yes",3)


# In[66]:


# Getting all the details of the laptop
ranks          = []
names          = []
net_worths     = []
ages           = []
citizenships   = []
sources        = []
industries     = []

def billionairesDetails():
    
    ranks1          = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[2]/div/span")
    names1          = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[3]/div/h3/a")
    net_worths1     = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[4]/div/span")
    ages1           = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[6]/div/span")
    citizenships1   = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[8]/div/span")
    sources1        = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[7]/div/span")
#     industries1   = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[7]/div/span")
    industries1     = sources1
    
    for rank in ranks1:
        try:
            ranks.append(rank.text)
        except NoSuchElementException:    
            ranks.append("-")
    
    for name in names1:
        try:
            names.append(name.text)
        except NoSuchElementException:    
            names.append("-") 
            
    for net_worth in net_worths1:
        try:
            net_worths.append(net_worth.text)
        except NoSuchElementException:    
            net_worths.append("-")
    
    for age in ages1:
        try:
            ages.append(age.text)
        except NoSuchElementException:    
            ages.append("-") 
            
    for citizenship in citizenships1:
        try:
            citizenships.append(citizenship.text)
        except NoSuchElementException:    
            citizenships.append("-")
    
    for source in sources1:
        try:
            sources.append(source.text)
        except NoSuchElementException:    
            sources.append("-")
            
    for industrie in industries1:
        try:
            industries.append(industrie.text)
        except NoSuchElementException:    
            industries.append("-")
    


# In[67]:


billionairesDetails()


# In[68]:


all_data = pd.DataFrame({'Rank':ranks, 'Name':names, 'Net worth':net_worths, 'Age':ages, 'Citizenship':citizenships, 'Source':sources, 'Industry':industries})
all_data


# # ANSWER OF 8th QUESTION

# 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
# from any YouTube Video.

# In[69]:


# Now opening the given website in the same window
openUrlInWindow("https://www.youtube.com/watch?v=kffacxfA7G4","yes",3)


# In[70]:


# Getting all the details of the laptop
names            = []
comments         = []
comment_upvotes  = []
comment_times    = []

def commentDetails():
    
    names1            = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[2]/div/span")
    comments1         = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[3]/div/h3/a")
    comment_upvotes1  = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[4]/div/span")
    comment_times1    = driver.find_elements(By.XPATH, "//table[@class='ng-scope ng-table']//td[6]/div/span")
    
    for name in names1:
        try:
            names.append(name.text)
        except NoSuchElementException:    
            names.append("-")
    
    for comment in comments1:
        try:
            comments.append(comment.text)
        except NoSuchElementException:    
            comments.append("-")
            
    for comment_upvote in comment_upvotes1:
        try:
            comment_upvotes.append(comment_upvote.text)
        except NoSuchElementException:    
            comment_upvotes.append("-")
    
    for comment_times in comment_times1:
        try:
            comment_times.append(comment_time.text)
        except NoSuchElementException:    
            comment_times.append("-")        


# In[71]:


commentDetails()


# In[72]:


all_data = pd.DataFrame({'Name':names,'Comments':comments, 'Comment upvote':comment_upvotes, 'Comment time':comment_times})
all_data


# # ANSWER OF 9th QUESTION

# 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
# reviews, privates from price, dorms from price, facilities and property description.

# In[73]:


# Now opening the given website in the same window
openUrlInWindow("https://www.hostelworld.com/","yes",3)


# In[74]:


def searchingHotels(keywords):
    menu_click  = driver.find_element(By.XPATH, "//button[@class='icon-core-menu-fill header-option item']")
    time.sleep(3)
    menu_click.click()

    clickingonhotel  = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/header/div[2]/div/div[2]/ul[2]/li[3]/a")
#     clickingonhotel.get_attribute('href')
    openUrlInWindow(clickingonhotel.get_attribute('href'),"yes",3)
    
#     typingkeywords  = driver.find_element(By.XPATH, "//input[@class='location-input']")
    time.sleep(3)
    typingkeywords  = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div/label/input")
    typingkeywords.click()
    time.sleep(3)
    # Searching by it's name
    typingkeywords.send_keys(keywords)
    time.sleep(5)
    
    searchud  = driver.find_element(By.XPATH, "//span[normalize-space()='England']")
    searchud.click()
    time.sleep(3)
    
    searchud  = driver.find_element(By.XPATH, "//button[@class='search-button']")
    searchud.click()
    time.sleep(3)
    driver.fullscreen_window()
    time.sleep(3)


# In[ ]:


searchingHotels('London')


# In[85]:


# Getting all the details of the laptop
hostel_names            = []
distances               = []
ratings                 = []
total_reviews           = []
overall_reviews         = []
privates_from_prices    = []
dorms_from_prices       = []
facilities              = []
property_descriptions   = []

def commentDetails():
    
    hostel_names1           = driver.find_elements(By.XPATH, "//h2[@class='title title-6']/a")
    distances1              = driver.find_elements(By.XPATH, "//span[@class='description']/span")
    ratings1                = driver.find_elements(By.XPATH, "//div[@class='score orange big']")
    total_reviews1          = driver.find_elements(By.XPATH, "//div[@class='reviews']")
    overall_reviews1        = driver.find_elements(By.XPATH, "//div[@class='keyword']/span")
    privates_from_prices1   = driver.find_elements(By.XPATH, "//div[@class='prices-col']//a[1]/div[1]/div")
    dorms_from_prices1      = driver.find_elements(By.XPATH, "//div[@class='prices-col']//a[1]/div[2]/div")
    facilities1             = driver.find_elements(By.XPATH, "//div[@class='has-wifi']//span")
    property_descriptions1  = driver.find_elements(By.XPATH, "//div[@class='has-wifi']//span")
    
    
    for hostel_name in hostel_names1:
        try:
            hostel_names.append(hostel_name.text)
        except NoSuchElementException:    
            hostel_names.append("-")
    
    for distance in distances1:
        try:
            distances.append(distance.text)
        except NoSuchElementException:    
            distances.append("-")
            
    for rating in ratings1:
        try:
            ratings.append(rating.text)
        except NoSuchElementException:    
            ratings.append("-")
    
    for total_review in total_reviews1:
        try:
            total_reviews.append(total_review.text)
        except NoSuchElementException:    
            total_reviews.append("-")
            
    for overall_review in overall_reviews1:
        try:
            overall_reviews.append(overall_review.text)
        except NoSuchElementException:    
            overall_reviews.append("-")
    
    for privates_from_price in privates_from_prices1:
        try:
            privates_from_prices.append(privates_from_price.text)
        except NoSuchElementException:    
            privates_from_prices.append("-")
            
    for dorms_from_price in dorms_from_prices1:
        try:
            dorms_from_prices.append(dorms_from_price.text)
        except NoSuchElementException:    
            dorms_from_prices.append("-")
    
    for facilitie in facilities1:
        try:
            facilities.append(facilitie.text)
        except NoSuchElementException:    
            facilities.append("-")        


# In[86]:


commentDetails()


# In[96]:


len(privates_from_prices)


# In[97]:


all_data = pd.DataFrame({'Hotel Name':hostel_names[:11],'Distance from city centre':distances[:11], 'Ratings':ratings[:11], 'Total reviews':total_reviews[:11], 'Overall reviews':overall_reviews[:11], 'Privates from price':privates_from_prices[:11], 'Dorms from price':dorms_from_prices[:11], 'Facilities':facilities[:11]})
all_data


# In[ ]:




