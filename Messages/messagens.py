import telebot

def SendMessage(message):
    # Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
    bot_token = '5913009769:AAGXYwrzoEUK9KHXuxdpxtbPXOEhX3ElOfo'
    # Substitua 'CHANNEL_ID' pelo ID do canal onde você deseja enviar a mensagem
    channel_id = '-1002144207029'

    # Crie uma instância do bot
    bot = telebot.TeleBot(bot_token)

    # Envie a mensagem para o canal
    msg_id = bot.send_message(channel_id, message)

    # Imprima uma mensagem de sucesso
    print('Mensagem enviada com sucesso')
    
    return msg_id.message_id

def EditMessage(message_id, message):
    # Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
    bot_token = '5913009769:AAGXYwrzoEUK9KHXuxdpxtbPXOEhX3ElOfo'
    # Substitua 'CHANNEL_ID' pelo ID do canal onde você deseja enviar a mensagem
    channel_id = '-1002144207029'

    # Crie uma instância do bot
    bot = telebot.TeleBot(bot_token)

    # Envie a mensagem para o canal
    msg_id = bot.edit_message_text('message', channel_id, 19)

    # Imprima uma mensagem de sucesso
    print('Mensagem enviada com sucesso')