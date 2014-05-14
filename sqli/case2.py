#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import time
import sqlite3

class Case2(webapp2.RequestHandler):
    """
・HTMLではなくHTTP通信に目を向けられているかどうか
    """
    ANSWER = "?id=1 or 1" # in POST
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQL Injection - 2 : 通信に目をつける</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script type="text/javascript">
function submitit() {
    var f = document.f;
    var t = f.id.value;
    if (t.length != 1 || isNaN(t) ) {
        alert("正しい値を入力してください。");
        return;
    }
    f.submit();
}
function rejectReturn(e){
    if (!e) var e = window.event;
    if(e.keyCode == 13)
        return false;
}
document.onkeydown = rejectReturn
</script>
</head>
<body>
""")
    db_id = self.request.get("id")
    if db_id is not None and not db_id in "0123456789":
        self.response.write(""""<script>
alert(/その試みはとても尊いものだ。\\nヒントは、LiveHTTPHeadersもしくはTemperDataだ。/.source)
</script>""")
    self.response.write("""
ID(0から9)を入力してください。
<form name="f" method='POST' target='_self'>
    <input type='text' name='id' onkeypress="rejectReturn(event)" maxLength='1' size=1>
    <input type='button' value="送信" onclick="submitit()">
</form>
</body>
</html>""")

    def post(self):
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `Manager` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Manager values (151, \'ミュウ\',2);
create table `Student` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Student values (0, \'鳩山\',0);
insert into Student values (1, \'田中\',0);
insert into Student values (2, \'麻生\',1);
insert into Student values (3, \'小浜\',1);
insert into Student values (4, \'福田\',0);
insert into Student values (5, \'安部\',0);
insert into Student values (6, \'佐藤\',1);
insert into Student values (7, \'海部\',0);
insert into Student values (8, \'山田\',0);
insert into Student values (9, \'小泉\',0);
insert into Student values (5454217, \'<script>alert("成功です！ KEY: CHOWNROOTROOT")</script><b>KEY</b>\',0);
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
<title>SQL Injection - 2 : 通信に目をつける</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        self.response.write('ようこそ。')
        print time.ctime(),self.request.remote_addr,"SQL2: ",query.encode("utf-8")
        try:
            if not db_id:
                raise Exception("""
<script type="text/javascript">
location.href=location.href;
</script>
""")
            for name in choser.execute(query):
                try:
                    self.response.write(u"""
<b>%s</b> さん。""" % name)
                except Exception as e:
                    pass
            choser.close()
        except Exception as e:
            self.response.write(str(e))
        memdb.close()
        self.response.write("""
</body>
</html>""")

