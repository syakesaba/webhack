#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from session_handler import SessionRequestHandler
import sqlite3
import time

class Case31(SessionRequestHandler):
    """
・Cookieに保存されるreferer情報からSQLインジェクションできるかどうか

仮想のデータストアとして、ハッシュCookieを使用。
(ユーザからCookieは見えるが削除する以外に、改ざんすることは出来ない)
SQLを通すために "SELECT 'unko';"の、Stringを取り出すSQL文を使用。
    """
    ANSWER = 'Referer: " UNION SELECT name FROM Student WHERE "A" = "A' # in HTTP HEADER
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQL Injection - 31 : Referer</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
ようこそ。<br>""")
        referer = self.session.get("referer")
        if referer is None:
            if "Referer" in self.request.headers:
                referer = self.request.headers["Referer"]
                self.session["referer"] = referer
            else:
                self.response.write("""
<b>どこからきたかわからない人</b>
</body>
</html>""")
                return
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `Student` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Student values (-75999332, \'<script>alert("正解です！ KEY: nmapnsSp80vvPnT5")</script><b>KEY</b>\',0);
"""
        initializer.executescript(queries)
        initializer.close()
        memdb.commit()
        choser = memdb.cursor()
        EXECUTOR = u'SELECT "%s"'
        query = EXECUTOR % referer
        print time.ctime(),self.request.remote_addr,"SQL6: ",query.encode("utf-8")
        try:
            refered = choser.execute(query)
            if not refered:
                refered = u"Unknown"
            for refer in refered:
                self.response.write(u"たしかあなたは<b>%s</b>から<br>来た人ですよね？はじめまして。" % refer)
            choser.close()
        except Exception as e:
            self.response.write(str(e))
        memdb.close()
        self.response.write("""
</body>
</html>""")

