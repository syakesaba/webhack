#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import sqlite3
import time

class Case4(webapp2.RequestHandler):
    """
・演算子やUNIONを使用しCGIから情報を得られるかどうか
    """
    ANSWER = "?id=1 or 0 UNION select id,name from Student where id != -89347398"
    def get(self):
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `Manager` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Manager values (151, \'ミュウ\',2);
create table `Student` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Student values (0, \'佐田\',0);
insert into Student values (1, \'田中\',0);
insert into Student values (2, \'鈴木\',1);
insert into Student values (3, \'佐藤\',1);
insert into Student values (4, \'後藤\',0);
insert into Student values (5, \'伊藤\',0);
insert into Student values (6, \'加賀\',1);
insert into Student values (7, \'堀田\',0);
insert into Student values (8, \'相葉\',0);
insert into Student values (9, \'二宮\',0);
insert into Student values (-89347398, \'<script>alert("惜しい！\\nヒント:クエリは\\nSELECT id,name FROM Student WHERE id = %s;\\nなお、idはprimary key。")</script><b>ヒント</b>\',1);
insert into Student values (-47418092, \'<script>alert("正解です！ KEY: ddifdevnullofdevhda")</script><b>KEY</b>\',0);
"""
        initializer.executescript(queries)
        initializer.close()
        memdb.commit()
        choser = memdb.cursor()
        EXECUTOR = "SELECT id,name FROM Student WHERE id = %s;"
        db_id = self.request.get('id')
        query = EXECUTOR % db_id
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQL Injection - 4 : SQLとCGIの予測</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        self.response.write('ようこそ。')
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

