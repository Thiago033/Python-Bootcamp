from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re, time

driver_path = "C:/Program Files/Development/chromedriver_win32/chromedriver.exe"

chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(driver_path, options=chr_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(10)

# cookie_button = driver.find_element(By.ID, 'cookieAnchor')
# cookie_button.click()

items = driver.find_elements(By.CSS_SELECTOR, "#products div")
items_ids = []

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

for item in items:
    product_id = item.get_attribute("id")
    if re.match(r"product[0-9]", product_id):
        items_ids.append(product_id)