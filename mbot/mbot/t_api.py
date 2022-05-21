from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event


import re
from bs4 import BeautifulSoup
import urllib.request


find_daytime=re.compile(r'<input id="hidden_title" type="hidden" value="(.*)">')
weather = on_command("天气", rule=to_me(), priority=5)

@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值

@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    city = state["city"]
    if city not in ["登封", "郑州"]:
        await weather.reject("你想查询的城市暂不支持，请重新输入！")
    city_weather = await get_weather(city)
    await weather.finish(city_weather)

async def get_weather(city: str):
    t_url = "http://www.weather.com.cn/weather1d/101180104.shtml#input"
    f_data = geturl(t_url)

    return f"{city}的天气是{f_data}".format(city,f_data)

def geturl(baseurl):
    html = parseuel(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('input', id="hidden_title"):
        item = str(item)
        daytime = re.findall(find_daytime, item)
        print(daytime)
        return daytime


def parseuel(url):
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'}
        req = urllib.request.Request(url, headers=head)

        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')

        return html