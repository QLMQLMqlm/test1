from selenium import webdriver
chromeoptions=webdriver.ChromeOptions()
chromeoptions.headless=True
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chromeoptions)
driver.get("http://localhost:8080/Sales")
driver.find_element_by_id("username").send_keys("yyyy")
v=driver.find_element_by_id("username").get_attribute("value")
print