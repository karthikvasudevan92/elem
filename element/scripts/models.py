from django.db import models
from bs4 import BeautifulSoup
from pprint import pprint
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
# Create your models here.
class Otype(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Sentence(models.Model):
    text = models.TextField(max_length=5000)
    sentnum = models.IntegerField(blank=True)
    def linenum(self):
        lines = [line.linenum for line in self.line_set.all()]
        return lines
    def tokens(self):
        tokens = []
        words = word_tokenize(self.text)
        for wid,word in enumerate(nltk.pos_tag(words)):
            token = {}
            token['text'] = word[0]
            token['tag'] = word[1]
            token['id'] = wid
            tokens.append(token)
        return tokens
    def __str__(self):
        return self.text
class Line(models.Model):
    text = models.TextField(max_length=10000)
    linenum = models.IntegerField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    sentences = models.ManyToManyField(Sentence, through='Line_Sentence', blank=True)
    def get_script(self):
        scriptnames = [script.name for script in self.script_set.all()]
        return scriptnames
    def get_tags(self):
        return self.tags.all()
    def __str__(self):
        return self.text
    def scan_line(self):
        # print(self.text)
        sents = sent_tokenize(self.text)
        for ids,sent in enumerate(sents):
            new_sentence = Sentence(text=sent,sentnum=ids)
            new_sentence.save()
            line_sentence = Line_Sentence(line=self,sentence=new_sentence)
            line_sentence.save()
            self.save()
    def save(self):
        super(Line, self).save()
        if not self.sentences.count()>0:
            self.scan_line()
            self.save()
    def sentence_count(self):
        return self.sentences.count()
    class Meta:
        ordering = ('linenum',)
class Script(models.Model):
    name = models.CharField(max_length=200)
    scriptfile = models.FileField(upload_to='scripts/')
    scanned = models.BooleanField(default=False)
    lines = models.ManyToManyField(Line, through='Script_Line', blank=True)
    def line(self):
        f = open( ''+self.scriptfile.path)
        for line in f:
            print(line)
        return f.readline()
    def analysis(self):
        analysis = {'sentence_count':0}
        f = open( ''+self.scriptfile.path)
        self.scriptfile.seek(0)
        file_html = self.scriptfile.read()
        soup = BeautifulSoup(file_html,'html.parser')
        lines = []
        for idl,string in enumerate(soup.stripped_strings):
            line = {'t_count':0}
            line['text'] = string
            line['sentences'] = []
            line['id'] = idl
            sentences = sent_tokenize(string)
            line['s_count'] = len(sentences)
            line['t_count'] = 0
            for ids,sent in enumerate(sentences):
                sentence = {}
                sentence['id'] = ids
                sentence['sent'] = sent
                sentence['words'] = word_tokenize(sent)
                sentence['t_count'] = len(sentence['words'])
                line['t_count'] += sentence['t_count']
                sentence['c_count'] = 0
                sentence['tokens'] = []
                for idw,wrd in enumerate(nltk.pos_tag(sentence['words'])):
                    token = {}
                    token['text'] = wrd[0]
                    token['tag'] = wrd[1]
                    sentence['c_count'] += len(token['text'])
                    sentence['tokens'].append(token)
                sentence['c_avg'] = sentence['c_count']/sentence['t_count']
                line['sentences'].append(sentence)
                analysis['sentence_count'] += 1
            line['t_avg'] = line['t_count']/line['s_count']
            lines.append(line)
        analysis['lines'] = lines
        return analysis
    def line_count(self):
        return self.lines.count()
    def sentence_count(self):
        sentence_count = 0
        for line in self.lines.all():
            sentence_count += line.sentence_count()
        return sentence_count
    def scan_script(self):
        if not self.scanned:
            analysis = self.analysis()
            for line in analysis['lines']:
                new_line = Line(text=line['text'],linenum=line['id'])
                if not self.lines.filter(linenum=line['id']):
                    new_line.save()
                    script_line = Script_Line(script=self,line=new_line)
                    script_line.save()
            if self.lines.count() == len(analysis['lines']):
                self.scanned = True
            self.save()
        else:
            analysis = False
        return analysis
    def __str__(self):
        return self.name
class Script_Line(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    def __str__(self):
        return self.script.name
class Line_Sentence(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    def __str__(self):
        return self.line.linenum
