#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from session_handler import SessionRequestHandler
import sqlite3
import time

class Case6(SessionRequestHandler):
    """
・Cookieに保存されるreferer情報からSQLインジェクションできるかどうか

仮想のデータストアとして、ハッシュCookieを使用。
(ユーザからCookieは見えるが削除する以外に、改ざんすることは出来ない)
SQLを通すために "SELECT 'unko';"の、Stringを取り出すSQL文を使用。
    """
    ANSWER = ""
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQL Injection - 6 : Cookie</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        name = self.request.get('name')
        if name:
            self.session["name"] = name
        if "Referer" in self.request.headers:
            referer = self.request.headers["Referer"]
        if "name" in self.session:
            self.response.write("""
ようこそ。 %sからお越しの%s さん。
""" % self.session["name"])
        else:
            self.response.write("""
ようこそ　名無しさん。
お名前をどうぞ。
<form target="_self" method="GET">
<input type="text" name="name">
<input type="submit" value="送信">
</form>
""")

        self.session["foo"] = "var"
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `Student` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Student values (-75454332, \'<script>alert("正解です！ KEY: ddifdevnullofdevhda")</script><b>KEY</b>\',0);
"""
        initializer.executescript(queries)
        initializer.close()
        memdb.commit()
        choser = memdb.cursor()
        EXECUTOR = "SELECT \"%s\""
        db_id = self.request.get('id')
        query = EXECUTOR % db_id
        if "foo" in self.session:
            print self.session["foo"].encode("utf-8")
        self.session["foo"] = "var"
        print time.ctime(),self.request.remote_addr,"SQL4: ",query.encode("utf-8")
        try:
            if not db_id:
                raise Exception("""
IDを入力してください。
<form target="_self" method="GET">
<select name="id">
<option value="0">0</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
<option value="5">5</option>
<option value="6">6</option>
<option value="7">7</option>
<option value="8">8</option>
<option value="9">9</option>
</select>
<input type="submit" value="送信">
</form>
""")
            #try:
            Id,name = choser.execute(query).next()
            self.response.write(u"""
<b>%s</b> さん。</br>あなたのidは<b>%d</b>です。""" % (name, Id) )
            #except Exception as e:
            #    pass
            choser.close()
        except Exception as e:
            self.response.write(str(e))
        memdb.close()
        self.response.write("""
</body>
</html>""")

