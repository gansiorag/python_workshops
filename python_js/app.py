from app import make_app
# import tornado.ioloop
#
# # for example, should be app
# #from app_p import app
# if __name__ == "__main__":
#     application().listen(5000)
#     tornado.ioloop.IOLoop.cuurent().start()

import tornado.ioloop
import tornado.web


if __name__ == "__main__":
    app = make_app()
    #app.listen(5000)
    adress = '127.0.0.1'
    port = 5000
    print(f'Started tornado!!! Listen address = {adress}, port = {port}')
    app.listen(address=adress, port=port)
    tornado.ioloop.IOLoop.current().start()