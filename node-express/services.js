(function () {

    var self = this;

    function Services (db) {
        self.db = db;
        this.findAll = findAll;
        this.insert = insert;
    };

    function findAll (req, res) {
        self.db.findAll().then(function (data) {
            res.send({result: data});
        });
    }

    function insert (req, res) {
        self.db.insert(req.body).then(function () {
            res.send(201, '');
        });
    }

    module.exports = Services;

})();