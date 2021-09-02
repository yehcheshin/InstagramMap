from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    "zSNR6szFA8ZgIVI0ZFMEBUXKFBe/rJGkThJw2/VuVdPnwpHSi3b0K8WK3sUxFsyhbsAV2V2+KNqOp3GZ404Teyp5lfFLTdTeJ5HL6JFHzJ5Ec3+FTqbQ4Tt23UbB4CUwg+xZDRXSsippi7USrMn/2QdB04t89/1O/w1cDnyilFU="
    )
handler = WebhookHandler('b0ff8a5576668a0d05bbbf242785dd2f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
