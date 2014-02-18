#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

class Hint(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
<!DOCTYPE html>
<html>
<head>
<title>ヒント</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body>
<pre>
便利なツールたち
<ul>
<li><a href="http://livehttpheaders.mozdev.org/">LiveHTTPheaders</a></li>
<li><a href="http://tamperdata.mozdev.org/">TemperData</a></li>
</ul>
</pre>
</body>
</html>
""")
