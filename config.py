import os, time

class Config(object):
    #Audio-_edit_bot client Config 
    API_ID = os.getenv("API_ID", "21740783")
    API_HASH = os.getenv("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7496680438:AAHyEZDGnIoARpfywrzQOhB27un9pja49p4")

    #port to run web server
    PORT = int(os.getenv('PORT', "8080"))

    # other configs
    BOT_UPTIME  = time.time()

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))
