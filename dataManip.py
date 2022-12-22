import json




def extractResponseMessageFromMessageContent(response):
    messageObjectList = response.split("\n\n")
    print(messageObjectList)
