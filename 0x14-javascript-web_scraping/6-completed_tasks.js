#!/usr/bin/node
// counting number of completed tasks
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const white = JSON.parse(body);
    const completed = {};
    white.forEach((todo) => {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else{
          completed[todo.userId] += 1;
        }
      }
    });
    console.log(completed);}
});
