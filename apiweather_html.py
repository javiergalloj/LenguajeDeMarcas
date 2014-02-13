# -*- coding: utf-8 -*-
import os
import json
import requests
import webbrowser
import jinja2

def orientacion (direccion):
	if direccion == 0:
		return 'N'
	if direccion > 0 and direccion < 90:
		return 'NE'
	if direccion == 90:
		return 'E'
	if direccion > 90 and direccion < 180:
		return 'SE'
	if direccion == 180:
		return 'S'
	if direccion > 180 and direccion < 270:
		return 'SO'
	if direccion == 270:
		return 'O'
	if direccion > 270 and direccion < 360:
		return 'NO'


provincias = ['Almería','Cádiz', 'Córdoba','Granada','Huelva','Jaen','Málaga','Sevilla']

for provincia in provincias:
	pronostico = requests.get(url='http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincia})
	pronostico_prov = json.loads(pronostico.text)
	temp_min = pronostico_prov['main']['temp_min']
	temp_min = round (temp_min - 273,1)
	temp_max = pronostico_prov['main']['temp_max']
	temp_max = round (temp_max - 273,1)
	viento = pronostico_prov['wind']['speed']
	viento = round (viento*1.609,0)
	direccion = int(pronostico_prov['wind']['deg'])
	direccion = orientacion(direccion)
	print temp_min
	print temp_max
	print viento
	print direccion

webbrowser.open("tiempo.html")
