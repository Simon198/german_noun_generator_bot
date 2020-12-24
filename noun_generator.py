from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot
import os
import random

dir_path = os.path.abspath(os.path.dirname(__file__))

with open(dir_path + '/nouns.txt', 'rb') as file:
    nouns = file.read()
    nouns = nouns.decode('utf-8').split('\n')

with open(dir_path + '/TOKEN.txt', 'r') as file:
    token = file.read()

def welcome_message (update, context):
    update.message.reply_text('Guten Tag Freund')
    update.message.reply_text('Über den Befehl /generate kannst du fünf zufällig deutsche Nomen generieren.')

def generate_random_noun (update, context):
    num_nouns = 5
    if len(context.args) > 0:
        try:
            num_nouns = int(context.args[0])
        except:
            update.message.reply_text('Du musst eine Zahl hinter /generate eingeben')
            return

    random_nouns = random.sample(range(len(nouns)), num_nouns)

    for i, noun_index in enumerate(random_nouns):
        update.message.reply_text(str(i + 1) + ' - ' + nouns[noun_index])


def main ():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', welcome_message))
    dp.add_handler(CommandHandler('generate', generate_random_noun))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__': 
    main()