#!/usr/bin/env python3
	
# wheater generator api
# created by @nerdemma https://github.com/nerdemma/wheater_api
	
import requests
from bs4 import BeautifulSoup
import json

data_details = []
data_list = []
wheater_list = []

def get_wheater_list(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	wl_counter=0
	
	principal = soup.find("ul",class_="princ-ciudades")
	lista = principal.find_all("span",class_="datos") 

	for listas in lista:
		wheater_location = listas.find("a")
		wheater_max_temperature = listas.find("span", class_="maxima")
		wheater_min_temperature = listas.find("span", class_="minima")
		wl_counter+=1
		
		#save to map
		data_w_list = {	
		"id": wl_counter,
		"ciudad": wheater_location.text.strip(),
		"maxima": wheater_max_temperature.text.strip(),
		"minima": wheater_min_temperature.text.strip()	
		}
		data_list.append(data_w_list)	
	
	
def get_wheater_details(url):
			page = requests.get(url)
			soup = BeautifulSoup(page.content, "html.parser")
			principal = soup.find("ul", class_="princ-ciudades")
			wheater = principal.find_all("img", class_="lazy") 		
			wd_counter=0
			
			for wheaters in wheater:
				wheater_info = wheaters.get("alt")
				
				wd_counter+=1
				
				#save to map
				data_w_details = {	
				"id": wd_counter,
				"estado": wheater_info,
				}
				data_details.append(data_w_details)	
	
#define variables
url = "https://www.tiempo.com/argentina.htm"
get_wheater_list(url)
get_wheater_details(url)	

for details in data_details:		
	details_id = details['id']
	ciudad = next((ciudad for ciudad in data_list if ciudad['id'] == details_id), None)
	if ciudad:
		wheater_info = {
		'estado': details['estado'],
		'ciudad': ciudad['ciudad'],
		'maxima': ciudad['maxima'],
		'minima': ciudad['minima']
		}
		wheater_list.append(wheater_info)

wheater_json = {'wheater':wheater_list}

with open('wheater_json.json', 'w') as json_file:
	json.dump(wheater_json, json_file, indent=4)
