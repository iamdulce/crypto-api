import requests #librería que me permite hacer llamadas a apis
from config import api_Key

r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={api_Key}') #Hago la llamada a la api
if r.status_code != 200: #asegura que la petición(200) sea valida y muestre el resultado si existe el dato (moneda) ingresad0
	raise Exception( "Error en consulta de assets:{}".format(r.status_code) )

lista_general= r.json() #obtengo todos los datos de cada moneda (crypto o no). Se guardan como una estructura de diccionario


lista_criptos=[]

for item in lista_general:
	if item["type_is_crypto"] == 1: #compruebo si el dato de cada moneda es de tipo crypto
		lista_criptos.append(item['asset_id']) #agrego esos datos en mi array vacío


moneda_cripto = input("Ingrese una criptomoneda conocida:").upper()

while moneda_cripto != "" and moneda_cripto.isalpha(): #mientras agreguen datos y no sean letras/letras+numero
	if moneda_cripto in lista_criptos:  #si la moneda ingresada está en mi array de solo criptos
		r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={api_Key}')
		resultado = r.json() 
		if r.status_code == 200: #llamo los datos específicos de la moneda y los muestro si están
			print( "{:,.2f}€".format(resultado["rate"]) )
		else:
			print(resultado["error"])
	moneda_cripto = input("Ingrese una criptomoneda conocida:").upper()