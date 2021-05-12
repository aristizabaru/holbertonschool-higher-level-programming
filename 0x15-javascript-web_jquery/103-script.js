const main = () => {
  const translate = () => {
    const endPoint = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(endPoint + $.param({ lang: $('INPUT#language_code').val() }), function (jsonData) {
      $('DIV#hello').html(jsonData.hello);
    });
  };

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        translate();
      }
    });
  });
};

document.addEventListener('DOMContentLoaded', function () {
  main();
}, false);
