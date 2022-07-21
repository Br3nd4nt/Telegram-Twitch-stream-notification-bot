TOKEN = None
try:
    import os
    TOKEN = os.environ.get('TELEGRAM_TWITCH_BOT_TOKEN')
except Exception:
    pass
try:
    from boto.s3.connection import S3Connection
    TOKEN = S3Connection(os.environ['TELEGRAM_TWITCH_BOT_TOKEN'])
except Exception:
    pass


from telegram import Bot
bot = Bot(token=TOKEN)
