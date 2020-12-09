from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.zoomit.ir/product/list/mobile/")
assert "mobile" in driver.title
elem = driver.find_elements_by_class_name("productSummery__title span")
elem.clear()
elem.send_keys("")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()