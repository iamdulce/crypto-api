from crypto_exchange.model import AllCoinApiIO
from config import api_Key
#16156 de  16378 (222)

def test_todocoin():
    todo = AllCoinApiIO()
    assert isinstance(todo, AllCoinApiIO)
    todo.getCoins(api_Key)
    assert len(todo.criptos) == 16156
    assert len(todo.no_criptos) == 222