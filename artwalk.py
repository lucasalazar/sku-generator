from bs4 import BeautifulSoup as bs #Importa pacotes necessários
import requests
import webbrowser

arrayLinks = []


def get_links():
    url = "https://www.artwalk.com.br/checkout/cart/add?sku="
    url2 = "&qty=1&seller=1&redirect=false&sc=1"
    sku = 2136283
    global arrayLinks
    arquivo = open("links.txt", "w+")
    while(sku < 2139000):
        urlCompleto = url + str(sku) + url2
        arrayLinks.append(urlCompleto)
        sku+=1
        print(urlCompleto)
        arquivo.write(urlCompleto+"\n")
        
get_links()
