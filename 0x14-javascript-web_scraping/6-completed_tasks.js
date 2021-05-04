#!/usr/bin/node
'use strict';
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  } // Print the error if one occurred
  if (response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    const users = fetchUsers(jsonData);
    const taskDone = fetchTask(jsonData, users);
    console.log(returnObject(users, taskDone));
  }
});

function returnObject (users, taskDone) {
  const resultObject = {};
  for (let i = 0; i < users.length; ++i) {
    if (taskDone[i] > 0) {
      resultObject[users[i]] = taskDone[i];
    }
  }
  return resultObject;
}

function fetchTask (jsonData, users) {
  const taskDone = [];
  for (const user of users) {
    let countTask = 0;
    for (const task of jsonData) {
      if (task.userId === user) {
        if (task.completed === true) {
          countTask += 1;
          taskDone[user - 1] = countTask;
        }
      }
    }
  }
  return taskDone;
}

function fetchUsers (jsonData) {
  const users = [];
  for (const task of jsonData) {
    if (users.includes(task.userId) === false) {
      users.push(task.userId);
    }
  }
  return users;
}
