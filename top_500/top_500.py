
import bs4 as bs
import requests
import os

def save_global500():

    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup (resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    vect = []
    vect1 = []
    for row in table.findAll('tr') [1:]:
        ticker = row.findAll('td') [0].text
        vect.append(ticker)
        ticker = row.findAll('td') [1].text
        vect1.append(ticker)

  
    return vect, vect1

if __name__ == '__main__':
    
    [vect ,vect1] = save_global500()
    n = len(vect)
    
    file = open("global500.txt",mode = "w")
    
    for i in range(n):
        
        file.write(vect[i][:-1])
        file.write(";")
        file.write(vect1[i])
        file.write("\n")

    file.close()