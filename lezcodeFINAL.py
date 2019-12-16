
# projeto:
# fazer webscraping de ROE (yahoo finance)
#Dividend (dividend.com)
#Last closing price (yahoo finance)
#Beta (yahoo finance)
#P\e (yahoo finance)
#net worth (yahoo finance)
from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
import string


betam = 0
lastam = 0
opnm = 0
divm = 0
PEm = 0

empresa = input("nome da(s) empresa(s):")


empresas = empresa.split(",")
for i in empresas: 

	
	url1 = f"https://finance.yahoo.com/quote/{i}?p={i}&.tsrc="
	r = requests.get(url1)
	soup = BeautifulSoup(r.text, 'html.parser')
	last = soup.find("td",{"data-test":"PREV_CLOSE-value"})
	opn = soup.find("td",{"data-test":"OPEN-value"})
	PE = soup.find("td",{"data-test":"PE_RATIO-value"})
	beta = soup.find("td",{"data-test":"BETA_3Y-value"})
	div = soup.find("td",{"data-test":"DIVIDEND_AND_YIELD-value"})
	
	if beta == None:
		betae = 'N/A'
	else:
		betae = beta.text
	if opn == None:
		opne = 'N/A'
	else:
		opne = opn.text
	if last == None:
		laste = 'N/A'
	else:
		laste = last.text
	if PE == None:
		PEe = 'N/A'
	else:
		PEe = PE.text
	if div == None:
		dive = 'N/A'
	else:
		dive = div.text


	lastt = laste.split(" ")
	divt = dive.split(" ")
	opnt = opne.split(" ")
	PEt = PEe.split(" ")
	betat = betae.split(" ")

	if lastt[0] != 'N/A':
		lastf = float(last.text)
	if divt[0] != 'N/A':
		divf = float(divt[1][1:4])
	if opnt[0] != 'N/A':	
		opnf = float(opn.text)
	if PEt[0] != 'N/A':
		PEf = float(PE.text)
	if betat[0] != 'N/A':
		betaf = float(beta.text)

	if betat[0] != 'N/A':	
		betam = betam + betaf
	if lastt[0] != 'N/A':
		lastam = lastam + lastf
	if opnt[0] != 'N/A':
		opnm = opnm + opnf
	if PEt[0] != 'N/A':
		PEm = PEm + PEf
	if divt[0] != 'N/A':
		divm = divm + divf

l = len(empresas)

betav = betam/l
lastav = lastam/l
opnv = opnm/l
PEv = PEm/l
divv = divm/l

print(betav,"list average beta")
print(lastav,"list average last close")
print(opnv,"list average last open")
print(PEv,"list average PE")
print(divv, "list average dividend yield")

person = input("your company")

url2 = f"https://finance.yahoo.com/quote/{person}?p={person}&.tsrc="
u = requests.get(url2)
sou = BeautifulSoup(u.text, 'html.parser')
lastp = sou.find("td",{"data-test":"PREV_CLOSE-value"})
opnp = sou.find("td",{"data-test":"OPEN-value"})
PEp = sou.find("td",{"data-test":"PE_RATIO-value"})
betap = sou.find("td",{"data-test":"BETA_3Y-value"})
divp = sou.find("td",{"data-test":"DIVIDEND_AND_YIELD-value"})

if lastp == None:
	lastep = 'N/A'
else: 
	lastep = lastp.text
if divp == None:
	divep = 'N/A'
else:
	divep = divp.text
if opnp == None:
	opnep = 'N/A'
else: 
	opnep = opnp.text
if PEp == None:
	PEep = 'N/A'
else:
	PEep = PEp.text

if divep != 'N/A':
	divepi = divep.split(" ")
if opnep != 'N/A':
	opnepi = opnep.split(" ")
if lastep != 'N/A':
	lastepi = lastep.split(" ")
if PEep != 'N/A':
	PEepi = PEep.split(" ")

if lastepi[0] != 'N/A':
	lastpf = float(lastep)
if opnepi[0] != 'N/A':
	opnpf = float(opnep)
if PEep[0] != 'N/A':
	PEpf = float(PEep)
if divep[0] != 'N/A':
	divpf = float(divep[1:4])

print(divpf)

print(f"""
	your company's results in relation to the benchmark:
	{lastpf - lastav}Last close
	{opnpf - opnv}   Last open
	{PEpf - PEv}     PE 
	{divpf - divv}   dividend yield""")
#{betapf - betav} beta

















#YTD - year to date, camparison between investments and their benchmarks. -quantidade de lucro gerada por um investimento desde certa data
#adicionar os mesmos critérios do S&P por setor, adicionar lista de empresas separadas por setor, comparar a empresa em questão
#com resto do S&P e lista
#fonte = https://blog.iqoption.com/en/an-analysis-of-sp-500-index-sectors/
#análise de empresa- comparação com o benchmark de seu respectivo setor, análise de risco e rentabilidade relativa ao benchmark.
#análise de risco: standard deviation, Beta and Sharpe ratio.
#standard deviation = volatility
#beta = standard deviation em relação ao benchmark.
#Sharpe ratio = quanto mais o investimento retorna em relação à um investimento sem risco (títulos do governo).
#Pessoa define o risco em porcentagem e o programa retorna os setores mais rentáveis dada a escala de risco e compara com
#as respectivas benchmarks.
# Python code to illustrate splitlines() 
 