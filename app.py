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


import requests
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['AccessToken'])
handler = WebhookHandler(os.environ['ChannelSecret'])


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

def get_stock_price(stock):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock}.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"

    resp = requests.get(url)
    data = resp.json()

    stock_price = data['chart']['result'][0]['meta']['regularMarketPrice']
    return stock_price


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    stocks = {
        '3008': "大立光",
        '2330': "台積電",
        '1216': "統一"
    }

    text = event.message.text
    if text in stocks:
        stock_price = get_stock_price(text)
        content = f'{text} {stocks[text]} 目前股價為: {stock_price}'
    else:
        content = '請輸入要查詢的股票代號：(1216 統一, 2330 台積電, 3008 大立光)'

    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))


if __name__ == "__main__":
    app.run()
