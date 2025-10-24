from time import sleep
import selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
myinput = input("saaaaaaaa duuuuude ")


Results = []

def remove_duplicates(duplist):
    noduplist = []
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist

def Shopping_Ebay(material):
    ebay = 'https://www.ebay.com/'
    driver = webdriver.Firefox()
    driver.get(ebay)
    sleep(0.5)
    searchbox = driver.find_element(by=By.ID, value="gh-ac")
    searchbox.send_keys(material)
    searchbox.submit()
    sleep(2)
    Links = driver.find_elements(by=By.CLASS_NAME, value="s-item__link")
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

def get_shit(url):
    #try:
    amonths = ["Jan", "Mar", "Feb", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(2)
    price = driver.find_element(by=By.XPATH, value='//div[@class="x-price-primary"]/span[@class="ux-textspans"]')
    Price = price.text
    sleep(0.1)
    print(f"\tPrice = {Price}")
    sleep(0.5)
    shipping = driver.find_elements(by=By.XPATH, value='//div[@class="ux-labels-values__values-content"]/div/span[@class="ux-textspans ux-textspans--BOLD"]')
    sleep(0.1)
    for x in shipping:
        sleep(1)
        X = remove_duplicates(duplist=x.text)
        for y in amonths:
            if y in X:
                print(f"Shipping Date = {X}")
                sleep(0.1)
        if X == "Free":
            print(f"ShippingPrice1 = {X}")
            sleep(0.1)
        
        if "." in X:
            print(f"Shipping Price2 = {X}")
            sleep(0.1)
    driver.close()
    #except:
        #print("this is the first url isn't it")
        #driver.close()

#Shopping_Ebay(material=myinput)
sleep(0.1)
#for x in Results:
    #print(" - " + x)
    #sleep(1)
get_shit(url="https://www.ebay.com/itm/325756564935?hash=item4bd89ab5c7:g:v14AAOSw5e1ky-rE&amdata=enc%3AAQAIAAAA4O%2FE7h7uHN12Eoca2KBtoxJ7rkl%2B846izKJ0Lmu7qx8AN3dfKsERcJUXNIn4jC21jTPRmOjw%2BqavSKKYq87DQKarlC6RfhlnSZj7lQmVFH01L5Cp%2F0jniIIZjoFrEDqXDIOIJ843NC7aVDfiMCgrdLrZQpmsJHvp%2BBaw0GzxyFQAKLqfgQ9NwEznncHcA89t9ONNb%2F9DJ95uvB%2FWxArARKNA02sLTosf2e1d7zIeQX%2FLNmzMLxPGeTZF8%2FSbJVAz6tcgZrhhTQlAajfZVPkQAvJP8ozcnzGiVkIGvn3dHCRR%7Ctkp%3ABk9SR76e-ti3Yg")
print("fuck ebay, try removing duplist ... it got rid of the shipping cost")
