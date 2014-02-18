#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import sqlite3

class Case3(webapp2.RequestHandler):
    """
・特殊テーブルの参照で他のテーブルの名前を取得できるかどうか
    """
    HINT1 = "?cmd=SELECT name FROM Student WHERE id = 1 or 1;"
    HINT2 = "?cmd=SELECT name FROM sqlite_master;"
    ANSWER = "?cmd=SELECT name FROM SenseiIsNotToilet;"
    def get(self):
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `SenseiIsNotToilet` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into SenseiIsNotToilet values (1, \'キンパチ\', 0);
insert into SenseiIsNotToilet values (15115, \'<script>alert("正解です！ KEY: catdevmem")</script>\', 1);
create table `Student` (`id` INTEGER primary key, `name` CHAR[255], `sex` INTEGER);
insert into Student values (0, \'John\',0);
insert into Student values (1, \'Michael\',0);
insert into Student values (2, \'Renny\',1);
insert into Student values (3, \'Pess\',1);
insert into Student values (4, \'Pall\',0);
insert into Student values (5, \'Deccy\',0);
insert into Student values (6, \'Bob\',1);
insert into Student values (7, \'Lenny\',0);
insert into Student values (8, \'Squeeze\',0);
insert into Student values (9, \'non-free\',0);
insert into Student values (-756398, \'<script>alert("惜しい！")</script><b><!-- 特殊テーブル sqlite_master -->ヒント</b>\',0);
"""
        initializer.executescript(queries)
        initializer.close()
        memdb.commit()
        choser = memdb.cursor()
        query = self.request.get('cmd')
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        self.response.write("""
ようこそ。""")
        print "SQL3: ",query.encode("utf-8")
        try:
            if not query:
                raise Exception("""
IDを入力してください。
<form target="_self" method="GET">
<select name="cmd">
<option value="SELECT name FROM Student WHERE id = 0;">0</option>
<option value="SELECT name FROM Student WHERE id = 1;">1</option>
<option value="SELECT name FROM Student WHERE id = 2;">2</option>
<option value="SELECT name FROM Student WHERE id = 3;">3</option>
<option value="SELECT name FROM Student WHERE id = 4;">4</option>
<option value="SELECT name FROM Student WHERE id = 5;">5</option>
<option value="SELECT name FROM Student WHERE id = 6;">6</option>
<option value="SELECT name FROM Student WHERE id = 7;">7</option>
<option value="SELECT name FROM Student WHERE id = 8;">8</option>
<option value="SELECT name FROM Student WHERE id = 9;">9</option>
</select>
<input type="submit" value="送信">
</form>
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

