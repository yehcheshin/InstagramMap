from __future__ import unicode_literals

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from linebot import LineBotApi, WebhookHandler
from flask_migrate import Migrate

from InstagramMap.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db  =  SQLAlchemy(app)
# migrate = Migrate(app,db)
cfg = Config()
line_bot_api = LineBotApi(cfg.channel_access_token)
handler = WebhookHandler(cfg.channel_secret)


from InstagramMap import routes
