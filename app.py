from flask import Flask, request
import requests
 
app = Flask(__name__)

# Access token from Facebook Developer console
PAGE_ACCESS_TOKEN = 'EAAIc354RjFQBAJmZAEunwtvnWzybYA74WyPVccJke8zF0GjWdpD8lZBfliVoUgAfT3MIBCcSQolJ0HpZBWQ9Em2hHYoyEH9MiooPEN5g3MV8uqmlDIc1tlyJUWRl2OWYOT3fRaif5EkxOD8Rl3Eofgke5uSLwMSoyVy9Gbn4yqQqCKJ5KYZAjc9ZAFIHsDfbaPFUM9lRobwZDZD'

# This is API key for facebook messenger.
API = "https://graph.facebook.com/LATEST-API-VERSION/me/messages?access_token="+PAGE_ACCESS_TOKEN


@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")== "<Your Verify token>":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200
 
if __name__ =='__main__':
    app.run()