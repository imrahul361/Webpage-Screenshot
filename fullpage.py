from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

url = input("Enter the Url: ")
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(url)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment

driver.find_element_by_tag_name('body').screenshot('Full Screenshot.png')

driver.quit()
print("Done")