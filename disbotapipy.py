import requests

def updateStats(clientid, token, serverCount):
    if(serverCount < 0):
        print("A server count must be sent by the bot")
    else:
        sendURL = f'https://disbot.top/api/v1/botupdate/{clientid}'
        auth = {'authorization': token}
        success = requests.post(sendURL, data = auth)
        print(f"{success} We did it")