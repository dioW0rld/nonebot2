# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 15:33
# @Author  : BYF
# @Email   : 3041733218@qq.com
# @File    : station.py
# @Software: PyCharm

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import sqlite3
import time
from urllib import parse
import requests
import re
from bs4 import BeautifulSoup


find_fromTime=re.compile(r'<div class="time">(.*?)</div>')
find_fromStation=re.compile(r'<div class="station">(.*?)</div>')
find_time=re.compile(r'<div class="haoshi">(.*?)</div>')
find_train=re.compile(r'<div class="checi">(.*?)<i class="ifont-cert">')
find_endTime=re.compile(r'<div class="to"><div class="time">(.*?)<!-- --> ')
find_endStation=re.compile(r'<div class="station">(.*?)</div></div>')
find_price=re.compile(r'<div class="price">(.*?)</div>')


station=on_command('查询',rule=to_me(),priority=20)

@station.handle()
async def first_recive(bot: Bot, event: Event, state: T_State): ##获取用户输入的信息  赋值
    args = str(event.get_message()).strip()# 首次发送命令时跟随的参数，例：/查询 安阳 北京
    args=args.split("/")
    if len(args)<2:
        await station.finish(message=Message('宝贝♥，输入的不对哦!'))
    elif len(args)==2:
        state["from"] = args[0]  # 如果用户发送了参数则直接赋值
        state["end"] = args[1]
        state["date"] = ''
    else:
    #if args:
        state["from"] = args[0]
        state["end"] =args[1]
        state["date"]=args[2]


@station.got("from", prompt="哪个城市？") ##  只获得指令 无查找的信息  重新输入赋值
async def handle_city(bot: Bot, event: Event, state: T_State):
    from_f= state["from"]
    end_d=state['end']
    date=state["date"]

    datalist=scrStation(from_f,end_d)
    if len(datalist)!=2:
         await station.finish(message=Message("没有这个城市哦!"))
    else:
         ifo = await parserCity(from_f,end_d,date)
         if ifo=='':
             await station.finish(message=Message('没有车车了哦！宝♥'))
         else:
            await station.finish(message=Message(ifo))

async def parserCity(f,e,d):    ##对返回的车次信息格式化进行输出
    f_f=parse.quote(parse.quote(f))
    e_e = parse.quote(parse.quote(e))  ##车站名称编码
    if d=='':
        daytime=time.strftime("%Y-%m-%d",time.localtime())  ##获取当天时间
    else:
        daytime=d
    url = f'https://trains.ctrip.com/webapp/train/list?ticketType=0&dStation={f_f}&aStation={e_e}&dDate={daytime}&rDate=&trainsType=gaotie-dongche&hubCityName=&highSpeedOnly=0'
    html=geturl(url)
    end=getdata(html)
    if end =='':
        return ''
    else:
        ssr=''
        flag=0
        for item in end:
            ssr=ssr+f'始: {item[1]}{item[0]}-->终: {item[5]}{item[4]} 历时{item[2]} 车次{item[3]}'+'\n'
            flag+=1
            if flag==25:
                break
        return ssr
def getdata(html):     ##获取所有车次信息
    datalist = []
    soup = BeautifulSoup(html, 'html.parser')
    for items in soup.find_all('div', class_="card-white list-item"):   ##查找所有
        data = []
        item = str(items)
        # print(item)
        from_Time = re.findall(find_fromTime, item)
        if from_Time != []:
            data.append(from_Time[0])

        from_Station = re.findall(find_fromStation, item)
        if from_Station != []:
            data.append(from_Station[0])

        extime = re.findall(find_time, item)
        if extime != []:
            data.append(extime[0])

        train = re.findall(find_train, item)
        if train != []:
            data.append(train[0])

        end_Time = re.findall(find_endTime, item)
        if end_Time != []:
            data.append(end_Time[0])

        end_Station = re.findall(find_endStation, item)
        if end_Station != []:
            data.append(end_Station[1])

        price = re.findall(find_price, item)
        if price != []:
            data.append(price[0])
        if len(data) == 7:
            datalist.append(data)
    return datalist
def geturl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'
        }
    req = requests.get(url, headers=headers)
    return req.text

def scrStation(f,e):  ##数据库查找车站 是否存在车站
    datalist=[]
    con=sqlite3.connect('station.db')
    cur=con.cursor()
    sql='select * from station where name="%s"' % (f)
    f_station=cur.execute(sql)
    for i in f_station:
        datalist.append(i)
    sql1 = 'select * from station where name ="%s"' % (e)
    end_station=cur.execute(sql1)
    for i in end_station:
        datalist.append(i)
    con.commit()
    con.close()
    return datalist
