#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const completedTasks = {};

request(url, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(data);

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
