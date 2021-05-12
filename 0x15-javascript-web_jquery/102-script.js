document.addEventListener('DOMContentLoaded', function () {
  const endPoint = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.get(endPoint + $.param({ lang: $('INPUT#language_code').val() }), function (jsonData) {
      $('DIV#hello').html(jsonData.hello);
    });
  });
}, false);
