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
r = requests.get(url1)
soup = BeautifulSoup(r.text, 'html.parser')
last = soup.find("td",{"data-test":"PREV_CLOSE-value"})
opn = soup.find("td",{"data-test":"OPEN-value"})
PE = soup.find("td",{"data-test":"PE_RATIO-value"})
beta = soup.find("td",{"data-test":"BETA_3Y-value"})
div = soup.find("td",{"data-test":"DIVIDEND_AND_YIELD-value"})
print(f"forward dividend & yield =  {div.text}")
print(f"previous close           =  {last.text}")
print(f"price earnings           =  {PE.text}")
print(f"beta                     =  {beta.text}")	
print(f"open                     =  {opn.text}")
#dontpad (link=sublimelc)
#adicionar os mesmos critérios do S&P por setor, adicionar lista de empresas separadas por setor, comparar a empresa em questão
#com resto do S&P e lista.
