from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./chromedriver.exe')
id = "com.facebook.orca"
prefix_url = "https://play.google.com/store/apps/details?id="
first_url = prefix_url + id
browser.get(first_url)

see_mores = browser.find_elements_by_css_selector('div.g4kCYe a')

see_more = None
for m in see_mores:
    if m.text == "See more":
        see_more = m
        print(m.text)
        break

# click "See more" button
see_more.click()

# wait 2 seconds
time.sleep(1)

elem = browser.find_element_by_tag_name("body")
no_of_pagedowns = 20
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1

# wait 2 seconds
time.sleep(1)

apps = browser.find_elements_by_css_selector('div.cover a.card-click-target')
for app in apps:
    print(app.get_attribute('href'))

# quit the browser
browser.quit()
