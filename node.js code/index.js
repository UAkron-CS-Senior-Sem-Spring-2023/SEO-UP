//using express for html files
const express = require('express');
const app = express();

//define an array of strings 
//add strings here when they are finished
const strings = ['test1', 'test2', 'test3', 'test4'];

// define a route that sends the selected strings to the html client
app.get('/strings', (req, res) => {
  res.send(strings);
});

//start the server (add local host here, using date as example)
app.listen(03132023, () => {
  console.log('Start the server on http://localhost:03132023');
});
