# -*- coding: utf-8 -*-
import os
import json
import requests
os.system("clear")
provincias = ['1. Almería','2. Cádiz', '3. Córdoba','4. Granada','5. Huelva','6. Jaen','7. Málaga','8. Sevilla']
for provincia in provincias:
	print provincia

print ""
prov_peticion = (int(raw_input("Teclea el número de la provincia que desea conocer el tiempo: "))-1)
os.system("clear")
print "El tiempo para",provincias[prov_peticion][3:],"es el siguiente:"
pronostico = requests.get(url='http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincias[prov_peticion][3:]})
print pronostico.text