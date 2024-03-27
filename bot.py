# bot.py
import config
import telebot
from bitcoin_rpc import generate_new_address, get_wallet_balance

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я бот для работы с криптовалютным кошельком.")

@bot.message_handler(commands=["getnewaddress"])
def get_new_address(message):
    try:
        new_address = generate_new_address()
        if new_address:
            bot.reply_to(message, f"Новый адрес создан: {new_address}")
        else:
            bot.reply_to(message, "Произошла ошибка при создании нового адреса.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

@bot.message_handler(commands=["getbalance"])
def get_balance(message):
    try:
        balance = get_wallet_balance()
        if balance is not None:
            bot.reply_to(message, f"Баланс вашего кошелька: {balance} BTC")
        else:
            bot.reply_to(message, "Произошла ошибка при получении баланса кошелька.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


if __name__ == '__main__':
    bot.infinity_polling()
