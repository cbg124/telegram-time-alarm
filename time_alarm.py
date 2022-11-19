import schedule
import time
import pytz
import datetime
import telegram

token="5721368729:AAFsOUr-z05gBXkXOCdfiOM-74cZyNnv-cc"
bot = telegram.Bot(token=token)
public_chat_name = '@k2022test'

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    now = time.localtime()
    id_channel = bot.sendMessage(chat_id=public_chat_name,
                             text="current time = " + str(now)).chat_id
    print(id_channel)
    print("current time = ", str(now))
    
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)