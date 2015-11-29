$(function(){
  $('.category').click(function(){
    $('.article-pane').hide();
    $('.cat-list-pane').removeClass('col-md-3').addClass('col-md-9').show();
  });
})();
