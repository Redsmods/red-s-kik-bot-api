# this is the example of how to make a command.
import logging
import sys

from kik_unofficial.datatypes.xmpp.chatting import *
import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.sign_up import RegisterResponse, UsernameUniquenessResponse
from kik_unofficial.datatypes.xmpp.login import LoginResponse
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
        print("you can now test out this simple bot example")
        
        # below is the normal command. simple prefix+command and hit send
         elif chat_message.body.lower() == prefix+"credits":
                self.client.send_chat_message(chat_message.from_jid, "This is a Simple Bot set up by Red./nThis wasnt tested so dont freak out if it has errors.")
            return
         # and below this is the command that sends txt files.
         elif chat_message.body.lower() == prefix+"help":
            with open("help/help.txt","r") as f:
                self.client.send_chat_message(chat_message.from_jid, f.read())
            return

if __name__ == '__main__':
    main()
