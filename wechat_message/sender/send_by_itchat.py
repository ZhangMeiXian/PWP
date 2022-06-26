#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
@ModuleName: 执行入口
@Author: zhangmeixian
@Date: 2022/06/25
参考博文链接:http://blog.itpub.net/31355641/viewspace-2676428/
"""
import schedule
import time
import itchat
from utils import logger


class ITSender:
    """
    通过itchat自动登陆并发送信息
    """

    def __init__(self):
        self.default_receiver = "zZz"

    def execute(self, receiver, msg, send_time=None):
        """
        执行入口
        :return:
        """
        if send_time is None:
            logger.info("send time not set")
            return
        # 自动登陆微信
        itchat.auto_login()
        while True:
            # 获取当前时间
            time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if time_now == send_time:
                self.send_msg(receiver, msg)
                break
            if time_now > send_time:
                logger.info("time has passed")
                break

    def send_msg(self, receiver, msg):
        """
        发送信息
        :return:
        """
        try:
            receiver = itchat.search_friends(name=receiver)
            itchat.send(msg, receiver[0]['UserName'])
            logger.info("send success")
            # # 在群里发送消息
            # myroom = itchat.search_chatrooms(name=receiver)  # 群
            # itchat.send_msg(msg, myroom[0]['UserName'])  # 群用户
        except Exception as e:
            logger.info("failed to send message: {}".format(e))
            receiver = itchat.search_friends(name=self.default_receiver)
            itchat.send(u"发送信息失败", receiver[0]['UserName'])

