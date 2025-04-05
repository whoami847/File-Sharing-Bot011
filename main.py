# bot.py
from flask import Flask

class Bot:
    def __init__(self):
        self.app = Flask(__name__)
        
    def run(self):
        self.app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# main.py
from bot import Bot
Bot().run()
