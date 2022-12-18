from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = "C:/Program Files/Development/chromedriver_win32/chromedriver.exe"

chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(driver_path, options=chr_options)
driver.get("https://www.amazon.com.br/Novo-Echo-4%C2%AA-gera%C3%A7%C3%A3o/dp/B085FXDTTX?ref=dlx_deals_gd_dcl_tlt_16_50a494a2_dt_sl16_bc")
driver.implicitly_wait(10)

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

driver.quit()