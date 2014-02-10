#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import sqlite3

class Case1(webapp2.RequestHandler):
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
insert into Student values (-756398, \'<script>alert("成功です！ KEY: CHMOD777!")</script><b>KEY</b>\',0);
"""
        initializer.executescript(queries)
        initializer.close()
        memdb.commit()
        choser = memdb.cursor()
        EXECUTOR = "SELECT name FROM Student WHERE id = %s;"
        db_id = self.request.get('id')
        query = EXECUTOR % db_id
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        self.response.write('ようこそ。')
        print query.encode("utf-8")
        try:
            if not db_id:
                raise Exception("""
ID(0から9)を入力してください。
<form name='f' method='GET' target='_self'>
    <input type='text' name='id' maxLength='100' size=100>
    <input type='submit'>
</form>
""")
            for name in choser.execute(query):
                try:
                    self.response.write(u"""
<b>%s</b> さん。""" % name)
                except Exception as e:
                    pass
        except Exception as e:
            self.response.write(str(e))
        memdb.close()
        self.response.write("""
</body>
</html>""")

