import logging
import subprocess
# List the modules
modules_to_install = ['python-telegram-bot', 'pyautogui']

# Iterate over the modules to install them using pip
for module in modules_to_install:
    subprocess.check_call(['pip', 'install', module])