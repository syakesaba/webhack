#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import sqlite3

class Case5(webapp2.RequestHandler):
    """
・SQLを完成できるかどうか。
    """
    ANSWER="id=\'or 1=1--"
    def get(self):
        memdb = sqlite3.connect(':memory:')
        initializer = memdb.cursor()
        queries = """
create table `passwd` (`id` CHAR[255] PRIMARY KEY, `uid` INTEGER UNIQUE, `gid` INTEGER, `gecos` CHAR[4096], `homeDirectory` CHAR[1024], `loginShell` CHAR[1024]);
insert into `passwd` values ('root', 0, 0, 'root', '/root','/bin/bash');
insert into `passwd` values ('daemon', 1, 1, 'daemon', '/usr/sbin','/bin/sh');
insert into `passwd` values ('bin', 2, 2, 'bin', '/bin','/bin/sh');
insert into `passwd` values ('sys', 3, 3, 'sys', '/dev','/bin/sh');
insert into `passwd` values ('sync', 4, 65534, 'sync', '/bin','/bin/sync');
insert into `passwd` values ('games', 5, 60, 'games', '/usr/games','/bin/sh');
insert into `passwd` values ('man', 6, 12, 'man', '/var/cache/man','/bin/sh');
insert into `passwd` values ('lp', 7, 7, 'lp', '/var/spool/lpd','/bin/sh');
insert into `passwd` values ('mail', 8, 8, 'mail', '/var/mail','/bin/sh');
insert into `passwd` values ('news', 9, 9, 'news', '/var/spool/news','/bin/sh');
insert into `passwd` values ('uucp', 10, 10, 'uucp', '/var/spool/uucp','/bin/sh');
insert into `passwd` values ('proxy', 13, 13, 'proxy', '/bin','/bin/sh');
insert into `passwd` values ('www-data', 33, 33, 'www-data', '/var/www','/bin/sh');
insert into `passwd` values ('backup', 34, 34, 'backup', '/var/backups','/bin/sh');
insert into `passwd` values ('list', 38, 38, 'Mailing List Manager', '/var/list','/bin/sh');
insert into `passwd` values ('irc', 39, 39, 'ircd', '/var/run/ircd','/bin/sh');
insert into `passwd` values ('gnats', 41, 41, 'Gnats Bug-Reporting System (admin)', '/var/lib/gnats','/bin/sh');
insert into `passwd` values ('nobody', 65534, 65534, 'nobody', '/nonexistent','/bin/sh');
insert into `passwd` values ('libuuid', 100, 101, '', '/var/lib/libuuid','/bin/sh');
insert into `passwd` values ('Debian-exim', 101, 103, '', '/var/spool/exim4','/bin/false');
insert into `passwd` values ('statd', 102, 65534, '', '/var/lib/nfs','/bin/false');
insert into `passwd` values ('ntp', 103, 106, '', '/home/ntp','/bin/false');
insert into `passwd` values ('sshd', 104, 65534, '', '/var/run/sshd','/usr/sbin/nologin');
insert into `passwd` values ('messagebus', 105, 107, '', '/var/run/dbus','/bin/false');
insert into `passwd` values ('colord', 106, 112, 'colord colour management daemon,,,', '/var/lib/colord','/bin/false');
insert into `passwd` values ('saned', 107, 113, '<b>HINT: singlequote will be escaped</b>', '/home/saned','/bin/false');
insert into `passwd` values ('', 1949, 1919, '<script>alert(/Good! KEY: catauthloggrepuser /)</script>MON<b>KEY</b>.', 'D.','Luffy');
"""
        initializer.executescript(queries)
        initializer.close()
        memdb.commit()
        choser = memdb.cursor()
        choser.execute("select id from passwd;")
        ids = [i[0] for i in choser.fetchall()]
        EXECUTOR = "SELECT * FROM passwd WHERE id = '%s';"
        db_id = self.request.get('id')
        query = EXECUTOR % db_id.replace("'","\\'")
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>SQL Injection -5 : エスケープを逆手に取る</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>""")
        self.response.write('ようこそ。')
        print "SQL5: ",query.encode("utf-8")
        try:
            if not db_id:
                raise Exception("""
IDを入力してください。
<form target="_self" method="GET">
<select name="id">
"""+"""
""".join(['<option value="%s">%s</option>' % (_id.encode("utf-8"),_id.encode("utf-8")) for _id in ids])
+
"""
</select>
<input type="submit" value="送信">
</form>
""")
            for line in choser.execute(query):
                try:
                    self.response.write(u"""
ようこそ。<br>
あなたの情報を表示します。<br>
<table border="3">
<tr>
    <td bgcolor="#9999ff">id</td>
    <td bgcolor="#9999ff">uid</td>
    <td bgcolor="#9999ff">gid</td>
    <td bgcolor="#9999ff">gecos</td>
    <td bgcolor="#9999ff">homeDirectory</td>
    <td bgcolor="#9999ff">loginShell</td>
</tr>
<tr>
<td>%s</td>
</tr>
</table>
""" % "</td><td>".join([str(l) for l in line]) )
                except Exception as e:
                    self.response.write(str(e))
            choser.close()
        except Exception as e:
            self.response.write(str(e))
        memdb.close()
        self.response.write("""
</body>
</html>""")

