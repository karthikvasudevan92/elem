from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import ListView
urlpatterns = [
    path('script/<int:pk>', views.ScriptDetail.as_view(), name='script-detail'),
    path('', views.ScriptList.as_view(),name='scriptlist'),
    path('languages', views.LanguageList.as_view(),name='languages'),
    path('language/<int:pk>', views.LanguageDetail.as_view(), name='language-detail'),
    path('script/<int:pk>/scan', views.ScanScript, name="scanscript"),
    path('script/<int:pk>/scanfile/<int:fid>', views.ScanFile, name="scanfile"),
    path('script/<int:sk>/line/<int:lk>/tagid/<int:tk>/action/<slug:action>', views.TagAction, name="TagAction"),
    path('script/<int:sk>/commonwordsentences/<int:wk>', views.CommonWordSentences, name="CommonWordSentences")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
