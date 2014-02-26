#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import index
import sqli
import xss


config = {}
config["webapp2_extras.sessions"] = {
    "secret_key":"WhoHaveTheBestOS?",
    "cookie_name":"WEBAPP2SESSIONID",
    "session_max_age":360,
}


applications = webapp2.WSGIApplication(
    index.ALL+sqli.ALL+xss.ALL
    , debug=True,config=config)

def main():
    from paste import httpserver
    httpserver.serve(applications, host='0.0.0.0', port='80')

if __name__ == '__main__':
    main()
