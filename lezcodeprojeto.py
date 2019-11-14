# projeto:
# fazer webscraping de ROE (yahoo finance)
#Dividend (dividend.com)
#Last closing price (yahoo finance)
#Beta (yahoo finance)
#P\e (yahoo finance)
#net worth (yahoo finance)
from bs4 import BeautifulSoup
import requests
empresa = input("nome da empresa:")
url1 = f"https://finance.yahoo.com/quote/{empresa}?p={empresa}&.tsrc="
r = req
uests.get(url1)
soup = BeautifulSoup(r.text, 'html.parser')
last = soup.find("span",{"data-reactid":"44"})
opn = soup.find("span",{"data-reactid":"49"})
PE = soup.find("span",{"data-reactid":"95"})
beta = soup.find("span",{"data-reactid":"110"})

print(opn)