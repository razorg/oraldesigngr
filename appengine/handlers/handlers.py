from BaseHandler import JinjaHandler


class Root(JinjaHandler):
    def get(self):
        self.render_response('index.html')
