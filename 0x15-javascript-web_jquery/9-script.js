$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (jsonData, statusCode) {
  if (statusCode === 'success') {
    $('#hello').text(jsonData.hello);
  }
});
