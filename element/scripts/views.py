from django.http import HttpResponse
from django.http import JsonResponse
from pprint import pprint
from .models import Script, Tag
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core import serializers
def index(request):
    return HttpResponse("Hello, world. You're at the scripts index.")
class ScriptDetail(DetailView):
    model = Script
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        return context
def ScanScript(request,pk):
    script = Script.objects.get(pk=pk)
    analysis = script.scan_script()
    return JsonResponse(analysis, safe=False)
def ScanFile(request,pk,fid):
    script = Script.objects.get(pk=pk)
    analysis = script.scan_file(fid)
    return JsonResponse(analysis, safe=False)
def CommonWordSentences(request,sk,wk):
    script = Script.objects.get(pk=sk)
    word = script.common_word_sentences(wk)
    response = {'sk':sk,'wk':wk,'word':word}
    return JsonResponse(response)
def TagAction(request,sk,lk,tk,action):
    line = Script.objects.get(pk=sk).lines.get(linenum=lk)
    tags = [tag.name for tag in line.tags.all()]
    tag = Tag.objects.get(pk=tk)
    if action == 'add':
        line.tags.add(tag)
    elif action == 'remove':
        line.tags.remove(tag)
    tags_updated = serializers.serialize('json',line.tags.all())
    response = {
                'sk':sk, 'lk':lk,
                'tk':tk, 'action':action,
                'tags':tags, 'tags_updated':tags_updated
                }
    print(response)
    return JsonResponse(response)
class ScriptList(ListView):
    # template_name = "list.html"
    model = Script
