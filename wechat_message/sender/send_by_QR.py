#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
@ModuleName: 执行入口
@Author: zhangmeixian
@Date: 2022/06/25
参考博文链接:http://dushusir.com/wechat-automatically-sends-messages-on-time-in-python/
"""
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
from utils import logger
import time


class QRSender:
    """
    扫码登陆并发送消息
    """

    def __init__(self):
        # 注意是微信名称
        self.default_receiver = "zZz"

    def execute(self, receiver, msg, send_time=None):
        """
        执行入口
        :return:
        """
        if send_time is None:
            logger.info("send time not set")
            return
        bot = Bot()
        while True:
            # 获取当前时间
            time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if time_now == send_time:
                self.send_msg(receiver, msg, bot)
                break
            if time_now > send_time:
                logger.info("time passed")
                break

    def get_default_news(self):

        """获取金山词霸每日一句，英文和翻译"""
        url = "http://open.iciba.com/dsapi/"
        r = requests.get(url)
        content = r.json()['content']
        note = r.json()['note']
        return content, note

    def send_msg(self, receiver, msg, bot):
        # linux执行登陆请调用下面的这句
        # bot = Bot(console_qr=2,cache_path="botoo.pkl")
        try:
            if msg is None:
                msg = self.get_default_news()
            # 你朋友的微信名称，不是备注，也不是微信帐号。
            my_friend = bot.friends().search(receiver)[0]
            my_friend.send(msg)
            # 每86400秒（1天），发送1次
            # t = Timer(10, self.send_msg)
            # 为了防止时间太固定，于是决定对其加上随机数
            # ran_int = random.randint(0,100)
            # t = Timer(86400+ran_int,send_msg)

            # t.start()
        except Exception as e:
            logger.info("failed to send message for: {}".format(e))
            my_friend = bot.friends().search(self.default_receiver)[0]
            my_friend.send(u"消息发送失败了")
