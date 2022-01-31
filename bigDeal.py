import winsound

winsound.PlaySound('alert', winsound.SND_ASYNC)  # 闹得挺大

our_country = ['某县城']
for high_school in our_country:
    print('传疯了')

import datetime

past = datetime.date.today() - datetime.timedelta(days=100)  # 以前


class past_me:
    def __init__(self):
        self.me = '二刺猿'

    def __str__(self):
        return '我'


class now_me:
    def __init__(self):
        self.grade = '高二'
        self.states = ('很少看动漫', '玩二次元游戏')

    def __str__(self):
        return '我'


class classmate(now_me):
    def __init__(self):
        self.states = now_me().states
        self._class = now_me.__class__('隔壁')

    def __str__(self):
        return '初中同学'


action = '{}, {} 一起吃饭'.format(now_me, classmate)


class idiot(classmate):
    def __init__(self):
        self.idiot = '二刺猿'
        self.states = ('上课天天看动漫', '玩游戏', '买手办')
        self.score = '班上倒数第一'
        self.hobby = '充钱'

    def charge_money(self, game, amount):
        game = '明日方舟'
        amount = '几万'

    def __str__(self):
        return '他班上的二刺猿'


while action:
    [now_me, classmate].append(idiot)
    print(f'{now_me()}, {classmate()} 不喜欢{idiot()}')
    print(f'{idiot()}吹嘘氪金抽到了什么什么')
    print(f'{idiot()}贬低别的动漫')
    break

try:
    idiot.friend
except AttributeError:
    print('几乎没什么朋友')
    print('口碑也很差')
    print('人品还有问题')

last_month = datetime.date.today() - datetime.timedelta(days=30)

idiot().charge_money('原神', '30000')
idiot().states = '没有满足'

steal_money = input('偷钱')
if steal_money == '成功':
    raise FileNotFoundError('这不是真实的历史')
elif steal_money == '失败':
    print('被他父亲抓了个现行', end='打起来了')
    idiot().charge_money('原神', '50000')

background = {
    '我学校': '全日制寄宿式',
    '放假': ['每个星期六放半天', '每个月月底放2-3天']
}

occurred_time = '十月'.endswith('月底')


class HisSister:
    def __init__(self):
        self.age = 12

    @property
    def LoveBrother(self):
        return '喜欢他'

    def __str__(self):
        return '他妹'


if '父母' not in '家':
    do = f'{idiot()}**了{HisSister()}'


    def threaten():
        print('不准告诉父母')

while '这个月月初回校中午吃饭时':
    print(f'{idiot()}说：')
    print(f'{HisSister()}是{HisSister.LoveBrother}')
    print(do)
    break

time = '前天10点左右'

school = ['老师', '学生']
legs = 2
if '知道' and do:
    school.append('他父母')
    legs -= 1

with open('录像.mp4', 'wb') as mobile_phone:
    mobile_phone.write(b'idiot fight against his father')

for high_school in our_country:
    high_school += '知道了这件事'

for time in ['半天']:
    print('这件事不要乱传')

print('早日放弃二刺猿，不要变成像他那样的人')