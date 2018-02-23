function Script(id){
  this.id=id;
}

Script.prototype.scan = function(){
  var pathname = window.location.pathname;
  console.log(pathname+'/scan');
  $.ajax({
    url: pathname+"/scan",
    context: document.body,
    complete: function(jqXHR, code){
      console.log(jqXHR.responseJSON);
    },
  });
};
function Line(id){
  this.id = id;
}
Line.prototype.update = function(){

};
function Tag(thistag){
  this.action = $(thistag).data('action');
  this.lid = $(thistag).closest('.line').find('span.line-id').data('lid');
  this.tid = $(thistag).closest('.tag').find('span.tag-name').data('tid');
  this.url = window.location.pathname+"/line/"+this.lid+"/tagid/"+this.tid+"/action/"+this.action;
  console.log(this.action);
  console.log(this.tid);
}

Tag.prototype.do = function(){
  console.log(this.url);
  $.ajax({
    url: this.url,
    dataType:'json',
    data: {},
    context: document.body,
    success:function(data){
      console.log(data);
      tags = JSON.parse(data.tags_updated);
      tags.forEach((tag) => {
        console.log(tag.fields.name);
      });
      console.log(tags);
    },
    complete: function(jqXHR, code){
    },
  });
};
