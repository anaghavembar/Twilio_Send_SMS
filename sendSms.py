from twilio.rest import Client
from credentials import account_sid,auth_token,my_cell,my_twilio

client=Client(account_sid,auth_token)

mymsg="Hi how are you"

message=client.messages.create(to=my_cell,from_=my_twilio,body=mymsg)
