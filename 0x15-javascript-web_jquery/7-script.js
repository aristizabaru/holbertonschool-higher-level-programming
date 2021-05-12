$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (jsonData, statusCode) {
  if (statusCode === 'success') {
    $('#character').text(jsonData.name);
  }
});
