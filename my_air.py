#!/usr/bin/env/python

from pushbullet import Pushbullet

import time

import requests

from apscheduler.schedulers.blocking import BlockingScheduler


def main():

    city = input()
    url = 'http://www.pm25.in/api/querys/pm2_5.json?city=%s&token=5j1znBVAsnSf5xQyNQyq' % city
    r = requests.get(url)

    data = r.json()

    for i in data:

        x = i.get('aqi')

        if x < 50:
            n = '空气质量不错，开窗通风吧！'

        if x > 150:
            n = '空气质量很糟糕， 快关窗户为自己续一秒！'

        else:
            n = '天气一般般，不好不坏。'

    answer = '%s的AQI为:' % city + str(data[-1]['aqi']) + '\n\n' + n

    p = Pushbullet("o.QiBXsVzuj9gXEEQWIdhiftZ6X9iG5QFc")

    t = time.strftime("%Y-%m-%d %H:%M", time.localtime())

    push = p.push_note('现在是' + t + '\n', answer)


sched = BlockingScheduler()

sched.add_job(main, 'interval', hours=12)

sched.start()








