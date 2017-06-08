import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from itertools import islice

mydict = {} #dictionary zum speichern der woerter und ihrer haeufigkeiten
		
for seite in range (0,4,1): #im loop werden die seiten der heise.de website durchgegangen, welche einen bezug zum thema https haben
    heise_url = "https://www.heise.de/thema/https?seite="+str(seite)	
    print(heise_url)
    soupElement = (BeautifulSoup(((requests.get(heise_url)).text),"lxml")).find("div", {"class":"keywordliste"})    #erstellen und durchsuchen eines BSoup-Elements
    headlines = soupElement.findAll("header") #spezielles suchen nach headern, um die ueberschriften zu isolieren
        
    for zeile in headlines:   #for loop zum aufsplitten der ueberschriften in einzelne woerter
        zeileAlsText = zeile.text
        woerter = zeileAlsText.split()
            
        for wort in woerter:   #befuellen des dictionarys mit den einzelnen woertern
            if not wort in mydict:  #falls nicht vorhanden: neuer eintrag mit haeufigkeit 1
                mydict[wort] = 1
            if wort in mydict:  #wenn vorhanden wird value um 1 erhoeht
                mydict[wort] = mydict[wort]+1
                
print("Die Top 3 Wörter sind: ")
def take (n, iterable): #funktion zum auswaehlen der ersten n elemente, eines durchzaehlbaeren objektes, mit rueckgabe einer liste
    return list(islice(iterable,n))

print(take(3,sorted(mydict.items(), key=itemgetter(1), reverse=True)))  #ausgabe einer liste mit take funktion(n=3) aus sortierter liste