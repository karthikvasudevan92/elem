from django.contrib import admin
from .models import Otype, Script, Line, Sentence, Tag, CommonWord, File
class FileInlineAdmin(admin.TabularInline):
    model = Script.scriptfiles.through
class ScriptAdmin(admin.ModelAdmin):
    def l_count(self,obj):
        return obj.name
    list_display = ('name','scriptfile','scanned')
    fieldsets = [
        (None, {'fields':['name','scriptfile']})
    ]
    inlines = (FileInlineAdmin,)
admin.site.register(Script, ScriptAdmin)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name','file')
admin.site.register(File, FileAdmin)
class LineAdmin(admin.ModelAdmin):
    list_display = ('text','get_script','linenum','get_tags')
admin.site.register(Line, LineAdmin)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'linenum', 'sentnum','get_tags')
admin.site.register(Sentence, SentenceAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Tag, TagAdmin)
class CommonWordAdmin(admin.ModelAdmin):
    list_display = ('text','wfreq')
admin.site.register(CommonWord, CommonWordAdmin)
class OtypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Otype, OtypeAdmin)
