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
助けが欲しいか？</br>
</body>
</html>
""")
