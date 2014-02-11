#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from case1 import Case1
from case2 import Case2
from case3 import Case3

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
</ul>
</body>
</html>
""")

ALL = [
("/sqli/",Index),
("/sqli/1",Case1),
("/sqli/2",Case2),
("/sqli/3",Case3)
]
