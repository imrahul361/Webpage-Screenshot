from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

url = input("Enter the Url: ")
driver = webdriver.Chrome()
driver.get(url)
sleep(4)

driver.get_screenshot_as_file("Screenshot.png")
driver.quit()
print("Done")