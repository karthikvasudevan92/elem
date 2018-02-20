from django.contrib import admin
from .models import Otype, Script, Line, Sentence, Tag
class ScriptAdmin(admin.ModelAdmin):
    def l_count(self,obj):
        return obj.name
    list_display = ('name','scriptfile','scanned')
admin.site.register(Script, ScriptAdmin)
class LineAdmin(admin.ModelAdmin):
    list_display = ('text','get_script','linenum','get_tags')
admin.site.register(Line, LineAdmin)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'linenum', 'sentnum')
admin.site.register(Sentence, SentenceAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Tag, TagAdmin)
class OtypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Otype, OtypeAdmin)
