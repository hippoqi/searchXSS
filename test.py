from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver
#chrome_driver = webdriver.Chrome(r'C:\Users\Shiqi\Desktop\Webdrivers\chromedriver.exe')
s = Service(r'C:\Users\Shiqi\Desktop\Webdrivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)


url = "http://3.144.32.18/"
driver.get(url)
driver.find_element(By.XPATH, r'/html/body/form/input[1]').click()
