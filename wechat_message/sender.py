#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
@ModuleName: 执行入口
@Author: zhangmeixian
@Date: 2022/06/25
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import argparse
from utils import logger
from sender.send_by_QR import QRSender
from sender.send_by_itchat import ITSender

__all__ = [
    'main',
]


def main():
    """
    主程序入口
    :return:
    """
    try:
        parser = argparse.ArgumentParser()
        senders = ("QRSender", "ITSender")
        parser.add_argument('--sender', type=str, default="ITSender", help="sender in {}".format(senders))
        parser.add_argument('--receiver', type=str, default="zZz", help="receiver you want to send to")
        parser.add_argument('--content', type=str, default=None, help="message you want to send to")
        parser.add_argument('--time', type=str, default=None, help="time you want to sent message to, "
                                                                   "e.g. 2022-06-01 22:00:00")
        args = parser.parse_args()
        sender = args.sender
        if sender not in senders:
            logger.error("wrong sender choice")
        if sender == "QRSender":
            # 扫码发送信息
            QRSender().execute(receiver=args.receiver, msg=args.content, send_time=args.time)
        elif sender == "ITSender":
            # 自定义发送信息
            ITSender().execute(receiver=args.receiver, msg=args.content, send_time=args.time)
        else:
            logger.info("you can define the sender by yourself")
    except Exception as e:
        logger.error(str(e))


if __name__ == "__main__":
    main()