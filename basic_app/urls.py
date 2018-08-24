from django.urls import path, re_path
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'basic_app'
urlpatterns = [
    re_path(r'^atlasDrzewa', views.AtlasDrzewa.as_view(),name='atlasDrzewa'),
    re_path(r'^atlasPaprotniki', views.AtlasPaprotniki.as_view(),name='atlasPaprotniki'),
    re_path(r'^atlasTrawy', views.AtlasTrawy.as_view(),name='atlasTrawy'),
    re_path(r'^atlasBiale', views.AtlasBiale.as_view(),name='atlasBiale'),
    re_path(r'^atlasZolte', views.AtlasZolte.as_view(),name='atlasZolte'),
    re_path(r'^atlasCzerwone', views.AtlasCzerwone.as_view(),name='atlasCzerwone'),
    re_path(r'^indeksPolski', views.IndeksPolski.as_view(),name='indeksPolski'),
    re_path(r'^indeksLacinski', views.IndeksLacinski.as_view(),name='indeksLacinski'),
    path('widokRosliny/<id>/', views.WidokRosliny.as_view(), name='widokRosliny'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
