# bitcoin_rpc.py
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config

# Создаем объект для подключения к локальному Bitcoin узлу
rpc_connection = AuthServiceProxy(f"http://{config.rpc_user}:{config.rpc_password}@{config.rpc_host}:{config.rpc_port}")

def generate_new_address():
    """
    Функция для генерации нового адреса в криптовалютном кошельке
    """
    try:
        new_address = rpc_connection.getnewaddress()
        return new_address
    except JSONRPCException as e:
        print("Ошибка при генерации нового адреса:", e)
        return None

def get_wallet_balance():
    """
    Функция для получения баланса криптовалютного кошелька
    """
    try:
        balance = rpc_connection.getbalance()
        return balance
    except JSONRPCException as e:
        print("Ошибка при получении баланса кошелька:", e)
        return None
