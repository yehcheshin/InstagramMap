import random
import json

from flask import request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from InstagramMap import app, line_bot_api, handler


from InstagramMap.utils.TSP import TSP

TSP_LineBot = TSP()


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    body_dict = json.loads(body)
    app.logger.info("Request body: " + body)
    print("---------------------------------------------")
   
    try:
        if body_dict["events"][0]["message"]["type"] == "location":
            TSP_LineBot.storeInfo["latitude"] = body_dict["events"][0]["message"]["latitude"]
            TSP_LineBot.storeInfo["longitude"] = body_dict["events"][0]["message"]["longitude"]
            print(body_dict["events"][0]["message"].get("title", "你所在的位置"))
        #     TSP_LineBot = TSP()
        #     TSP_LineBot.storeInfo["latitude"] = body_dict["events"][0]["message"]["latitude"]
        #     TSP_LineBot.storeInfo["longitude"] = body_dict["events"][0]["message"]["longitude"]
        #     TSP_LineBot.storeInfo["name"] = body_dict["events"][0]["message"]["title"]



        
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
def  Isfloat(text):
    try:
        return isinstance(float(text),float)
    except ValueError   : 
        return False

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    def reply(text):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))

    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        message = TextSendMessage(text=event.message.text)
        
        if message.text == "find restaurant": 
            reply("請輸入搜尋半徑（單位:km）")
        
        if Isfloat(message.text):
            TSP_LineBot.SetRadius(float(message.text))
            result = TSP_LineBot.AccessInRange()
            path = f'你選擇的搜尋距離是 {TSP_LineBot.radius} m\n 一共有{len(result)}家:\n'
            for i,store in enumerate(result):
                path += '{}. {}: {:.2f} m\n'.format(i+1,store[0],store[1])
            reply(path)
       

       