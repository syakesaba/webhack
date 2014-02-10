#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import index
import sqli
import xss

applications = webapp2.WSGIApplication(
    index.ALL+sqli.ALL+xss.ALL
    , debug=True)

def main():
    from paste import httpserver
    httpserver.serve(applications, host='127.0.0.1', port='80')

if __name__ == '__main__':
    main()
