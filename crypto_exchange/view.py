#VIEW: interacción con el usuario
class Views():
	def __init__(self):
		pass

	def insertCoin(self):
		coinName = input("Ingrese moneda conocida: ").upper()
		return coinName

	def viewCoinsList(self, allcoins):
		print("La cantidad de criptos son {} ,\
		y la de no criptos son {}"\
		.format(len(allcoins.cryptos),len(allcoins.no_cryptos)))

	def getRateExchange(self, exchange):
		print( "{:,.8f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

	def getError(self, error):
		print(error)
