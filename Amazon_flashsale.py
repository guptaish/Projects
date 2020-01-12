from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser=webdriver.Chrome()
browser.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
browser.find_element_by_id('ap_email').send_keys('abc@gmail.com')#your amazon email
browser.find_element_by_id('continue').click()
browser.find_element_by_id('ap_password').send_keys('123456')#your password
browser.find_element_by_id('signInSubmit').click()
#i=0
#n=str(input())
#if(n=='true' or n=='T' or 0xFF==ord('o')):
while(True):
    browser.get('https://www.amazon.in/Fabulous-Shampoo-250ml-Conditioner-Reviver/dp/B00NCHR9BQ/')#url of product
    price=browser.find_element_by_id('priceblock_ourprice')
    #button=browser.find_element_by_id('buy-now-button')
    cart=browser.find_element_by_id('add-to-cart-button')
    deal=browser.find_element_by_id('priceblock_dealprice')        
    p=price.text
    d=deal.text
    dealbutton=browser.find_element_by_id('a-autoid-0-announce')
    if(d=='₹ 1,599.40'):#flash sale item price 
        dealbutton.click()
        break
    


    
    
    
