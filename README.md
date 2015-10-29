# benchmark
> Simple codes for stress tests

## Configure

Run postgres as Docker container:

    docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=root -d postgres
    docker run -it --link postgres:postgres --rm postgres sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

SQL Schema:

```sql
CREATE TABLE urls (
   id SERIAL PRIMARY KEY NOT NULL,
   long_url VARCHAR(250) NOT NULL,
   short_url VARCHAR(20) NOT NULL,
   clicks INT DEFAULT 0,
   created_at DATE NOT NULL DEFAULT CURRENT_DATE
);

INSERT INTO urls (long_url, short_url) VALUES ('http://mywebapp.com/about', 'http://goo.gl/7dh3');
```

Map in `/etc/hosts` the PostgreSQL server ip:

    $ cat /etc/hosts
    172.17.0.2      docker.postgres.local

## Result

    siege -c 500 -t 30S -r 5000 http://url:port

|                              | node-restify | node-express | golang  | python-falcon | python-wheezy | php-pure |
| ---------------------------- | ------------ | ------------ | ------- | ------------- | ------------- | ---------|
| Transactions (hits):         | 15478        | 13710        | 18266   | 14199         | 10471         | 8850     |
| Availability (%):            | 100.00%      | 100.00%      | 100.00% | 100.00%       | 100.00%       | 100.00%  |
| Elapsed time (secs):         | 29.58        | 29.58        | 30.01   | 29.93         | 29.33         | 29.06    |
| Data transferred (MB):       | 2.13         | 1.88         | 1.29    | 1.73          | 1.28          | 1.2      |
| Response time (secs):        | 0.42         | 0.41         | 0.29    | 0.42          | 0.83          | 0.67     |
| Transaction rate (trans/sec):| 523.26       | 463.49       | 608.66  | 474.41        | 357.01        | 304.54   |
| Throughput (MB/sec):         | 0.07         | 0.06         | 0.04    | 0.06          | 0.04          | 0.04     |
| Concurrency:                 | 219.43       | 191.43       | 176.08  | 198.51        | 296.12        | 202.53   |
| Successful transactions:     | 15478        | 13710        | 18267   | 14199         | 10471         | 8850     |
| Longest transaction:         | 2.81         | 6.92         | 2.86    | 7.3           | 3.62          | 21.28    |
| Shortest transaction:        | 0.24         | 0.24         | 0.24    | 0.24          | 0.26          | 0.24     |

