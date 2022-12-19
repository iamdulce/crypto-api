from crypto_exchange.model import *
from config import api_Key

#creamos objeto de AllCoinApiIO
allcoint = AllCoinApiIO()
#ejecutar el metodo getCoins que consulta y carga lista de coins
allcoint.getCoins(api_Key)

print("La cantidad de criptos son {} ,\
		y la de no criptos son {}"\
		.format(len(allcoint.cryptos),len(allcoint.no_cryptos)))

crypto = input("Ingrese moneda digital conocida: ").upper()


while crypto != "" and crypto.isalpha():
	if crypto in allcoint.cryptos:
		exchange = Exchange(crypto)
		try:
			#si todo bien esto se ejecuta
			exchange.updateExchange(api_Key)
			print( "{:,.2f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

		except ModelError as error:# si falla imprime esto de aqui
			print(error)    


	crypto = input("Ingrese moneda digital conocida: ").upper()
