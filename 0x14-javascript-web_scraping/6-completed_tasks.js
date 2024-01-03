#!/usr/bin/node
// Computes the number of completed tasks
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 1;
        } else {
          completedTasks[todo.userId]++;
        }
      }
    }
    console.log(completedTasks);
  }
});
