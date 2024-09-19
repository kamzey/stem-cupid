from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
    return driver

def scrape_disciplines():
    driver = get_driver()
    driver.get("https://www.gradcracker.com/search/all-disciplines/engineering-graduate-jobs")

    disciplines = [element.text for element in driver.find_elements(By.CLASS_NAME, "tw-flex-1")]
    disciplines_hrefs = [element.find_element(By.TAG_NAME, "a").get_attribute("href")
                        for element in driver.find_elements(By.CLASS_NAME, "tw-py-1")]
    
    disciplines_dict = {disciplines[i]: disciplines_hrefs[i] for i in range(len(disciplines))}

    driver.quit()
    return disciplines_dict



