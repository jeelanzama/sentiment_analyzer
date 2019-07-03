var express = require('express');
var path = require("path");
var bodyParser = require("body-parser");
var Sentiment = require("sentiment");
var analyzer = new Sentiment();
var app = express();
app.use(express.static(path.join(__dirname,'public')));
app.set('view engine','ejs');

function check_score(number){
    if(number >= 0){
        return 'positive'
    }else{
        return 'negative'
    }
}

app.use(bodyParser.urlencoded({ extended: true }));
app.get('/',function(req,res){
   res.render('home');
});
app.get('/login',function(req,res){
   res.render('login');
});
app.post('/dashboard',function(req,res){
    res.render('dashboard');
});
app.post('/prediction_success',function (req, res) {
    console.log(req.body.review);
    var result = analyzer.analyze(req.body.review);
    console.log(check_score(result.score));
    res.render('prediction_success');
});

app.listen(3000,function(){
    console.log("server running on port 3000")
});

