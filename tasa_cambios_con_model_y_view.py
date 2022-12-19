'''
Este archivo funcionaría como el CONTROLLER porque comunica la vista y el model 
(faltaría convertir en clase para poder ejecutar desde main) => LLEVAR A ARCHIVO CONTROLLER
'''

from crypto_exchange.model import AllCoinApiIO,Exchange,ModelError
from crypto_exchange.view import Views
from config import api_Key

#Model: creamos objeto de AllCoinApiIO()
allcoins = AllCoinApiIO()
#ejecutar el metodo getCoins que consulta y carga lista total de coins
allcoins.getCoins(api_Key)

#View: creamos objeto de Views()
viewTools = Views()

viewTools.viewCoinsList(allcoins)

crypto = viewTools.insertCoin()


while crypto != "" and crypto.isalpha():
	if crypto in allcoins.cryptos: #compruebo si es criptomoneda de la lista
		exchange = Exchange(crypto) #Model: se crea objeto de Exchange
		try:
			#ejecutar método updateExchange que carga los datos de la moneda específicada
			exchange.updateExchange(api_Key)
			viewTools.getRateExchange(exchange)

		except ModelError as error:# si falla imprime esto de aqui
			viewTools.getError(error)

	crypto = viewTools.insertCoin()
