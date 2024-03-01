#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json

def obtener_numero(cadena):
	numeros = ''.join(filter(str.isdigit,cadena))
	return numeros[:2]


def get_weather(url, ciudad):
	try:
		page = requests.get(url)
		page.raise_for_status()
		soup = BeautifulSoup(page.content, "html.parser")
		lista = soup.find_all("span", class_="col")
		wheater_list=[]
	
		for listas in lista:
			temperatura = listas.find("span",class_="dato-temperatura changeUnitT")
			sensacion = listas.find("span",class_="sensacion changeUnitT")
	   
			if temperatura:
				temperatura_numero = obtener_numero(temperatura.text.strip())
				sensacion_numero = obtener_numero(temperatura.text.strip())
	
				resultados = {
				"ciudad": ciudad,
				"temperatura": temperatura_numero,
				"termica": sensacion_numero
				}
				wheater_list.append(resultados)
		climalocal = {'wheater':wheater_list}
	
		  
		with open(''+ciudad+'.json', 'w') as json_file:
			json.dump(climalocal, json_file)
	except requests.RequestException as e:
		learprint(f"Error al obtemer los datos {e}")
				   

if __name__ == "__main__" :

	ciudad="garin"
	url = "https://www.tiempo.com/"+ciudad+".htm"
	get_weather(url,ciudad)
	
