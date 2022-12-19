from crypto_exchange.model import AllCoinApiIO, Exchange, ModelError
from config import api_Key
import pytest
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
	print(cambio.time)
	#para ver los prints en consola puedo usar pytest -s

def test_cambio_no_ok():#para esta es cuando necesito importar pytest, y poder capturar el error
	noOk = Exchange("NADAdhajkf")
	#assert noOk.updateExchange(api_Key) ==  ModelError( f"status: {noOk.r.status_code} error: {noOk.resultado['error']} ")

	with pytest.raises(ModelError) as exceptionInfo:
		noOk.updateExchange(api_Key)
	
	assert str(exceptionInfo.value) == "status: 550 error: You requested specific single item that we don't have at this moment. "