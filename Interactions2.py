from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

article_count = driver.find_element(By.NAME, value="fName")
article_count.send_keys("Diego")

article_count = driver.find_element(By.NAME, value="lName")
article_count.send_keys("Fernandez")

article_count = driver.find_element(By.NAME, value="email")
article_count.send_keys("diegofernandez@gmail.com")

article_count = driver.find_element(By.CSS_SELECTOR, value="form button")
article_count.click()

