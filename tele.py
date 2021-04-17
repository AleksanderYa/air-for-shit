from telethon.sync import TelegramClient
from telethon import functions, types
"""
from telethon.sync import TelegramClient, events

with TelegramClient('name', 1760301, "1d0b2fe62d66e00cddc89e84cab0b05d") as client:
   client.send_message('me', 'Hello, myself!')

   client.run_until_disconnected()
   exit()
"""



api_id = 1681640
api_hash = "628c84fccb38b488fb8d7e0d7588f8cd"
name = 'some'



with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.contacts.GetContactsRequest(
        hash=0
    ))
 
    #for i in result.stringify():
       # ii += 1
       # print(i)
       # if ii > 10:
         #   continue
    wr = open('text.txt', 'w')
    wr.writelines(result.stringify())
    wr.close