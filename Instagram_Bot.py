
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

user=str(input("Enter username/email/mobile no :"))
password=str(input("Enter password : "))
tags=str(input("Enter Tag Name : "))
browser = webdriver.Chrome()

browser.get(
    'https://www.instagram.com/accounts/login')  # url of product

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(2)

browser.find_element_by_name('username').send_keys(user)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys('Follow4FollowBack')
browser.get('https://www.instagram.com/explore/tags/'+tags)
time.sleep(2)
i=1
linked=[]
while(i<20):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    content=browser.find_elements_by_tag_name('a')
    content=[elem.get_attribute('href') for elem in content if '.com/p/' in elem.get_attribute('href')]
    i+=1
print(len(content))
links=set(content)
print(links)
print(len(links))
for link in content:
    try:
        browser.get(link)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span').click()
        time.sleep(2)
      
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys("F4F")
        time.sleep(3)
    
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/button').click()
        time.sleep(2)
    except Exception:
        continue
browser.close()
