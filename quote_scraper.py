from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "python-scraper/chromedriver"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com/")

authors_set = set()


while len(authors_set) < 10:
	quotes = driver.find_elements(By.CLASS_NAME, "quote")
	for quote in quotes:
		author_name = quote.find_element(By.CLASS_NAME, "author").text
		authors_set.add(author_name)
	next_button = driver.find_element(By.CSS_SELECTOR, ".next > a")
	if "disabled" in next_button.get_attribute("class"):
		break
	next_button.click()
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
	
for author_name in authors_set:
	name = author_name.replace(" ", "-")
	if "." in author_name:
		name = author_name.replace(".", "-")
		name = name.replace(" ", "")
	
	driver.get(f"http://quotes.toscrape.com/author/{name}")

	nationality = driver.find_element(By.CLASS_NAME, "author-born-location").text
	date_of_birth = driver.find_element(By.CLASS_NAME, "author-born-date").text
	description = driver.find_element(By.CLASS_NAME, "author-description").text
	
	print("Name:", name)
	print("Nationality:", nationality)
	print("Description:", description)
	print("Date of Birth:", date_of_birth)
	print()


# name = "seun. a"
# print(name.strip("n"))
driver.quit()
