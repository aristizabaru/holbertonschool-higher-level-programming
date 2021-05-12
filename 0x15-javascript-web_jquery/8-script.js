$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (jsonData, statusCode) {
  if (statusCode === 'success') {
    const films = jsonData.results;
    for (const i in films) {
      $('#list_movies').append('<li>' + films[i].title + '</li>');
    }
  }
});
