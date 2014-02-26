#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from webapp2_extras import sessions

class SessionRequestHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()
