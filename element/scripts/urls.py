from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import ListView
urlpatterns = [
    path('', views.index, name='index'),
    path('script/<int:pk>', views.ScriptDetail.as_view(), name='script-detail'),
    path('scripts/', views.ScriptList.as_view(),name='script-list'),
    path('script/<int:pk>/scan', views.ScanScript, name="scanscript"),
    path('script/<int:pk>/scanfile/<int:fid>', views.ScanFile, name="scanfile"),
    path('script/<int:sk>/line/<int:lk>/tagid/<int:tk>/action/<slug:action>', views.TagAction, name="TagAction"),
    path('script/<int:sk>/commonwordsentences/<int:wk>', views.CommonWordSentences, name="CommonWordSentences")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
