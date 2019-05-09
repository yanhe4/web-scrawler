import paramaters
from selenium import webdriver
from time import sleep
#import csv
#from selenium.webdriver.common.keys import Keys


#writer = csv.writer(open(paramaters.file_name, 'wb'))

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=130-1786620-8625104&language=en_US&openid.assoc_handle=amzn_prime_video_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fsignup%252Fref%253Ddv_web_auth_no_re_sig%253F_encoding%253DUTF8%2526offer%253Dpm')

username = driver.find_element_by_id('ap_email')
username.send_keys(paramaters.prime_username)
sleep(0.5)

password = driver.find_element_by_id('ap_password')
password.send_keys(paramaters.prime_password) 
sleep(0.5)

sign_in_button = driver.find_element_by_id('signInSubmit')
sign_in_button.click()
#password.send_keys(Keys.RETURN)
#sleep(20)

username = driver.find_element_by_id('ap_email')
username.send_keys(paramaters.prime_username)
sleep(0.5)

password = driver.find_element_by_id('ap_password')
password.send_keys(paramaters.prime_password) 
sleep(0.5)

sign_in_button = driver.find_element_by_id('signInSubmit')
sign_in_button.click()

series_page = driver.find_element_by_css_selector('a.DigitalVideoUI_Link__link.DigitalVideoWebNodeStorefront_SeeMore__SeeMore.tst-see-more')
series_page.click()
sleep(5.2)

series_link = driver.find_elements_by_css_selector('a.av-beard-title-link')
series_link = [url.get_attribute('href') for url in series_link]
print(len(series_link))

with open(paramaters.file_name, 'w') as f:
    for item in series_link:
        f.write("%s\n" % item)

driver.quit()