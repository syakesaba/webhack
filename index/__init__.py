#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import webapp2
from helppage import Help

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>メニュー画面</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
ようこそ。</br>
<ul>
<li><a href="./sqli/">SQLインジェクション</a></li>
<li><a href="./xss/">クロスサイトスクリプティング</a></li>
</ul>
<br>
<hr>
<a href="/help">ヘルプ</a>
<a href="file:///C:/">TEST</a>
</body>
</html>
""")

ALL = [
("/",Index),
("/help",Help)
]
