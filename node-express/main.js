var express = require('express');
var Database = require('./database');
var Services = require('./services');

var db = new Database();
var service = new Services(db);
var app = express();

app.get('/hello', function (req, res) {
    res.send('Hello World!');
});

app.get('/', service.findAll);
app.post('/', service.insert);

app.listen(8080, function () {
  console.log('App listening');
});
