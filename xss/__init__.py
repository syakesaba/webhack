#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>Cross-Site-Scripting</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
<ul>
<li><a href="./1">1</a></li>
</ul>
</body>
</html>
""")

ALL = [
("/xss/",Index),
]
