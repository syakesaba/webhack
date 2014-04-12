#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import sqlite3
import time
import crypt

class Case6(webapp2.RequestHandler):
    """
・関数の引数の数を推測し正しい数の引数を代入させることができるかどうか。
・プリペアドステートメントを含むバインディングSQLを完成できるかどうか。
    """
    ANSWER="id=root&passwd=a','a') or 1 or ? or ?--"
    def get(self):
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `passwd` (`id` CHAR[255] PRIMARY KEY, `salt` CHAR[255], `hash` CHAR[1024]);
insert into `passwd` values ('root','$6$0P2MRTHD$','UrVvRg5yEfY6Oz.Lc96ONoK.myTh4fOdLG1AWzkxQFbxlnd1Dy96kwOsD6S08Dmvxv3fhcO9VCD4CIan66cgi.');
insert into `passwd` values ('user1','$6$mT3ncmux$','Pu.miMo6pXUj4Cb2EpXsRObOE6xcEM1JUV472PVmL2cg.Ise418UeOY79slaLmOU5zkdUmatFtRjwQiNJmome/');
insert into `passwd` values ('user2','$6$FiA9SD2G$','ZkxLUT4gYo1imR5LWZ3t9wgFePSIlAhomaK7WwR/ZVKNoY1A7njlPb428gDLk03rz6p7deXBkAmtlJ2gexJP..');
insert into `passwd` values ('user3','$6$0WPncyBa$','AGosRNldySnpEHR2XGBQJZOXkPdaLs1D1RNm2GTNfJ9IzQMerPj155qlnc3mnZdLx9PcdG.LhDE4RuH6FZy/V/');
insert into `passwd` values ('mario','$6$zvKdeoPj$','JNoTKVKGP4O8uJgYr5ELLGIkbYRuwJHBwebToAlvI8/pwXvUjMTodiAX5lRH1UPxf2u9jR0.2bfHUyAx.kRog1');
insert into `passwd` values ('kirby','$6$wQ.Hfs/L$','wutODOnhvKW6z.wpnIULpExWHQ1gQbwW4o6JRwLp5Q9qaVuRS4Zcjcl2D/oTj0N44g6wtxDjqdUvJG0PlZS0n0');
insert into `passwd` values ('xss','$6$Mr/o0WIv$','cGfAeRdAOJu/IE1WuE6vY3x8BU/Pkk6oVWLwvNbJPze1fCb/FqjGqa.GSBr.ENZCJ/LAdB1RAzE9cLINv6BJO/');
insert into `passwd` values ('sqli','$6$zZPLDpgs$','8sdS8EmEnUAWRE.x8PIZwp9HuAQlktF7W05X1m6gv8e9yJee/jOdoj4TegV/QGBwd8mnIEpRz9JiKfOzAoa5i.');
insert into `passwd` values ('px5','$6$KWhrjXqj$','Lbf1zo52kWNpLUeUltaNOen4lHA/YR0tHXd713FbHdOj0PaLjDgck9JGEDPIxtN3ZMhMj7qR6h5f.wIzTokAj/');
insert into `passwd` values ('john','$6$xbSJEbfW$','g7Sy4ePdDsEGUVMnjS2xkaKY4pUt1XuO/wdtRAJSU8rWEr8XiVQFIonJHcBrZxfTZ/Jr0hBxB49mwCYIi/fdP/');
insert into `passwd` values ('toor','$6$6c4f0WUe$','h5MDovjrpNJCUkIKwi6tUzxdiufgbNlTozvXs5tDzgyz0d32C2tEsJFG8WI7FEnwm2NOso1l2hTwlcGTLtLjt0');
"""
        initializer.executescript(queries)
        initializer.close()
        #crypt.crypt("word","salt") -> shadow (salt+hash)
        memdb.create_function("crypt", 2, crypt.crypt)
        memdb.commit()
        choser = memdb.cursor()
        choser.execute("select id from passwd;")
        ids = [_id[0] for _id in choser.fetchall()]
        EXECUTOR1 = "SELECT salt,hash FROM passwd WHERE id = ?"
        EXECUTOR2 = "SELECT 'Success! <script>alert(/  OK! KEY is ettercapTqMArpREMOTE   /)</script>' FROM passwd WHERE crypt('%s',?) = ?;"
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQL Injection - 6 : SQLと関数、プリペアドステートメント</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        get_id = self.request.get('id')
        get_passwd = self.request.get('passwd')
        if not get_id or not get_passwd:
            self.response.write("""
<b>IDとパスワードを入力してください</b><br>
<form target="_self" method="GET">
ID:<br>
<select name="id">
"""+"""
""".join(['<option value="%s">%s</option>' % (_id.encode("utf-8"),_id.encode("utf-8")) for _id in ids])
+
"""
</select><br>
パスワード: <input name="passwd" type="password" value=""><br>
<input type="submit" value="送信">
</form><br>
""")
        else:
            try:
                choser.execute(EXECUTOR1, (get_id,))
                db_ret = choser.fetchall()
                if len(db_ret) != 1 or len(db_ret[0]) != 2:
                    self.response.write("""
Invalid ID '<b>%s</b>'. Try Again.
    """ % get_id)
                else:
                    db_salt,db_hash = db_ret[0]
                    print time.ctime(),self.request.remote_addr,"SQL6: ",(EXECUTOR2 % get_passwd).encode("utf-8")
                    choser.execute(EXECUTOR2 % get_passwd ,(db_salt, db_salt+db_hash, ))
                    db_ret = choser.fetchall()
                    if len(db_ret) > 0:
                        if get_id == "root":
                            self.response.write(db_ret[0][0])
                        else:
                            self.response.write("""
パスワードクラックおめでとう。<br>
だが君はrootじゃないからキーは渡せないなあ＾＾""")
                    else:
                        self.response.write("""
Invalid Password '<b>%s</b>' for user '<b>%s</b>'. Try Again.<br>""" % (get_passwd,get_id))
            except Exception as e:
                self.response.write("<br>Application Error. <b>%s</b><br>" % str(e))
        choser.close()
        memdb.close()
        self.response.write("""
</body>
</html>""")

