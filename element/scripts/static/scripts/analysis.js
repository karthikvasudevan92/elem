function Line(line){
  this.line = line[0];
  this.id = line.find('span.line-id').data('lid');
}
Line.prototype.update = function(){

};


function CommonWord(word){
  this.word = word;
  this.text = word.data('text');
  this.id = word.data('id');
  this.detail = $('.common-word-details ul.tab-content>li#commonword'+this.id);
  this.url = window.location.pathname+"/commonwordsentences/"+this.id;
  this.initiate();
}

CommonWord.prototype.initiate = function(){
  var self = this;
  if( this.word[0].dataset.state == 'active' )
  {
    $(this.word[0]).tab('show');
    self.getSentences();
  }
  this.word.bind('show.bs.tab',function(){
    self.getSentences();
  });
};

CommonWord.prototype.getSentences = function(){
  var self = this;
  self.detail.find('.progress-bar').css('width','40%');
  $(self.word[0]).siblings().removeClass('active');
  $.ajax({
    url: self.url,
    context: self.detail,
    complete: function(jqXHR, code){
      // console.log(jqXHR);
      var sentences = jQuery.parseJSON(jqXHR.responseJSON.word.sentences);
      self.detail.find('.progress-bar').css('width','90%');
      output = '<ul class="no-style">';
      for(i=0;i<sentences.length;i++)
      {
        output += '<li>';
        output += '<p>'+sentences[i].fields.text+'</p>';
        output += '</li>';
      }
      output += '</ul>';
      $(self.word[0]).addClass('active');
      self.detail.find('.common-word-sentences').html(output);

    },
  });
};

function Script(id){
  this.id = id;
  this.lines = [];
  this.commonwords = [];
  this.getLines();
  this.makeBindings();
  this.getCommonWords();
}

Script.prototype.makeBindings = function(){
  var self = this;
  $('button[name="scanscript"]').bind('click',function(){
    self.scan();
  });
  $('button[name="scanscriptfile"]').bind('click',function(){
    scriptfile = $(this).siblings('a')[0].dataset.fid;
    self.scanfile(scriptfile);
  });
};

Script.prototype.getLines = function(){
  var self = this;
  var s_lines = $('ul#alines>li');
  s_lines.each(function( index ,line ){
    var new_line = new Line($(line));
    self.lines.push(new_line);
  });
};

Script.prototype.getCommonWords = function(){
  var self = this;
  var commonwords_list = $('.common-words-wrap>a');
  commonwords_list.each(function( index ,obj ){
    var commonword = new CommonWord($(obj));
    self.commonwords.push(commonword);
  });
};

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

Script.prototype.scanfile = function(fid){
  var pathname = window.location.pathname;
  console.log(pathname+'/scanfile/'+fid);
  $.ajax({
    url: pathname+"/scanfile/"+fid,
    context: document.body,
    complete: function(jqXHR, code){
      console.log(jqXHR.responseJSON);
    },
  });
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
