# -*- coding:utf-8 -*-
from ics import Calendar
import requests
import arrow

from datetime import date
from datetime import timedelta

file = "abfuhrtermine.ics"
c = Calendar(open(file,"r").read())

today = date.today()

l = list(c.events)
l.sort(key=lambda x: x.begin)

gen = (x for x in l if (x.begin >= arrow.get(today).floor("day") and x.begin < arrow.get(today + timedelta(days = 6))))

for x in gen:
    print (x.name)
    print (x.begin)
