import random
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6969784897:AAEOAz_SIZn_SJ5-UgTKb00NbPfiTa_YuE4'

# Define the admin user ID
ADMIN_ID = 7024083559  # Replace with the actual admin user ID

# Function to handle the /start command
def start(update, context):
    if update.message.from_user.id == ADMIN_ID:
        context.bot.send_message(chat_id=update.message.chat_id, text="Bot started. Only admins can use /ban.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Only admins can start the bot.")

# Function to handle the /ban command
def ban(update, context):
    if update.message.from_user.id != ADMIN_ID:
        context.bot.send_message(chat_id=update.message.chat_id, text="Only admins can use this command.")
        return

    # Check if a parameter is provided
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.message.chat_id, text="Please specify the number of bans.")
        return

    # Get the number of bans
    try:
        num_bans = int(context.args[0])
    except ValueError:
        context.bot.send_message(chat_id=update.message.chat_id, text="Invalid number. Please specify an integer.")
        return

    # Start typing
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

    # Get list of members in the group
    members = context.bot.get_chat_members(update.message.chat_id)
    member_usernames = [member.user.username for member in members if member.user.username is not None]

    # Generate and send ban messages
    for _ in range(num_bans):
        if member_usernames:
            username = random.choice(member_usernames)
            context.bot.send_message(chat_id=update.message.chat_id, text=f"/ban@{username}")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="No members found in the group.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ban', ban))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
