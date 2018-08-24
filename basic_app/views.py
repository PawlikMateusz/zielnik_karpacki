from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView,TemplateView
from django.db.models.functions import Lower
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
         context = super(IndexView, self).get_context_data(**kwargs)
         last_rosliny = models.Roslina.objects.order_by('-id_rosliny')[:3]
         context['rosliny'] = last_rosliny
         return context

class AtlasPaprotniki(TemplateView):
    template_name='basic_app/atlas.html'
    def get_context_data(self, **kwargs):
         context = super(AtlasPaprotniki, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.filter(kategoria='pap').order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context
class AtlasDrzewa(TemplateView):
    template_name='basic_app/atlas.html'
    def get_context_data(self, **kwargs):
         context = super(AtlasDrzewa, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.filter(kategoria='drz').order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context
class AtlasTrawy(TemplateView):
    template_name='basic_app/atlas.html'
    def get_context_data(self, **kwargs):
         context = super(AtlasTrawy, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.filter(kategoria='tra').order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context
class AtlasBiale(TemplateView):
    template_name='basic_app/atlas.html'
    def get_context_data(self, **kwargs):
         context = super(AtlasBiale, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.filter(kategoria='bia').order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context
class AtlasZolte(TemplateView):
    template_name='basic_app/atlas.html'
    def get_context_data(self, **kwargs):
         context = super(AtlasZolte, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.filter(kategoria='zol').order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context
class AtlasCzerwone(TemplateView):
    template_name='basic_app/atlas.html'
    def get_context_data(self, **kwargs):
         context = super(AtlasCzerwone, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.filter(kategoria='cze').order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context

class IndeksPolski(TemplateView):
    template_name='basic_app/indeksPolski.html'
    def get_context_data(self, **kwargs):
         context = super(IndeksPolski, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.order_by(Lower('nazwa_polska'))
         context['rosliny'] = roslinki
         return context

class IndeksLacinski(TemplateView):
    template_name='basic_app/indeksLacinski.html'
    def get_context_data(self, **kwargs):
         context = super(IndeksLacinski, self).get_context_data(**kwargs)
         roslinki = models.Roslina.objects.order_by(Lower('nazwa_lacinska'))
         context['rosliny'] = roslinki
         return context
class WidokRosliny(TemplateView):
    template_name='basic_app/widokRosliny.html'
    def get_queryset(self):
        return models.Roslina.objects.filter(id_rosliny=self.kwargs['id'])
    def get_context_data(self, **kwargs):
        context = super(WidokRosliny, self).get_context_data(**kwargs)
        roslina_by_id = models.Roslina.objects.filter(id_rosliny=self.kwargs['id'])
        context['roslina'] = roslina_by_id
        return context
