# -*- coding:utf-8 -*-

import textwrap
import json

class Birthdays:
    def __init__(self):
        pass

    def update(self):
        with open('dates.json') as f:
            self.data = json.load(f)
        return self.data

    def selected_title(self):
        list_dates = []
        for i in range(len(self.data["DateEntry"])):
                line = self.data["DateEntry"][i]["Title"]
                line = textwrap.wrap(line, width=30)
                list_dates.append(line)
        return list_dates
    
    def birthdayList(self):
        liste = {}
        for i in range(len(self.data["DateEntry"])):
                liste[str(self.data["DateEntry"][i]["Day"])+"."+str(self.data["DateEntry"][i]["Month"])+"."] = self.data["DateEntry"][i]["Title"]
        return liste


