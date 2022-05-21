# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 10:17
# @Author  : BYF
# @Email   : 3041733218@qq.com
# @File    : send_image.py
# @Software: PyCharm

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message,MessageSegment


import requests
from urllib.parse import quote
import asyncio

senddd=on_command('来点好看的',rule=to_me(),priority=30)


@senddd.handle()
async def send_tu(bot: Bot, event: Event, state: T_State):
    #loop = asyncio.get_event_loop()
    #task = loop.create_task(main())
    #loop.run_until_complete(task)
    url1='https://c-ssl.duitang.com/uploads/blog/202106/22/20210622201414_46017.jpg'
    url='https://pics1.baidu.com/feed/d8f9d72a6059252d0bd23c49f54a9e3d59b5b98a.jpeg'
    #await send.finish(Message(MessageSegment.image(file=url)))
    ms=f'[CQ:image,file={url},type=show,id=40000]'
    await senddd.finish(Message(ms))


async def main():
    world='樱岛麻衣'
    world=quote(world)
    page=1
    url_list=[]
    for i in range(1,page+1):
        url_list.append(f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8677882260006934699&ipn=rj&ct=201326592&is=&fp=result&fr=&word={world}&queryWord={world}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={i*30}&rn=30&gsm=1e&1648040041418=')
    return await parse(url_list)
async def getdata(data):

    datalist=[]
    for item in data['data']:
        if item:
            datalist.append(item['thumbURL'])

    print('1')
    return datalist

async def parse(url_list):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1648121168265_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCwzLDEsNSw2LDQsOCw3LDIsOQ%3D%3D&ie=utf-8&sid=&word=%E8%BF%AA%E8%BF%A6%E5%A5%A5%E7%89%B9%E6%9B%BC%E5%9B%BE%E7%89%87'
            }
    for i in url_list:
        req=requests.get(i,headers=head)
        return await getdata(req.json())

