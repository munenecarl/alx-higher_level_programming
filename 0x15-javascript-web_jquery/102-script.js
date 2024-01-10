$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang }, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
