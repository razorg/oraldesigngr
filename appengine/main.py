# -*- coding: utf-8 -*-
import os
import set_sys_path

import webapp2
from config import config
from urls import routes
import error_handlers

# Is this the development server?
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Instantiate the application.
app = webapp2.WSGIApplication(routes=routes, config=config, debug=debug)
error_handlers.register(app)

def main():
    app.run()

if __name__ == '__main__':
    main()
