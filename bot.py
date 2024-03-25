import telegram
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6969784897:AAEOAz_SIZn_SJ5-UgTKb00NbPfiTa_YuE4'

# Define the admin user ID
ADMIN_ID = 7024083559  # Replace with the actual admin user ID

# Function to handle the /start command
def start(update, context):
    user_id = update.message.from_user.id
    if user_id == ADMIN_ID:
        context.bot.send_message(chat_id=update.message.chat_id, text="Bot started. Only admins can use /ban100.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Only admins can start the bot.")

# Function to handle the /ban100 command
def ban(update, context):
    user_id = update.message.from_user.id
    if user_id != ADMIN_ID:
        context.bot.send_message(chat_id=update.message.chat_id, text="Only admins can use this command.")
        return
    
    # Rest of the ban logic...

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ban100', ban))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
