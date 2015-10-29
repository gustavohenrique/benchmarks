var pgp = require('pg-promise')();
var cn = {
    host: 'docker.postgres.local',
    port: 5432,
    database: 'benchmark',
    user: 'postgres',
    password: 'root'
};

(function () {

    function Database() {
        var self = this;
        var conn = pgp(cn);

        var findAll = function () {
            return conn.query('select * from urls', true);
        };

        var insert = function (data) {
            return conn.none('insert into urls(long_url, short_url) values(${long_url}, ${short_url})', data);
        };

        self.conn = conn;
        self.findAll = findAll;
        self.insert = insert;
        return self;
    };

    module.exports = Database;

})();
