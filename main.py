# Importing the basic modules
import logging
import subprocess
import time

# List of modules required for this to work
modules_to_install = ['python-telegram-bot', 'pyautogui']
# Putting it in a try, except block
try:
    # Iterate over the modules to install them using pip
    for module in modules_to_install:
        subprocess.check_call(['pip', 'install', module])
except e as Exception:
    print(e)

