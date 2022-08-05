import os

import jinja2
from tornado import web
from tornado.web import StaticFileHandler
#from tornado_jinja2 import Jinja2Loader
from python_js.app.start_page import MainHandler
from python_js.py_js.drop_out import dropping_out
# Create a instance of Jinja2Loader
#jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template/path/'), autoescape=False)
#jinja2_loader = Jinja2Loader(jinja2_env)

# Give it to Tornado to replace the default Loader.
#settings = dict(template_loader=jinja2_loader)
drop_init = dropping_out('fff', ['1','2'],'/')
drop_init.clear()

def make_app():
    settings = {
        "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        "login_url": "/login",
        "debug": True
    }
    return web.Application([
        (r"/", MainHandler),
        (r"/(.*)", StaticFileHandler, {'path': os.path.dirname(os.path.abspath(__file__))}),
    ], **settings)
