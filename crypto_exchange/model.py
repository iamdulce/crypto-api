#MODEL: donde puedo acceder y actualizar la info
import requests

class ModelError(Exception):
	pass

class AllCoinApiIO:
	def __init__(self):
		self.cryptos = []
		self.no_cryptos = []

	def getCoins(self, api_Key):
		r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={api_Key}')
		if r.status_code != 200:
			raise ModelError( "Error en consulta de assets:{}".format(r.status_code))

		lista_general = r.json()
		for item in lista_general:
			if item['type_is_crypto'] == 1:
				self.cryptos.append(item['asset_id'])
			else:
				self.no_cryptos.append(item['asset_id'])

class Exchange:
	def __init__(self,crypto):
		self.crypto = crypto
		self.rate = None
		self.time = None
		self.r = None
		self.resultado = None

	def updateExchange(self,api_Key):
		self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.crypto}/EUR?apikey={api_Key}')
		self.resultado = self.r.json()
		if self.r.status_code == 200:
			self.rate = self.resultado['rate']
			self.time = self.resultado['time']
		else:    
			raise ModelError( f"status: {self.r.status_code} error: {self.resultado['error']} ")