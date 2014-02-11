#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

class Help(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>ヘルプ画面</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
<pre>
<h4>SQLの仕様</h4>
MariaでもPostgreでもMyでもありません。
sqlite3というPythonの簡易データベースツールです。
COPY文など使用できないstatementが多数存在します。
一つ、大きな特徴として、「select * from table;select * from table;」
のような、select文においてmultiple statementな
SQLクエリを発行することができません。
詳しくは<a href="http://docs.python.jp/2.6/library/sqlite3.html">python-sqlite3の公式Doc</a>をご覧ください。
<h4>XSSの仕様</h4>
未実装。
phantomjsガー
外部との通信ガー
</pre>
</body>
</html>
""")
