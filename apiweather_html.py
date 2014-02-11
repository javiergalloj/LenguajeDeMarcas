# -*- coding: utf-8 -*-
import os
import json
import requests
import webbrowser

provincias = ['Almería','Cádiz', 'Córdoba','Granada','Huelva','Jaen','Málaga','Sevilla']

html = open('tiempo.html','w')
html.write("""<!DOCTYPE html PUBLIC '-// W3C // DTD XHTML 1.0 Strict //EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='es' charset="utf-8">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta charset="UTF-8">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>EL TIEMPO</title>
</head>
<body>
<h1>EL TIEMPO EN ANDALUCIA<h1>""")

for provincia in provincias:
	html.write("<h2>%s</h2>" % provincia)
	pronostico = requests.get(url='http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincia})
	pronostico_prov = json.loads(pronostico.text)
	temp_min = pronostico_prov['main']['temp_min']
	temp_min = round (temp_min - 273,1)
	temp_max = pronostico_prov['main']['temp_max']
	temp_max = round (temp_max - 273,1)
	viento = pronostico_prov['wind']['speed']
	html.write('''<ul>
		<li>Temperatura mínima prevista: %s ºC.</li>
		<li>Temperatura máxima prevista: %s ºC.</li>
		<li>Viento: %s Km/h.</li>
		</ul>''' % (temp_min,temp_max,viento))

html.write("</body>")
html.write("</html>")
html.close()
webbrowser.open("tiempo.html")