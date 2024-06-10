var express = require('express');
var app = express();
const PORT = 8080;
const HOST = '0.0.0.0';
var average = require('./average')
const url = require('url');

app.listen(
    PORT, HOST,
    () => console.log('its alive on http://${HOST}:${PORT}')
)

app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Content-Type', 'application/json');
    next();
});
// app.use(cors());
// app.options('*', cors());

app.use(express.json())

//http://localhost:8080/?mark_1=1&mark_2=2&mark_3=3&mark_4=4&mark_5=100
app.get('/', (req, res) => {
    //extract the parameters
    let params = url.parse(req.url, true).query
    var mark_1 = params.mark_1
    var mark_2 = params.mark_2
    var mark_3 = params.mark_3
    var mark_4 = params.mark_4
    var mark_5 = params.mark_5

    if (mark_1 === undefined || mark_1 === '') {
        res.status(400).send({
            error: true,
            errormessage: "Mark 1 was not provided",
            output: null
        })
    }
    if (mark_2 === undefined || mark_2 === '') {
        res.status(400).send({
            error: true,
            errormessage: "Mark 2 was not provided",
            output: null
        })
    }
    if (mark_3 === undefined || mark_3 === '') {
        console.log("triggered")
        res.status(400).send({
            error: true,
            errormessage: "Mark 3 was not provided",
            output: null
        })
    }
    if (mark_4 === undefined || mark_4 === '') {
        console.log("triggered")
        res.status(400).send({
            error: true,
            errormessage: "Mark 4 was not provided",
            output: null
        })
    }
    if (mark_5 === undefined || mark_5 === '') {
        res.status(400).send({
            error: true,
            errormessage: "Mark 5 was not provided",
            output: null
        })
    }
    if (!validMarkInt(mark_1, mark_2, mark_3, mark_4, mark_5)) {
        res.status(400).send({
            error: true,
            errormessage: "Invalid mark provided (must be int)",
            output: null
        })
    } 
    //check it is a int and between 0-100
    if (!validMarkRange(mark_1, mark_2, mark_3, mark_4, mark_5)) {
        res.status(400).send({
            error: true,
            errormessage: "All marks must be valid integars between 0-100",
            output: null
        })
    } else {
        //average mark
        raverage = average(parseInt(mark_1), parseInt(mark_2), parseInt(mark_3), parseInt(mark_4), parseInt(mark_5))
        res.status(200).send({
            error: false,
            errormessage: null,
            output: raverage
        })
    }
})

//check it is a number 
function validMarkInt(...marks) {
    for (var i = 0; i < marks.length; i++) {
        if (isNaN(marks[i])) {
            return false
        }
    }
    return true;
}
//check it is between 0-100
function validMarkRange(...marks) {
    for (var i = 0; i < marks.length; i++) {
        if (marks[i] < 0 || marks[i] > 100) {
            return false
        }
    }
    return true;
}