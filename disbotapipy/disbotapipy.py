import requests

class disbot():

    def updateStats(self, clientid, token, serverCount):
        if(serverCount < 0):
            print("A server count must be sent by the bot")
        else:
            sendURL = f'https://disbot.top/api/v1/botupdate/{clientid}'
            body = {'serverCount': serverCount}
            header = {'authorization': token}
            success = requests.post(sendURL, data = body, headers=header)
            print(f"{success} We did it")