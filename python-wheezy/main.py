from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

import bjoern

from database import find_all, insert


class HelloHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        response.write('Hello World!')
        return response


class DatabaseHandler(BaseHandler):

    def get(self):
        rows = find_all()
        response = HTTPResponse()
        response.write(rows)
        return response

    def post(self):
        data = self.request.form
        insert(data)
        response = HTTPResponse()
        response.status_code = 201
        return response


all_urls = [
    url('', DatabaseHandler, name='database'),
    url('hello', HelloHandler, name='hello'),
]


main = WSGIApplication(
    middleware=[bootstrap_defaults(url_mapping=all_urls), path_routing_middleware_factory],
    options={}
)


if __name__ == '__main__':
    bjoern.listen(main, '0.0.0.0', 8080)
    bjoern.run()
