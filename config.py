# © CodeXBotz

import os
import logging
import time
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from pyrogram.errors.exceptions.flood_ import FloodWait


# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7433238930:AAEUv4hrv5CWrcLCaNxE-_bAXF2YiefEbm4")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29580054"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8c12aad7243d77767ad428e01b630034")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002059027303"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5057842745"))

# Port
PORT = int(os.environ.get("PORT", "8080"))

# Database URI
DB_URI = "mongodb+srv://devhub:Fes9abgab9@testcluster0.d78tek8.mongodb.net/?retryWrites=true&w=majority&appName=testCluster0"
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Short link configuration
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "48ec4a68cf9755089d39300e8395d49a9db2be8f")

# Verify settings
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400))  # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "2059027303/4")

# Force sub channel id, if you want to enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002144945669"))

# Number of workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nMy First Message")

# Admins list
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "5057842745").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me.\n\nKindly please join the Channel.</b>")

# Custom caption for files
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

# Protect content from forwarding
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Disable share button for channel posts
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# Reply text for user messages
USER_REPLY_TEXT = "❌ Don't send me messages directly. I'm only a File Share bot!"

# Add OWNER_ID and additional admin ID to ADMINS list
ADMINS.append(OWNER_ID)

# Logging configuration
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,  # 50 MB
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


# Function to get logger instance for different modules
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# Initialize the Pyrogram Client
bot = Client(
    "my_bot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=TG_BOT_TOKEN,
    workers=TG_BOT_WORKERS
)


# Example function where you handle messages or media sending
def send_message_or_media():
    try:
        # Your message or media sending logic here
        # Example: bot.send_message(chat_id, text)
        # Example: bot.send_photo(chat_id, photo)
        pass
    except FloodWait as e:
        wait_seconds = e.x  # Access the wait time in seconds
        logging.warning(f"Telegram FloodWait: Waiting for {wait_seconds} seconds.")
        time.sleep(wait_seconds)  # Wait for the specified time
        send_message_or_media()  # Retry the action after waiting
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        # Handle other exceptions as needed


# Start the bot
if __name__ == "__main__":
    bot.run()
