#!/usr/bin/env python
# coding: utf-8

# In[146]:


import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.maximize_window()


# In[118]:


my_password = getpass.getpass()


# In[119]:


user_name = driver.find_element(By.XPATH, "//input[@type='text']")
user_name.send_keys("andersongonzalez2001@gmail.com")

password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys(my_password)


# In[120]:


log_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
log_in_button.click()
sleep(10)

# In[129]:

driver.get("https://www.facebook.com/groups/1486484598263009/members/friends")

friendsListTecno = set()

my_friend = driver.find_elements(
    By.XPATH,
    '//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"]',
)
while True:
    for f in my_friend:
        friendsListTecno.add(f.text)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    my_friend = driver.find_elements(
        By.XPATH,
        '//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"]',
    )
    sleep(5)
    print(friendsListTecno)
    if len(friendsListTecno) > 50:
        break

# In[131]:
driver.get("https://www.facebook.com/anderson.s.gonzalez.8/friends")

friendsList = set()

my_friend = driver.find_elements(
    By.XPATH,
    "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 tia6h79c iv3no6db jagab5yi g1cxx5fr lrazzd5p oo9gr5id']",
)
while True:
    for f in my_friend:
        friendsList.add(f.text)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    my_friend = driver.find_elements(
        By.XPATH,
        "//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 tia6h79c iv3no6db jagab5yi g1cxx5fr lrazzd5p oo9gr5id']",
    )
    sleep(5)
    print(friendsList)
    if len(friendsList) > 100:
        break


# In[132]:


print(len(friendsList))
print(len(friendsListTecno))


# In[133]:


# import pandas as pd


# # In[144]:


# dtecno = pd.DataFrame(friendsListTecno, columns=["name"])
# dfriends = pd.DataFrame(friendsList, columns=["name"])

# # In[145]:


# dtecno.shape
# dfriends.shape

# In[132]:

resultantListFriends = friendsList - friendsListTecno


# dfriendsAct = pd.DataFrame(resultantListFriends, columns=["name"])

# dfriendsAct.shape
print(len(resultantListFriends))

with open("TecnoStudents", "w") as opfile:
    opfile.write("\n".join(friendsListTecno))

with open("NoTecnoStudents", "w") as opfile:
    opfile.write("\n".join(resultantListFriends))

with open("AllFriends", "w") as opfile:
    opfile.write("\n".join(friendsList))


# In[135]:


# %%
