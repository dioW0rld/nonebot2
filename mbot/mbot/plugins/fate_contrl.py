# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 21:03
# @Author  : BYF
# @Email   : 3041733218@qq.com
# @File    : fate_contrl.py
# @Software: PyCharm

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import time
import sqlite3


fate=on_command('抽签',rule=to_me(),priority=40)

@fate.handle()
async def fate_con(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    now=time.strftime("%S", time.localtime())
    now=float(now)*6.4
    id=str(event.get_user_id())
    if now==0:
        now=1
    end=await findfate(int(now))
    await fate.send(Message(f'[CQ:at,qq={id}]{end}'))

async def findfate(tiem):
    time=tiem
    scr=''
    datalist=scr_fate(time)
    for item in datalist:
        scr=scr+f'{item[1]}签:\n' \
                f'-------------------------------------------------\n' \
                f'{item[2]}\n' \
                f'{item[3]}'
    return scr

def scr_fate(time):
    data=[]
    con=sqlite3.connect('zhuge.db')
    cur=con.cursor()
    f_f=cur.execute("select * from zhuge where id=('%s')"%time)
    for i in f_f:
        data.append(i)
    con.commit()
    con.close()
    return data

