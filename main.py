from config import api_Key
from crypto_exchange.model import Exchange

cambio = Exchange('NADA')
cambio.updateExchange(api_Key)
