#!/usr/bin/env python
# encoding: utf-8

import os
import mimetypes
import webapp2

class StaticFileHandler(webapp2.RequestHandler):
    """
Only-One-Static-File vesion of https://pypi.python.org/pypi/webapp2_static
original author: Robert Spychala
License: MIT
Platform: any

Keep this file in webapp2 application's root directory.
e.g. myapp/static_handler.py

Usage:
    app = webapp2.WSGIApplication([
        (r'/', example.IndexHandler),
        (r'/favicon.ico', static_handler.StaticFileHandler)
        )

    """
    def get(self):
        abs_path_dir = os.path.dirname(os.path.abspath(__file__))
        abs_path = abs_path_dir + self.request.path
        if os.path.isdir(abs_path) or abs_path.find(os.getcwd()) != 0:
            self.response.set_status(403)
            return
        try:
            f = open(abs_path, 'r')
            self.response.headers.add_header('Content-Type', mimetypes.guess_type(abs_path)[0])
            self.response.out.write(f.read())
            f.close()
        except:
            self.response.set_status(404)
