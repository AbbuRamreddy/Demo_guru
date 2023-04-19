from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("http://www.demo.guru99.com/V4/")
print(driver.title)
userid=driver.find_element(By.XPATH,"//*[@name='uid']").send_keys("mngr493913")
password=driver.find_element(By.XPATH,"//*[@name='password']").send_keys("madEqAj")
login=driver.find_element(By.XPATH,"//*[@name='btnLogin']").click()
print(driver.title)