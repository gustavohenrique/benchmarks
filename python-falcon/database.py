# coding: utf-8
from __future__ import with_statement
from contextlib import contextmanager

import psycopg2
import psycopg2.pool
import json

a = psycopg2.pool.SimpleConnectionPool(1, 10, database='benchmark', user='postgres', password='root', host='docker.postgres.local')


@contextmanager
def getcursor():
    connection = a.getconn()
    try:
        yield connection.cursor()
        connection.commit()
    except:
        connection.rollback()
    finally:
        a.putconn(connection)


def find_all():
    result = []
    with getcursor() as cur:
        cur.execute('SELECT * FROM urls')
        rows = cur.fetchall()
        for item in rows:
            data = {
                'id': item[0],
                'long_url': item[1],
                'short_url': item[2],
                'clicks': item[3],
                'created_at': u'%s' % item[4]
            }
            result.append(data)
    return json.dumps(result)


def insert(data):
    with getcursor() as cur:
        cur.execute('INSERT INTO urls(long_url, short_url) VALUES (%(long_url)s, %(short_url)s)', data)
