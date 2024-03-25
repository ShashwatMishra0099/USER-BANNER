import random
import telegram
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6969784897:AAEOAz_SIZn_SJ5-UgTKb00NbPfiTa_YuE4'

# Function to handle the /start command
def start(update, context):
    # Check if the user is an admin
    if update.message.from_user.id in context.bot.get_chat_administrators(update.message.chat_id):
        context.bot.send_message(chat_id=update.message.chat_id, text="Bot started. Only admins can use /ban100.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Only admins can start the bot.")

# Function to handle the /ban100 command
def ban(update, context):
    # Check if the user is an admin
    if update.message.from_user.id not in context.bot.get_chat_administrators(update.message.chat_id):
        context.bot.send_message(chat_id=update.message.chat_id, text="Only admins can use this command.")
        return
    
    # Get list of members in the group
    members = context.bot.get_chat_members_count(update.message.chat_id)
    
    # Generate random usernames and ban commands
    banned_users = random.sample(range(members), min(100, members))
    for user_id in banned_users:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"/ban {user_id}")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ban100', ban))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
