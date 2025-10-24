from time import sleep
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

my_input = input("wtf do you want? ")
def get_sources_for_synthesis(search_term):
    google = "https://www.google.com"
    browser = webdriver.Firefox()
    browser.get(google)
    sleep(0.5)
    search_box = browser.find_element(by=By.ID, value="APjFqb")
    search_box.send_keys(search_term)
    search_box.submit()
    sleep(2)
    links = browser.find_elements(by=By.XPATH, value='//div[@class="yuRUbf"]/div/a')
    results = []
    for link in links:
        h3 = link.find_element(by=By.TAG_NAME, value="h3")
        href = link.get_attribute("href")
        results.append(href)
    counts = [results.index(item) for item in results]
    sleep(0.5)
    
    Counts = str(int(counts[-1] + 1))
    for x in results:
        print("-" + x)
    print(f"Jarvis... Sir I have found {Counts} sources for your search")
    
    browser.close()
get_sources_for_synthesis(search_term=my_input)

