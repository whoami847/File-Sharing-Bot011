import os
from bot import Bot

if __name__ == "__main__":
    # For web apps (e.g., Flask/Django): Add host/port configuration
    # app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))  # Example for Flask
    
    # For non-web workers (e.g., Discord bots/scripts):
    Bot().run()
