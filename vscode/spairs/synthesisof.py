from time import sleep

print("synthesis of 'chemical name'")
myinput = input("what chemical's synthesis do you wish to know of? ")

great = []
good = []
bad = []

results = ['https://byjus.com/chemistry/preparation-of-benzene/', 'https://www.toppr.com/ask/content/concept/preparation-of-benzene-202952/', 'https://www.chemistrysteps.com/synthesis-of-aromatic-compounds-from-benzene/', 'https://www.masterorganicchemistry.com/2018/11/19/synthesis-7-reaction-map-of-benzene-and-related-aromatic-compounds/', 'https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/b/Benzene.htm', 'https://en.wikipedia.org/wiki/Benzene', 'https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Map%3A_Organic_Chemistry_(Vollhardt_and_Schore)/15%3A_Benzene_and_Aromaticity%3A_Electrophilic_Aromatic_Substitution/15.08%3A_Synthesis_of_Benzene__Derivatives%3A__Electrophilic_Aromatic__Substitution', 'https://byjus.com/chemistry/preparation-of-benzene/', 'https://www.toppr.com/ask/content/concept/preparation-of-benzene-202952/', 'https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/b/Benzene.htm', 'https://en.wikipedia.org/wiki/Benzene', 'https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/b/Benzene.htm', 'https://en.wikipedia.org/wiki/Benzene', 'https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Map%3A_Organic_Chemistry_(Vollhardt_and_Schore)/15%3A_Benzene_and_Aromaticity%3A_Electrophilic_Aromatic_Substitution/15.08%3A_Synthesis_of_Benzene__Derivatives%3A__Electrophilic_Aromatic__Substitution', 'https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Supplemental_Modules_(Organic_Chemistry)/Arenes/Synthesis_of_Arenes/Electrophilic_Aromatic_Substitution', 'https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Map%3A_Organic_Chemistry_(Vollhardt_and_Schore)/15%3A_Benzene_and_Aromaticity%3A_Electrophilic_Aromatic_Substitution/15.08%3A_Synthesis_of_Benzene__Derivatives%3A__Electrophilic_Aromatic__Substitution','https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Supplemental_Modules_(Organic_Chemistry)/Arenes/Synthesis_of_Arenes/Electrophilic_Aromatic_Substitution', 'https://www.echemi.com/cms/603806.html', 'https://www.masterorganicchemistry.com/2018/10/15/aromatic-synthesis-1-order-of-operations/', 'https://www.nature.com/articles/d41586-021-02322-y', 'https://pubs.acs.org/doi/10.1021/jacs.6b02533']

def remove_duplicates(duplist):
    noduplist = []
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist


def lastword(myinput):
    lis = list(myinput.split(' '))
    length = len(lis)
    return lis[length-1]
last_word = lastword(myinput.strip())

def firstword(myinput):
    lis = list(myinput.split(' '))
    length = len(lis)
    return lis[length-3]
first_word = firstword(myinput.strip())





def synthesis(one, two):
    One = one.title()
    Two = two.title()
    #synthesis and chemical name
    sleep(1)
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

    # chemical name no, synthesis yes
    for x in results:
        if two in x:
            if one not in x:
                good.append(x)
    for x in results:
        if Two in x:
            if One not in x:
                good.append(x)
    for x in results:
        if Two in x:
            if one not in x:
                good.append(x)
    for x in results:
        if two in x:
            if One not in x:
                good.append(x)
    
    # synthesis no, chemical name yes
    for x in results:
        if One in x:
            if two not in x:
                good.append(x)
    for x in results:
        if one in x:
            if two not in x:
                good.append(x)
    for x in results:
        if One in x:
            if Two not in x:
                good.append(x)
    for x in results:
        if one in x:
            if Two not in x:
                good.append(x)

    Good = remove_duplicates(good)
    Great = remove_duplicates(great)

    sleep(2)
    for x in Great:
        print(" - " + x)
    print("\n")
    for x in Good:
        print(" - " + x)


if "synthesis" in myinput:
    synthesis(one=first_word, two=last_word)

    


