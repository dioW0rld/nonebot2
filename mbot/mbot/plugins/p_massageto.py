from nonebot.plugin import on_message
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.plugin import on_command, export
from nonebot.adapters.cqhttp.message import Message
from nonebot.typing import T_State


fuck=on_command('傻逼')

@fuck.handle()
async def fuck__f(bot: Bot, event: Event, state: T_State):

     id='15633554'
     await fuck.send(Message(f'[CQ:at,qq={id}]傻逼'))













#
# #from nonebot.adapters.cqhttp import Message
# from nonebot import on_keyword
# from nonebot.typing import T_State
# #from nonebot.adapters import Bot, Event
#
# eng=on_keyword('测试')
#
# eng.handle()
# async def eng_hh(bot: Bot, event: Event, state: T_State):
#     await eng.send(Message(f'[CQ:at,qq={event.get_user_id()}],wwwwwwwwwwww'))
#
# @eng.got('hh')
# async def FF(bot: Bot, event: Event, state: T_State):
#     await eng.send(Message(f'[CQ:at,qq={event.get_user_id()}]wowowwowo'))
#
#
#













# msg = on_command('test', priority=50)
#
#
# @msg.handle()
# async def f_l(bot: Bot, event: Event):
#     user_msg = str(event.get_message()).strip()
#     a=user_msg.split()
#     user_msg="".join(a)
    # if user_msg=='test':
    # id=str(event.get_user_id())
    # at2="[CQ:at,qq={}]".format(2928442872)
    # at_="[CQ:at,qq={}]".format(id)
    # ms=at_+'我你'
    # print('dasd')
    # ms1=at2+'sb'
    #seq= MessageSegment.image({"type":"image","data":{'file':'66.jpg'}})

    #seq =f'[CQ:image,file=]'

    # await msg.send(Message(user_msg))
    #await msg.finish(message=Message(seq))
    # await msg.send('woaini')
# from nonebot.adapters.cqhttp import Bot, Event
# from nonebot.plugin import on_message
#
#
# #自定义回复词典
# reply_dic = {
#     '您好': '你也好' ,
#     '早上好'  : '早上好~' ,
#     '晚安'    : '做个好梦',
#     '我爱你'    :'我也爱你'
# }
# #回复部分
# reply = on_message(priority=100)
# @reply.handle()
# async def reply_handle(bot: Bot, event: Event):
#     id=str(event.get_user_id())
#     user_msg = str(event.get_message()).strip()
#     #对输入进行判断并处理
#     try:
#         reply_msg = reply_dic[user_msg]
#         await reply.finish(reply_msg)
#     except KeyError:
#         await reply.finish()

#
# import random
# from datetime import date
# from nonebot.plugin import on_command, export
# from nonebot.adapters.cqhttp import Bot, Event
# from nonebot.adapters.cqhttp.message import Message
#
# export = export()
# export.name = '今日人品'
# export.usage = '''/jrrp'''
#
# def luck_simple(num):
#     if num < 18:
#         return '大吉'
#     elif num < 53:
#         return '吉'
#     elif num < 58:
#         return '半吉'
#     elif num < 62:
#         return '小吉'
#     elif num < 65:
#         return '末小吉'
#     elif num < 71:
#         return '末吉'
#     else:
#         return '凶'
#
# """ON_COMMAND
# ON_COMMAND是MFC提供的宏，实现命令消息（如菜单、工具栏的选项消息）的消息响应函数的注册。
# 使用方法为ON_COMMAND（消息ID, 响应函数名）
# 注册了响应函数之后，一旦主窗口接收到该命令消息，程序就会调用我们提供的消息响应函数进行处理
#
# """
# jrrp = on_command('jrrp', priority=50)  # 接收关键字
# """
# 在上方代码中，我们注册了一个事件响应器 Matcher，它由几个部分组成：
# on_command 注册一个消息类型的命令处理器
# "天气" 指定 jrrp 参数 - 命令名
# rule 补充事件响应器的匹配规则
# priority 事件响应器优先级
# block 是否阻止事件传递
# """
#
#
# """handle()
# 简单的为事件响应器添加一个事件处理函数，这个函数将会在上一个处理函数正常返回执行完毕后立即执行。
# """
# @jrrp.handle()  # 监听 jrrp
# async def jrrp_handle(bot: Bot, event: Event):
#     rnd = random.Random()
#     rnd.seed((int(date.today().strftime("%y%m%d")) * 45) * (int(event.get_user_id()) * 55))
#     lucknum = rnd.randint(1, 100)  # 1 到 100的数
#
#     # 返回QQ号， 发送消息
   #  await jrrp.finish(message=Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"'))
#
#
