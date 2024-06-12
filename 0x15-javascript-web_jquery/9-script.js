$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, respStatus) {
    $('DIV#hello').text(data.hello);
  });
});
