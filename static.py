from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver_path = "/usr/local/bin/chromedriver"
# Set up the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.gradcracker.com/search/all-disciplines/engineering-graduate-jobs")
disciplines_divs = driver.find_elements(By.CSS_SELECTOR, "a")
disciplines_links = [div.find_element(By.TAG_NAME, "a").get_attribute('href') for div in disciplines_divs]
disciplines_list = [div.text for div in disciplines_divs if div.text.contains('/search/') and ~div.text.contains('/all-disciplines/')]