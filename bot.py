#import os
from flask_restful import Flask, request, redirect
#from twilio.rest import Client

app = Flask(__name__)

#this doesn't actually run anything. We are using Cloud Functions to run the actual backend
@app.route("/", methods=["GET", "POST"])
def process(request):
    audio = request.values.get('MediaUrl0', None)
    print(type(audio))
    if audio == None:
        #audio = request.values.get('Body', None)
        audio = "Please send a voice message in order for AnotherTake to work its magic."
    from twilio.twiml.messaging_response import MessagingResponse
    resp = MessagingResponse()
    #resp.message("Welcome to AnotherTake! This bot does not have any musical ability yet, sadly.")
    resp.message(audio)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

'''
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Welcome to AnotherTake!",
    from_="+19034209599",
    to="+14702333985"
)

print(message.sid)
'''
