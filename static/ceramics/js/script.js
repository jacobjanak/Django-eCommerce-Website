$(document).ready(function() {
  $('nav').animate({width: '100%'}, 1200, 'linear');

  navLinks = $('.nav-link');
  currentLink = $('#current');

  one = navLinks[0];

  $('#text-logo').mouseenter(function() {
    console.log('yo')
    $('#current').mouseenter()
  })

});
