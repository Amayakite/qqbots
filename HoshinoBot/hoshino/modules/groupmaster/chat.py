import random

from nonebot import on_command

from hoshino import R, Service, priv, util

from datetime import datetime
import pytz

# basic function for debug, not included in Service('chat')
tz = pytz.timezone('Asia/Shanghai')


@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('?')


sv = Service('chat', visible=False)


@sv.on_fullmatch('沙雕机器人')
async def say_sorry(bot, ev):
    await bot.send(ev, '滚呐')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('laopo.jpg').cqcode)
    else:
        await bot.send(ev, 'mua~')


@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '爪巴！', at_sender=True)


@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '笨蛋~', at_sender=True)


@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')
    await util.silence(ev, 30)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    await util.silence(ev, 30)


# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)


@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.02:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

nyb_player = f'''{R.img('newyearburst.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()


@sv.on_keyword(('春黑', '新黑'))
async def new_year_burst(bot, ev):
    if random.random() < 0.02:
        await bot.send(ev, nyb_player)

# ---------------------------------------------分割线-----------


@sv.on_fullmatch(('我登顶了', '我挖完了', '我到顶了', '我出货了'), only_to_me=True)
async def chat_congrat(bot, ev):
    await bot.send(ev, '恭喜！', at_sender=True)


@sv.on_fullmatch(('我井了', '我天井了', '我沉了'), only_to_me=True)
async def chat_sympathy(bot, ev):
    if random.random() < 0.95:
        await bot.send(ev, '真可惜。不过不要灰心，说不定下一次抽卡就出奇迹了呢！', at_sender=True)
    else:
        await bot.send(ev, '真的吗？好可怜…噗哈哈哈…', at_sender=True)


@sv.on_fullmatch(('晚安', '晚安哦', '晚安啦', 'good night'), only_to_me=True)
async def goodnight(bot, ev):
    now_hour = datetime.now(tz).hour
    if now_hour <= 3 or now_hour >= 21:
        await bot.send(ev, '晚安~', at_sender=True)
    elif 19 <= now_hour < 21:
        await bot.send(ev, f'现在才{now_hour}点，这么早就睡了吗？', at_sender=True)
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没到晚上咧。嘿嘿', at_sender=True)


@sv.on_fullmatch(('晚上好', '晚上好啊', '晚上好呀', 'good evening'), only_to_me=True)
async def goodevening(bot, ev):
    now_hour = datetime.now(tz).hour
    if 18 <= now_hour < 24:
        await bot.send(ev, f'晚上好！今晚想做什么呢？', at_sender=True)
    elif 0 <= now_hour < 6:
        await bot.send(ev, f'{now_hour}点啦，还不睡吗？', at_sender=True)
    elif 6 <= now_hour <= 9:
        await bot.send(ev, f'晚上好…嗯？我刚起床呢', at_sender=True)
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没天黑呢。嘿嘿', at_sender=True)


@sv.on_fullmatch(('你真棒', '你好棒', '你真厉害', '你好厉害', '真棒', '真聪明', '你真聪明'), only_to_me=True)
async def iamgood(bot, ev):
    await bot.send(ev, f'诶嘿嘿~')


@sv.on_fullmatch(('早安', '早安哦', '早上好', '早上好啊', '早上好呀', '早', 'good morning'), only_to_me=True)
async def goodmorning(bot, ev):
    now_hour = datetime.now(tz).hour
    if 0 <= now_hour < 6:
        await bot.send(ev, f'好早，现在才{now_hour}点呢', at_sender=True)
    elif 6 <= now_hour < 10:
        await bot.send(ev, '早上好！今天打算做什么呢？', at_sender=True)
    elif 21 <= now_hour < 24:
        await bot.send(ev, '别闹，准备睡觉啦！', at_sender=True)
    else:
        await bot.send(ev, f'{now_hour}点了才起床吗…', at_sender=True)


@sv.on_fullmatch(('你是谁', '你是谁啊', '你是谁？', '你是谁啊？', '你是谁?', '你是谁啊?'), only_to_me=True)
async def selfintro(bot, ev):
    await bot.send(ev, '我是镜华呀~')


@sv.on_fullmatch(('再见', '拜拜'), only_to_me=True)
async def farewell(bot, ev):
    await bot.send(ev, "拜拜~", at_sender=True)

hentai_audio = ("你是变态可疑分子.silk", "我懂了，你是变态吧.silk")
roar_audio = ("瓜啊.silk", "呜啊.silk")


@sv.on_fullmatch(('变态', '我是变态', '我是绅士', '变态可疑分子', '可疑分子'))
async def chat_hentai(bot, ev):
    rec = random.choice(hentai_audio)
    await bot.send(ev, R.rec(rec).cqcode)


@sv.on_fullmatch(('娇喘',))
async def chat_roar(bot, ev):
    rec = random.choice(roar_audio)
    await bot.send(ev, R.rec(rec).cqcode)


@sv.on_fullmatch(('唱歌', '唱首歌', '来首歌', '来唱首歌'), only_to_me=True)
async def sing(bot, ev):
    await bot.send(ev, R.rec('song.silk').cqcode)
    #这儿用的是优妮曲目，以后换成小仓唯的


@sv.on_keyword(('大佬', 'dalao', '大神'))
async def chat_dalao(bot, ev):
    if random.random() < 0.15:
        await bot.send(ev, R.img('dalao.jpg').cqcode)


@sv.on_keyword(('吃镜华', '吃xcw', '吃小仓唯'))
async def eatme(bot, ev):
    await bot.send(ev, '这样不好，真的！', at_sender=True)
