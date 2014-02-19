#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from case1 import Case1
from case2 import Case2
from case3 import Case3
from case4 import Case4
from case5 import Case5
from case6 import Case6

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQLインジェクション</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
<ul>
<li><a href="./1">問題1</a> - インフルエンザウイルスレベル</li>
<li><a href="./2">問題2</a> - ミトコンドリアレベル</li>
<li><a href="./3">問題3</a> - ミドリムシレベル</li>
<li><a href="./4">問題4</a> - ミジンコレベル</li>
<li><a href="./5">問題5</a> - ボウフラレベル</li>
<li><a href="./6">問題6</a> - アメンボレベル</li>
</ul>
</body>
</html>
""")

ALL = [
("/sqli/",Index),
("/sqli/1",Case1),
("/sqli/2",Case2),
("/sqli/3",Case3),
("/sqli/4",Case4),
("/sqli/5",Case5),
("/sqli/6",Case6)
]
