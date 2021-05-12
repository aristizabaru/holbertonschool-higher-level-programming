document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    const listItem = $('ul.my_list li');
    if (listItem.length > 0) {
      listItem[listItem.length - 1].remove();
    }
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
}, false);
