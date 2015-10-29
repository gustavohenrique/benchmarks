var restify = require('restify'),
    routes = require('restify-route'),
    Database = require('./database'),
    Services = require('./services');

function getServer () {
    var server = restify.createServer({ name: 'Benchmark' });

    var db = new Database(),
        service = new Services(db);

    server.use(restify.fullResponse())
          .use(restify.bodyParser())
          .use(restify.CORS())
          .use(restify.queryParser());

    routes
        .use(server)
        .set('/', 'get', service.findAll)
        .set('/', 'post', service.insert)
        .set('/hello', 'get', function (req, res) {
            res.send('Hello World!');
        });

    return server;
};

getServer().listen(8080, '0.0.0.0', function () {
    console.log('is running.');
});
