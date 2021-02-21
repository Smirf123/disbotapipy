import requests

class disbot():

    def updateStats(self, clientid, token, serverCount:int):
        sendURL = f'https://disbot.top/api/v1/botupdate/{clientid}'
        body = {'serverCount': serverCount}
        header = {'authorization': token}
        success = requests.post(sendURL, data = body, headers=header)
        print(f"{success} We did it")
    def getVotes(self, clientid):
        url = f"https://disbot.top/api/v2/bot/{clientid}/getvotes"
        return(requests.get(url))
    def getInfo(self, clientid):
        url = f"https://disbot.top/api/v2/bot/{clientid}/get"
        return(requests.get(url))
