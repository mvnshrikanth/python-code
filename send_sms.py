from twilio.rest import Client

# put your own credentials here
account_sid = "AC04d6a3eda87beefbd533362964883b68"
auth_token = "f56dc2285da27867023064cddafdeed4"

client = Client(account_sid, auth_token)

message = client.messages.create(
  to="+18607092564",
  from_="+18609474738",
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
    media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")
print(message.sid)
