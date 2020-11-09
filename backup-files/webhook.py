import requests
import json

channelID = "754713894135660588" # enable dev mode on discord, right-click on the channel, copy ID
botToken = "your token"   # get from the bot page. must be a bot, not a discord app

baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }

message = "363358736820994058"

POSTedJSON = json.dumps({"content": message})

r = requests.post(baseURL, headers=headers, data=POSTedJSON)
