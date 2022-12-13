import requests

api_Key = '8B30787E-E140-44C4-B21A-E093FB2DAE75'
moneda_crypto = input("Ingrese una criptomoneda conocida: ").upper()


while moneda_crypto != "" and moneda_crypto.isalpha():
	r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_crypto}/EUR?apikey={api_Key}') 
	#capturo datos del json de la api
	
	resultado = r.json() 
	#guardo los datos (en forma de diccionario)

	if r.status_code == 200:
		print ('{:,.2f}€'.format(resultado['rate']))
	else:
		print(resultado['error'])
	#la petición(200) es valida y muestra el resultado si existe la moneda ingresada

	moneda_crypto =input('Ingrese una criptomoneda conocida: ').upper()