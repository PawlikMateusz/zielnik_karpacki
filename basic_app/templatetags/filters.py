from django import template
register = template.Library()

@register.filter(name='zdjecia_rosliny')
def zdjecia_rosliny(zdjecia,roslina):
    print(zdjecia)
    return zdjecia.filter(zdjecia.nazwa_polska==roslina.nazwa_polska)
