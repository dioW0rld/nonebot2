from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import re
from bs4 import BeautifulSoup
import urllib.request
import sqlite3
import requests
import json

find_daytime=re.compile(r'<input id="hidden_title" type="hidden" value="(.*)">')
weather = on_command("天气", rule=to_me(), priority=100)

@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值

@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    code=dbscr(city)
    if code==0:
        await weather.finish(message=Message("没有这个城市哦"))
    else:
        city_weather = await get_weather(city,code)
        await weather.finish(message=Message(city_weather))

async def get_weather(city,code):

    t_url = "http://www.weather.com.cn/weather1d/"+code+".shtml#input"
    url=f'https://yiketianqi.com/api?unescape=1&version=v6&appid=87418573&appsecret=KQxr3DGd&cityid={code}'
    #f_data =geturl(url)
    r=geturl(url)
    if r['wea_img'] =='qing':
        image_url='[CQ:face,id=74]'
    if r['wea_img'] =='yu':
        image_url='[CQ:face,id=90]'
    if r['wea_img'] =='lei':
        image_url='[CQ:face,id=54]'
    if r['wea_img'] =='yun' or r['wea_img'] =='yin':
        image_url='[CQ:face,id=91]'
    if r['wea_img'] =='shachen' or r['wea_img'] =='bingbao':
        image_url='[CQ:face,id=190]'
    if r['wea_img'] =='xue' or r['wea_img'] =='wu':
        image_url='[CQ:face,id=41]'


    #return f"{city}的天气是{f_data}"

    return (f"今天是{r['date']} {r['city']}\n "
            f"天气 {r['wea']} {image_url}\n"
            f"今天的温度 {r['tem2']}~{r['tem1']}°C\n"
            f"现在温度是{r['tem']}°C 风向{r['win']} 风力等级{r['win_speed']} 风速{r['win_meter']}\n"
            f"湿度{r['humidity']} 能见度{r['visibility']} 空气质量{r['air']}\n"
            f"{r['air_tips']}")
def geturl(baseurl):

    html = parseuel(baseurl)
    return html
    #soup = BeautifulSoup(html, "html.parser")
    #for item in soup.find_all('input', id="hidden_title"):
        #item = str(item)
        #daytime = re.findall(find_daytime, item)
        #return daytime
def parseuel(url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'}

        req = requests.get(url, headers=header)

        r = req.json()
        return r


        #req = urllib.request.Request(url, headers=head)
        #res = urllib.request.urlopen(req)
        #html = res.read().decode('utf-8')
        #return html
def dbscr(state):
    datalist = []
    comm = sqlite3.connect('citycode.db')
    con = comm.cursor()
    sql = 'select * from citycode where keyword="%s"' % (state)
    sstate = con.execute(sql)
    for i in sstate:
        datalist.append(i)
    comm.commit()
    comm.close()
    if datalist==[]:
        #weather.reject("没有这个城市哦")
        return 0
    else:
        code=datalist[0][0]
        return code

