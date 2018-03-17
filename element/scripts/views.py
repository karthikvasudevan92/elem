from django.http import HttpResponse
from django.http import JsonResponse
from pprint import pprint
from .models import Script, Tag, Language
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core import serializers
from django.core.paginator import Paginator


def index(request):
    return render(
        request,
        'index.html',
        context={'page':'home'},
    )
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
class ScriptDetail(DetailView):
    model = Script
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        script = context['script']
        lines = script.lines.all()
        paginator = Paginator(lines, 100)
        page = 1
        page_requested = self.request.GET.get('page')
        if page_requested:
            page = page_requested
        scriptlines = paginator.get_page(page)
        context['paginator'] = paginator
        context['lines_page'] = scriptlines
        context['num_pages'] = paginator.num_pages
        context['tag_list'] = Tag.objects.all()
        return context
class ScriptList(ListView):
    # template_name = "list.html"
    model = Script
class LanguageDetail(DetailView):
    model = Language
class LanguageList(ListView):
    model = Language
