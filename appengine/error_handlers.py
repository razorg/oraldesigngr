import logging, sys, os
current_path = os.path.abspath(os.path.dirname(__file__))

# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
sys.path[0:0] = [
    os.path.join(current_path, 'lib'),
]
logging.debug(sys.path)
from webapp2_extras import jinja2
import logging

def handle_error(error_code):
    def error_handler(request, response, exception):
        logging.exception(exception)
        rv = jinja2.get_jinja2().render_template('%s.html' % error_code)
        response.write(rv)
        response.set_status(error_code)
    return error_handler

def register(app):
	app.error_handlers[404] = handle_error(404)
