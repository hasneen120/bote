from telethon.tl.functions.account import UpdateProfileRequest
import datetime,time
from telethon.sync import TelegramClient,events
from telethon.sessions import StringSession
api_id = '21668705'
api_hash = '39c36792085322fd5ce73ccdbc62996d'
sessin ='1BJWap1wBu1p_lkv0-YDsDjZsXJ1vjxO5uY-raoKn5uzUALZPuQzKW2SB1nSddj-YzhCOz2Dvi0EU-Ugr7y2_KZ_FkSFTdb8mZlsXDMnU8jPQKA37EAb7VOUDeCgmY7G6YSvyPa6M9vusk_2kBUoH4sttX9nMZb4qWC0_Hw6my5PU9DcEOlGRBX07DLOYPLdIzvXHMec9VNJOBpOWax2CpU3YkoORnw2AXlNNR2hv0qZgwzZAQPCuWL26bfdfzdD-LWs9sbQS0vTkVSkFOjUEBah5qwMCKrH4srtnb2yuhVBbnSsisEUfGY0MEIBJZZShlzHvF1Bv2gnSEEFDn8WMPImweK4J59c='

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
