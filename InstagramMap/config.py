import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class Config:
    
    channel_access_token = config.get('line-bot', 'channel_access_token')
    channel_secret = config.get('line-bot', 'channel_secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL','SQLALCHEMY_DATABASE_URI')
   
    
   
