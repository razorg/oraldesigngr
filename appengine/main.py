# -*- coding: utf-8 -*-
import os, sys

current_path = os.path.abspath(os.path.dirname(__file__))

# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
sys.path[0:0] = [
    os.path.join(current_path, 'lib'),
]

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
