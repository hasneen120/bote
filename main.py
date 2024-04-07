from telethon.tl.functions.account import UpdateProfileRequest
import datetime,time
from telethon.sync import TelegramClient,events
from telethon.sessions import StringSession
api_id = '21668705'
api_hash = '39c36792085322fd5ce73ccdbc62996d'
sessin = input(' Enter Your Session')

with TelegramClient(StringSession(sessin), api_id, api_hash) as client:
	print(client.session.save())
    
    
@client.on(events.NewMessage)
async def upd_name(event):
	while True:
		now = datetime.datetime.now()
		n = now.strftime("%l:%M %p")
		await client(UpdateProfileRequest(first_name=n))
		time.sleep(60)
client.start()
client.run_until_disconnected()
