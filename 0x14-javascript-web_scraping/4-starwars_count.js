#!/usr/bin/node
// Gets the number of appearances of a character in the star wars franchise
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const wedgeMovies = data.results.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(wedgeMovies.length);
  }
});
