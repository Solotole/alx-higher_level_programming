$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
    $.each(data.results, function (i, datas) {
      $('UL#list_movies').append('<li>' + datas.title + '</li>');
    });
  });
});
