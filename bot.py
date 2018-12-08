#!/usr/bin/env python

from irc import *
from sqrt import *
import time
import re
import base64
import string


def init(server, channel, nickname, testchannel):
    irc.connect(server)
    irc.nickuser(nickname)
    time.sleep(2)
    irc.channel(testchannel)
    irc.send(chan=testchannel, msg='Startup completed')


def refresh():
    text = irc.get_text()
    print(text)
    return text


def eq1():
    irc.send(chan=channel, msg='!ep1')
    text = refresh()
    m = re.search('([0-9]*)\s/\s([0-9]*)', str(text))
    if m is not None:
        print('[+] ' + str(m))
        print('[+] Match numbers ' + m.group(0))
        num1 = float(m.group(1))
        print(num1)
        num2 = float(m.group(2))
        print(num2)
        num3 = calc(num1, num2)
        print(num3)
        forge = '!ep1 -rep ' + str(num3)
        irc.send(chan=testchannel, msg=forge)
        irc.send(chan=channel, msg=forge)


def eq2():
    irc.send(chan=channel, msg='!ep2')
    text = refresh()
    m = re.search('(?<= botep \:)(.*)', str(text))
    print(m)
    if m is not None:
        try:
            print('[+] catched ' + str(text))
            decode = base64.b64decode(str(m.group(1)))
            print('[+] Decoded string ' + str(decode) + ' From ' + str(m.group(1)))
            forge = '!ep2 -rep ' + str(decode)
            print('[+] Sending back ' + str(forge))
            irc.send(chan=testchannel, msg=forge)
            irc.send(chan=channel, msg=forge)
            time.sleep(5)
        except:
            time.sleep(1)


def eq3():
    irc.send(chan=channel, msg='!ep3')
    text = refresh()
    m = re.search('(?<= botep \:)(.*)', str(text))
    print(m)
    if m is not None:
        try:
            rot13 = string.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
            decode = string.translate(str(m.group(1)), rot13)
            forge = '!ep3 -rep ' + str(decode)
            print('[+] Sending back ' + str(forge))
            irc.send(chan=testchannel, msg=forge)
            irc.send(chan=channel, msg=forge)
            time.sleep(5)
        except:
            time.sleep(1)


def eq4():
    time.sleep(1)


irc = IRC()
channel = "candy"
testchannel = "#testit"
server = "irc.root-me.org"
nickname = "botep"
init(server, channel, nickname, testchannel)

try :
    while 1:
        text = refresh()
        if text.find('PINGtest') != -1:
            irc.send(chan=testchannel, msg='pong')
        if text.find('eq1start') != -1:
            eq1()
        if text.find('eq2start') != -1:
            eq2()
        if text.find('eq3start') != -1:
            eq3()
        if text.find('eq4start') != -1:
            eq4()
except KeyboardInterrupt:
    print('\n[+] Closing bot')
