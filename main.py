import randcoords

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

coords = randcoords.generate()
s = Service('C:/Users/konch/OneDrive/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s)
s = 'https://www.google.com/maps/@'+str(coords[0][0])+','+str(coords[0][1])+',16.25z'
driver.get(s)
driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()




















