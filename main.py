import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("SEU_TOKEN_AQUI")

# Banco de dados
saldos = {}


# Função Home
def home(chat_id): bot.send_message(chat_id, "O que deseja fazer?", reply_markup=menu_keyboard())


# Menu de opções
def menu_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ver saldo", callback_data="saldo"))
    markup.add(InlineKeyboardButton("Depositar", callback_data="depositar"))
    markup.add(InlineKeyboardButton("Sacar", callback_data="sacar"))
    markup.add(InlineKeyboardButton("Sair", callback_data="sair"))
    return markup


# Função de depósito
def depositar(message):
    chat_id = message.chat.id
    try:
        valor = float(message.text)
        if valor > 0:
            saldos[chat_id] += valor
            bot.send_message(chat_id, "Depósito realizado com sucesso!")
            home(chat_id)
        else:
            bot.send_message(chat_id, "Valor inválido. Digite um valor maior que 0.")
            home(chat_id)

    except ValueError:
        bot.send_message(chat_id, "Valor inválido. Digite um número.")
        home(chat_id)


# Função de saque
def sacar(message):
    chat_id = message.chat.id
    try:
        valor = float(message.text)
        if 0 < valor <= saldos[chat_id]:
            saldos[chat_id] -= valor
            bot.send_message(chat_id, "Saque realizado com sucesso!")
            home(chat_id)
        else:
            bot.send_message(chat_id, "Valor inválido ou saldo insuficiente.")
            home(chat_id)

    except ValueError:
        bot.send_message(chat_id, "Valor inválido. Digite um número.")
        home(chat_id)


# Manipulador de comandos
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    saldos[chat_id] = 0
    bot.send_message(chat_id, "Bem-vindo ao Banco Virtual!")
    home(chat_id)


# Manipulador de callbacks
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    data = call.data

    match data:
        case "saldo":
            bot.edit_message_text(f"Seu saldo é: R$: {saldos[chat_id]:.2f}", chat_id, call.message.id)
            home(chat_id)

        case "depositar":
            msg = bot.edit_message_text("Digite abaixo o valor que deseja depositar: ", chat_id, call.message.id)
            bot.register_next_step_handler(msg, depositar)

        case "sacar":
            msg = bot.edit_message_text("Digite abaixo o valor que deseja sacar: ", chat_id, call.message.id)
            bot.register_next_step_handler(msg, sacar)

        case "sair":
            bot.edit_message_text("Obrigado por usar nosso serviço!", chat_id, call.message.id)


bot.infinity_polling()
