from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy.orm import Session
from .models import Job, Discipline
from .database import SessionLocal, engine
from geopy.geocoders import Nominatim

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

def scrape_jobs(driver):
    jobs = [element.text for element in driver.find_elements(By.CLASS_NAME, "tw-block")]
    jobs_hrefs = [element.get_attribute("href") for element in driver.find_elements(By.CLASS_NAME, "tw-block")]
    jobs_locations = driver.find_elements(By.XPATH, '//span[contains(text(), "Location:")]/following-sibling::text()')
    jobs_locations = [location.strip() for location in jobs_locations]
    jobs_dict = {jobs[i]: (jobs_hrefs[i], jobs_locations[i]) for i in range(len(jobs))}
    driver.quit()
    return jobs_dict
    
def get_coordinates(location):
    geolocator = Nominatim(user_agent="my_job_scraper")
    try:
        location_obj = geolocator.geocode(location)
        if location_obj:
            return (location_obj.latitude, location_obj.longitude)
        else:
            return (None, None)
    except Exception as e:
        print(f"Error in geocoding location {location}: {e}")
        return (None, None)

def scrape_all_pages(start_url):
    driver = get_driver()
    driver.get(start_url)

    while True:
        jobs_dict = scrape_jobs(driver)
        store_jobs_in_db(jobs_dict)

        try:
            next_button = driver.find_element(By.XPATH, '//a[contains(text(), "Next »")]')
            next_button.click()
        except NoSuchElementException:
            print("Reached the last page")
            break
    
    driver.quit()

def store_jobs_in_db(jobs_dict):
    db = SessionLocal()

    for title, (url, location) in jobs_dict.items():
        job_exists = db.query(Job).filter(Job.url == url).first()
        
        if not job_exists:
            job = Job(title=title, location=location, url=url)
            db.add(job)
            db.commit()

    db.close()



