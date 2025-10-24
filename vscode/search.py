from time import sleep
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
results = []
Results = []
bluenames = []
shopping = []

myinput=input("sup ")
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
    for link in links:
        h3 = link.find_element(by=By.TAG_NAME, value="h3")
        href = link.get_attribute("href")
        results.append(href)
    counts = [results.index(item) for item in results]
    sleep(0.6)
    try:
        Counts = str(int(counts[-1] + 1))
        print(f"Jarvis... Sir I have found {Counts} sources for your search")
    except IndexError:
        print("didn't find shit")
    sleep(0.5)
    browser.close()

def search_sources(search):
    google_scholar = 'https://scholar.google.com'
    driver = webdriver.Firefox()
    driver.get(google_scholar)
    sleep(0.5)
    searchbox = driver.find_element(by=By.ID, value="gs_hdr_tsi")
    searchbox.send_keys(search)
    searchbox.submit()
    sleep(60)
    for i in range(3):
        try:
            sleep(0.5)
            Links = driver.find_elements(by=By.XPATH, value='//h3[@class="gs_rt"]/a')
            for Link in Links:
                Href = Link.get_attribute("href")
                Results.append(Href)
            counds = [Results.index(item) for item in Results]
            sleep(1)
            sleep(2)
            Next = driver.find_element(by=By.XPATH, value='//b[@style="display:block;margin-left:53px"]')
            Next.click()
        except:
            driver.close()





def Abstract_google_scholar(url):
    driver = webdriver.Firefox()
    driver.get(url)
    if ".pdf" in url:
        print("\tA whole ass artical! lets Gooooooo!!!")
    else:
        try:
            try:
                try:
                    try:
                        abstract = driver.find_element(by=By.XPATH, value='//div[@class="u-mb-1"]//div')
                    except:
                        abstract = driver.find_element(by=By.XPATH, value='//div[@class="abstractSection abstractInFull"]/p')
                except:
                    abstract = driver.find_element(by=By.XPATH, value='//section[@class="abstract"]/p')
            except:
                abstract = driver.find_element(by=By.XPATH, value='//div[@class="simple-item-view-description item-page-field-wrapper table"]')
        except:
            pass
        try:
            Abstract = abstract.text
            print(f"\n{Abstract}")
        except:
            print("\tI tried :(")

    driver.close()
    
def Shopping_Amazon(material):
    amazon = 'https://www.amazon.com/electronics-store/b?ie=UTF8&node=172282&tag=mh0b-20&hvadid=78065360753152&hvqmt=p&hvbmt=bb&hvdev=c&ref=pd_sl_515aw1wohw_b'
    driver = webdriver.Firefox()
    driver.get(amazon)
    sleep(0.5)
    searchbox = driver.find_element(by=By.ID, value="twotabsearchtextbox")
    searchbox.send_keys(material)
    searchbox.submit()
    sleep(6)
    Links = driver.find_elements(by=By.XPATH, value='//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for Link in Links:
        Href = Link.get_attribute("href")
        Results.append(Href)
        sleep(0.1)
    counds = [Results.index(item) for item in Results]
    sleep(1)
    try:
        Counds = str(int(counds[-1] + 1))
        print(f"Jarvis... Sir I have found {Counds} sources for your search")
    except IndexError:
        print("didn't find shit")
    sleep(0.5)
    driver.close()

def duckduckgo_searching():
    duckduckgo = "https://duckduckgo.com"
    driver = webdriver.Firefox()
    driver.get(duckduckgo)
    sleep(0.5)
    search_box = driver.find_element(by=By.ID, value="searchbox_input")
    search_box.send_keys("amazon servos")
    search_box.submit()
    sleep(2)




def summarize_amazon(url):
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(2)
    price = driver.find_element(by=By.XPATH, value='//span[@class="a-price-whole"]')
    Price = price.text
    cents = driver.find_element(by=By.XPATH, value='//span[@class="a-price-fraction"]')
    Cents = cents.text
    properties = driver.find_elements(by=By.XPATH, value='//li[@class="a-spacing-mini"]/span')
    try:
        stars = driver.find_element(by=By.XPATH, value='//a/span[@class="a-size-base a-color-base"]')
    except:
        pass
    for z in properties:
        sleep(2)
        Properties = z.text
        print(f"\t\t - {Properties}")
    sleep(1)
    try:
        Stars = stars.text
        print(f"\t{Stars} Stars")
    except:
        print("\tno star rating")
    try:
        freereturns = driver.find_element(by=By.ID, value="creturns-policy-anchor-text")
        Free_returns = freereturns.text
        print(f"\t{Free_returns}")
    except:
        print("\tno free returns")
    print(f"\tPrice=${Price}.{Cents}")

    sleep(0.1)
    driver.close()


print("\n")
print("\t--removed duplicates--")
print("\n")

def remove1(List):
    cleaned_list = list(set(List))
    for x in cleaned_list:
        print(cleaned_list.index(x))
        print ("\t" + x)
        Abstract_google_scholar(url=x)

#remove1(List=Results)

Shopping_Amazon(material=myinput)
for x in Results:
    print(Results.index(x))
    print(x)
    sleep(1)
    #Abstract_google_scholar(url=x)
    sleep(0.1)
    summarize_amazon(url=x)

#index properties url stars free returns price