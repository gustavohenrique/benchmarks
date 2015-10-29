# coding: utf-8
import falcon
import bjoern

from middleware import RequireJSON, JSONTranslator
from database import find_all, insert


class HelloResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('Hello World')


class DatabaseResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        rows = find_all()
        resp.body = rows

    def on_post(self, req, resp):
        data = req.context.get('data')
        insert(data)
        resp.status = falcon.HTTP_201


app = falcon.API(middleware=[RequireJSON(), JSONTranslator()])
app.add_route('/', DatabaseResource())
app.add_route('/hello', HelloResource())

if __name__ == '__main__':
    bjoern.listen(app, '0.0.0.0', 8080)
    bjoern.run()
