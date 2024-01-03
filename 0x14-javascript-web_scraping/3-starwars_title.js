#!/usr/bin/node
// Gets starwars title
const request = require('request');
const id = process.argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
