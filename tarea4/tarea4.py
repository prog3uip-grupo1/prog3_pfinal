from kivy.network.urlrequest import UrlRequest
import json
import tarea3

def request():
	ul = tarea3.urls  # link base de datos 
	data =UrlRequest(ul,mostrar)	
	print (resultado) #traeria todos los datos del url en formato json
	data = json.loads(data.decode()) if not isinstance(data, dict) else data
	# faltataria recorrer  y asiganr la que traiga resultado
def requestConParametro(id):
	ul = tarea3.urls  
	resultado =UrlRequest(ul, id,mostrar)# si el url pide un parametro 
	print (resultado) #traeria todos los datos del url en formato json
	# faltataria recorrer  y asiganr la que traiga resultado

def mostrar(req, results): # mostrar la data
	for key, value in results['weather'][0].items():
		print(key, ': ', value)