from crypto_exchange.model import AllCoinApiIO, Exchange, ModelError
from config import api_Key
#16156 de  16378 (222)

def test_todocoin():
	todo = AllCoinApiIO()
	assert isinstance(todo, AllCoinApiIO)
	todo.getCoins(api_Key)
	assert len(todo.cryptos) == 16156
	assert len(todo.no_cryptos) == 222

def test_cambio_ok():
	cambio = Exchange("ETC")
	assert cambio.rate is None#True
	assert cambio.time is None#True
	cambio.updateExchange(api_Key) #rate y time deberían después de hacer un llamdo exitoso
	assert cambio.rate > 0 #Que el valor de la  coin sea mayor a 0 si la llamada a la api va bien
	print(cambio.rate)
	assert isinstance(cambio.time,str)

def test_cambio_no_ok():
	noOk = Exchange("NADA")
	#conseguir comparar Resultado de la clase ModelError, consultar como lo hicimos en romanos
	#assert noOk.updateExchange(apiKey) ==  ModelError( f"status: {noOk.r.status_code} error: {noOk.resultado['error']} ")