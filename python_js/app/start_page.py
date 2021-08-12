"""
This module make init first page for tornado

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""
from bokeh.embed import components
from tornado import web
import jinja2
from python_js.py_js.drop_out import dropping_out
class MainHandler(web.RequestHandler):
    def post(self):
        title = "Показ работы разных плюшек."
        list_field = ['aaaa', 'fffff', 'ereref', 'ggggg', 'ttttt']
        dict_field = {'aaaa' : 0, 'fffff' : 1, 'ereref' : 2,
                      'ggggg' : 3, 'ttttt' : 4}
        drop_lis_one = dropping_out('first', list_field,'/')
        print(self.get_argument(drop_lis_one.name_this_wid, default=None, strip=False))

        return  self.render('index.html',
                            title = title,
                            drop_lis_one = drop_lis_one.cod_html()
                          )
    get = post


