import requests

class disbot():

    def updateStats(self, clientid, token, serverCount:int):
        sendURL = f'https://disbot.top/api/v1/botupdate/{clientid}'
        body = {'serverCount': serverCount}
        header = {'authorization': token}
        success = requests.post(sendURL, data = body, headers=header)
        print(f"{success} We did it")
