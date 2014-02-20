# -*- coding: utf-8 -*-
import os
import json
import requests
import webbrowser
from jinja2 import Template

def orientacion (direccion):
	if (direccion > 337.5 and direccion <= 360) or (direccion >= 0 and direccion < 22.5):
		return 'N'
	if direccion >= 22.5 and direccion <= 67.5:
		return 'NE'
	if direccion > 67.5 and direccion < 112.5:
		return 'E'
	if direccion >= 112.5 and direccion <= 157.5:
		return 'SE'
	if direccion > 157.5 and direccion < 202.5:
		return 'S'
	if direccion >= 202.5 and direccion <= 247.5:
		return 'SO'
	if direccion > 247.5 and direccion < 292.5:
		return 'O'
	if direccion >= 292.5 and direccion <= 337.5:
		return 'NO'


provincias = ['Almeria','Cadiz', 'Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
plantilla = open('plantilla.html','r')
salidahtml = open('salidahtml.html','w')
html = ''

for linea in plantilla:
	html += linea

for provincia in provincias:
	pronostico = requests.get(url='http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincia})
	pronostico_prov = json.loads(pronostico.text)
	temp_min = pronostico_prov['main']['temp_min']
	temp_min = round (temp_min - 273,1)
	temp_max = pronostico_prov['main']['temp_max']
	temp_max = round (temp_max - 273,1)
	viento = pronostico_prov['wind']['speed']
	viento = round (viento*1.609,0)
	direccion = pronostico_prov['wind']['deg']
	direccion = orientacion(direccion)
	salida = Template(html)
	salida = salida.render(provincia = provincia, temp_min = temp_min, temp_max = temp_max, viento = viento, direccion = direccion)
	salidahtml.write(salida)


webbrowser.open("salidahtml.html")