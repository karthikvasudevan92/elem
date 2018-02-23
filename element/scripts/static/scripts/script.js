$(document).ready(function(){
  var urlParts = window.location.pathname.split('/');
  var scriptId = urlParts[urlParts.length-1];
  var script = new Script(scriptId);
  $('button[name="scanscript"]').bind('click',function(){
    script.scan();
  });
  $('ul.tag-actions>li a').bind('click',function(e){
    var line = $(this).closest('li.line');
    var lineid = line.find('.line-id')[0].innerText;
    var tag = new Tag(this);
    tag.do();
  });

});
