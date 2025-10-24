from time import sleep
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By


myinput = input("oh good sir what do you wish to know? ")

bad = []
good = []
great = []
results = []

def lastword(myinput):
    lis = list(myinput.split(' '))
    length = len(lis)
    return lis[length-1]
last_word = lastword(myinput.strip())
Last_word = last_word.title()

def firstword(myinput):
    lis = list(myinput.split(' '))
    length = len(lis)
    return lis[length-3]
first_word = firstword(myinput.strip())
First_word = first_word.title()

def remove_duplicates(duplist):
    noduplist = []
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist

def sort_text(Input):
    INput = Input.title()
    sleep(1)    
    for x in results:
        if (Input in x and INput in x):
            good.append(x)
    sleep(1.1)


    for x in results:
        if INput not in x:
            if Input in x:
                good.append(x)
    sleep(1.1)

    for x in results:
        if Input not in x:
            if INput in x:
                good.append(x)
    sleep(1.1)

    for x in results:
        if (Input not in x and INput not in x):
            if INput not in x:
                if Input not in x:
                    bad.append(x)
    sleep(1.1)

    Great = remove_duplicates(duplist=great)
    Good = remove_duplicates(duplist=good)
    Bad = remove_duplicates(duplist=bad)

    print("great\n")
    sleep(2)
    for x in Great:
        print("\t - " + x)
        sleep(0.1)
    print("\n")
    print("good\n")
    for x in Good:
        print("\t - " + x)
        sleep(0.1)
    print("\n")
    print("bad\n")
    for x in Bad:
        print("\t - " + x)
        sleep(0.1)


def lastandfirst(one, two):
    One = one.title()
    Two = two.title()
    for x in results:
        if (one in x and two in x):
            great.append(x)
        if (One in x and Two in x):
            great.append(x)
        if (One in x and two in x):
            great.append(x)
        if (Two in x and one in x):
            great.append(x)
        sleep(1)
    for x in results:
        if two in x:
            if one not in x:
                good.append(x)
    sleep(1)
    for x in results:
        if Two in x:
            if One not in x:
                good.append(x)
    for x in results:
        if Two in x:
            if one not in x:
                good.append(x)
    sleep(1)
    for x in results:
        if One in x:
            if two not in x:
                good.append(x)
    sleep(1)
    

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

def compare(d):
    Great = remove_duplicates(duplist=great)
    Good = remove_duplicates(duplist=good)
    Bad = remove_duplicates(duplist=bad)

    if d != Great:
        for y in Great:
            for z in d:
                if y == z:
                    d.remove(z)
    
            
    

def text_file(textfile):
    fname = (textfile + ".txt")
    fp = ("/home/calisthenicchemist/pythoncode/sources/" + fname) 

    Great = remove_duplicates(duplist=great)
    Good = remove_duplicates(duplist=good)
    Bad = remove_duplicates(duplist=bad)

    file = open(fp, "w")
    file.write("great\n")
    for x in Great:
        file.write("\t - " + x + "\n")
        sleep(0.2)
    file.write("\n")
    file.write("good\n")
    for x in Good:
        file.write("\t - " + x + "\n")
        sleep(0.2)
    file.write("\n")
    file.write("bad\n")
    for x in Bad:
        file.write("\t - " + x + "\n")
    file.close()

def cloop():
    Great = remove_duplicates(duplist=great)
    Good = remove_duplicates(duplist=good)
    Bad = remove_duplicates(duplist=bad)
    moderate = [Great, Good, Bad]
    for x in moderate:
        compare(d=x)
    sleep(1)
    print("great\n")
    sleep(2)
    for x in Great:
        print("\t - " + x)
        sleep(0.1)
    print("\n")
    print("good\n")
    for x in Good:
        print("\t - " + x)
        sleep(0.1)
    print("\n")
    print("bad\n")
    for x in Bad:
        print("\t - " + x)
        sleep(0.1)

get_sources_for_synthesis(search_term=myinput)
sleep(1)
sort_text(Input=last_word)
sleep(1)
lastandfirst(one=first_word, two=last_word)
sleep(1)
#text_file(textfile=myinput)
cloop()