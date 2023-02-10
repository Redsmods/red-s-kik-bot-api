import logging
import sys

from kik_unofficial.datatypes.xmpp.chatting import *
import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import SignUpError, LoginError
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse, PeersInfoResponse
from kik_unofficial.datatypes.xmpp.sign_up import RegisterResponse, UsernameUniquenessResponse
from kik_unofficial.datatypes.xmpp.login import LoginResponse, ConnectionFailedResponse
from kik_unofficial.datatypes.xmpp.xiphias import UsersResponse, UsersByAliasResponse
from typing import Union, List, Tuple

import time, re, datetime, requests, json, _thread, configparser
from bs4 import BeautifulSoup

from helper_funcs import *

config = configparser.ConfigParser()
config.read('config.ini')

username = config['REQUIRED']['username']
password = config['REQUIRED']['password']
device_id = config['REQUIRED']['device_id']
android_id = config['REQUIRED']['android_id']

super = config['REQUIRED']['super']
owner = config['REQUIRED']['owner']
prefix = config['REQUIRED']['prefix']

kik_bot_username = config['OPTIONAL']['kik_bot_username']
kik_bot_key = config['OPTIONAL']['kik_bot_api_key']


def main():
    bot = RedsCute()

class RedsCute(KikClientCallback):
    def __init__(self):
        self.client = KikClient(self, username, password,  device_id_override = device_id, android_id_override = android_id)

    def on_authenticated(self):
        print("Authenticated")
        ensure_bot(username)
        clear_captchas()
        _thread.start_new_thread( check_captchas, (self.client, username, ) )

    def on_login_ended(self, response: LoginResponse):
        print("Full name: {} {}".format(response.first_name, response.last_name))
        
         elif chat_message.body.lower() == prefix+"credits":
                self.client.send_chat_message(chat_message.from_jid, "This is a Simple Bot set up by Red./nThis wasnt tested so dont freak out if it has errors.")
            return

if __name__ == '__main__':
    main()
