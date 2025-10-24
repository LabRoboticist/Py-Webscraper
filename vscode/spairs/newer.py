from time import sleep
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import os

bad = []
good = []

def lastword(myinput):
    lis = list(myinput.split(' '))
    length = len(lis)
    return lis[length-1]

def firstword(myinput):
    lis = list(myinput.split(' '))
    length = len(lis)
    return lis[length-3]
first_word = firstword(myinput.strip())
First_word = first_word.title()

myinput = input("oh good sir what do you wish to know? ")
my_input = lastword(myinput.strip())
My_input = my_input.title()

My_input = my_input.title()
def get_sources_for_synthesis(search_term):


    fname = (search_term + ".txt")
    fp = ("/home/calisthenicchemist/pythoncode/sources/" + fname) 
    file = open(fp, "w")
    google = "https://www.google.com"
    browser = webdriver.Firefox()
    browser.get(google)
    sleep(0.5)
    search_box = browser.find_element(by=By.ID, value="APjFqb")
    search_box.send_keys(search_term)
    search_box.submit()
    sleep(2)
    links = browser.find_elements(by=By.XPATH, value='//div[@class="yuRUbf"]/a')
    results = []
    for link in links:
        h3 = link.find_element(by=By.TAG_NAME, value="h3")
        href = link.get_attribute("href")
        results.append(href)
    counts = [results.index(item) for item in results]
    sleep(0.6)
    try:
        Counts = str(int(counts[-1] + 1))

        sleep(1)
        
        for x in results:
            if (my_input in x and My_input in x):
                good.append(x)
        sleep(1.1)


        for x in results:
            if My_input not in x:
                if my_input in x:
                    good.append(x)
        sleep(1.1)

        for x in results:
            if my_input not in x:
                if My_input in x:
                    good.append(x)
        sleep(1.1)

        for x in results:
            if (my_input not in x and My_input not in x):
                if My_input not in x:
                    if my_input not in x:
                        bad.append(x)
        sleep(1.1)


        for x in good:
            print(" - " + x)
        print("\n")
        sleep(0.1)
        for x in bad:
            print(" - " + x)

        sleep(3)

        for x in good:
            file.write(" - " + x + "\n")
            sleep(0.2)
        file.write("\n")
        for x in bad:
            file.write(" - " + x + "\n") 
            
        print(f"Jarvis... Sir I have found {Counts} sources for your search")
    except IndexError:
        print("didn't find shit")
    sleep(0.5)
    browser.close()
    file.close()

get_sources_for_synthesis(search_term=my_input)
