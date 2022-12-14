#CONTROLLER: comunica la vista y el model
from crypto_exchange.model import AllCoinApiIO,Exchange,ModelError,ExchangeReverse
from crypto_exchange.view import Views
from config import api_Key

class CryptoExchangeController:
	def executeProgram(self):
		allcoins = AllCoinApiIO() #Model: objeto que instancia AllCoinApiIO()
		allcoins.getCoins(api_Key) #ejecutar método que consulta y carga lista total de coins

		viewTools = Views() #View: objeto que instancia Views()
		viewTools.viewCoinsList(allcoins) #imprime en terminal

		crypto = viewTools.insertCoin() #input que pide crypto

		while crypto != "" and crypto.isalpha():
			if crypto in allcoins.cryptos: #compruebo si es criptomoneda de la lista
				exchange = Exchange(crypto) #Model: objeto que instancia Exchange()
				try: #ejecutar método updateExchange que carga los datos de la cripto específicada
					exchange.updateExchange(api_Key)
					viewTools.getRateExchange(exchange) #imprime en terminal el rate
				except ModelError as error:
					viewTools.getError(error) #imprime en terminal el error

			crypto = viewTools.insertCoin() #input que pide crypto

	#
	def executeProgram2(self):
		allcoins = AllCoinApiIO() #Model: objeto que instancia AllCoinApiIO()
		allcoins.getCoins(api_Key) #ejecutar método que consulta y carga lista total de coins

		viewTools = Views() #View: objeto que instancia Views()
		viewTools.viewCoinsList(allcoins) #imprime en terminal

		coin = viewTools.insertCoin() #input que pide moneda

		while coin != "" and coin.isalpha():
			if coin in allcoins.no_cryptos: #compruebo que sea una moneda normal de la lista
				exchange = ExchangeReverse(coin) #Model: objeto que instancia ExchangeReverse()
				try: #ejecutar método updateExchange que carga los datos de la moneda específicada
					exchange.updateExchange(api_Key)
					viewTools.getRateExchange(exchange) #imprime en terminal el rate
				except ModelError as error:
					viewTools.getError(error) #imprime en terminal el error

			coin = viewTools.insertCoin() #input que pide moneda