import requests
from bs4 import BeautifulSoup

def getListCountriesBasedOnTotalCasesPerCapita():
    URL = "https://www.worldometers.info/coronavirus/#main_table"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    x = soup.find_all("div", class_="maincounter-number")
    print("total cases : " + x[0].text.strip())

    table = soup.find("table")

    countries = {}
    l =[]
    for row in table.find_all("tr")[1:]:
        td = row.find_all("td")
        if td[1] and td[10].text !="":
            l.append(float(td[10].text.replace(",","")))
            countries[td[1].text]=td[10].text
    l.sort(reverse= True)

    m = []
    for i in l:
        for key in countries.keys():
            if float(countries[key].replace(",",""))==i:
                if key not in m:
                    m.append(key)
    return m, countries

if __name__ == "__main__":
    m, countries = getListCountriesBasedOnTotalCasesPerCapita()
    for j in m:
        print(j+ "\t\t" + str(countries[j]))
