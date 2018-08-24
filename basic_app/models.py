from django.db import models

def generate_filename(self, filename):
    url = "galeria/rosliny/%d/%s" % (int(self.nazwa_polska.id_rosliny), filename)
    return url
# Create your models here.
class Roslina(models.Model):
    bezbarwny = 'bb'
    biały = 'bi'
    brązowy = 'br'
    czerwony = 'cz'
    fioletowy = 'fi'
    niebieski = 'nb'
    pomarańczowy = 'po'
    różowy = 'ro'
    zielony = 'gr'
    żółty = 'zo'
    kolory = (
        (bezbarwny, 'bezbarwny'),
        (biały, 'biały'),
        (brązowy, 'brązowy'),
        (czerwony, 'czerwony'),
        (fioletowy, 'fioletowy'),
        (niebieski, 'niebieski'),
        (pomarańczowy, 'pomarańczowy'),
        (różowy, 'różowy'),
        (zielony, 'zielony'),
        (żółty, 'żółty'),
    )


    styczen = '01'
    luty = '02'
    marzec = '03'
    kwiecien = '04'
    maj = '05'
    czerwiec = '06'
    lipiec = '07'
    sierpien = '08'
    wrzesien = '09'
    pazdziernik = '10'
    listopad = '11'
    grudzien = '12'
    kwitnienie = (
        ('styczen', 'styczeń'),
        ('luty', 'luty'),
        ('marzec', 'marzec'),
        ('kwiecien', 'kwiecień'),
        ('maj', 'maj'),
        ('czerwiec', 'czerwiec'),
        ('lipiec', 'lipiec'),
        ('sierpien', 'sierpień'),
        ('wrzesien', 'wrzesień'),
        ('pazdziernik', 'pażdziernik'),
        ('listopad', 'listopad'),
        ('grudzien', 'grudzie'),
    )

    TAK_NIE = (
        ('y', 'Tak'),
        ('n', 'Nie')
    )
    rodziny = (
        ('Agres', 'Agrestowate'),
        ('Amary', 'Amarylkowate'),
        ('Arali', 'Araliowate'),
        ('Astro', 'Astrowate (Złożone)'),
        ('Babko', 'Babkowate'),
        ('Bagni', 'Bagnicowate'),
        ('Balda', 'Baldaszkowate (Selerowate)'),
        ('Bazyn', 'Bażynowate'),
        ('Berbe', 'Berberysowate'),
        ('Bobow', 'Bobowate (Motylkowate)'),
        ('Bobrk', 'Bobrkowate'),
        ('Bodzi', 'Bodziszkowate'),
        ('Brzoz', 'Brzozowate'),
        ('Bukow', 'Bukowate'),
        ('Cisow', 'Cisowate'),
        ('Cypry', 'Cyprysowate'),
        ('Czyst', 'Czystkowate (Posłonkowate)'),
        ('Deren', 'Dereniowate'),
        ('Dynio', 'Dyniowate'),
        ('Dziew', 'Dziewięciornikowate'),
        ('Dziur', 'Dziurawcowate'),
        ('Dzwon', 'Dzwonkowate'),
        ('Fiolk', 'Fiołkowate'),
        ('Gazew', 'Gązewnikowate'),
        ('Goryc', 'Goryczkowate'),
        ('Gozdz', 'Goździkowate'),
        ('Grubo', 'Gruboszowate'),
        ('Grusz', 'Gruszyczkowate'),
        ('Grzyb', 'Grzybieniowate'),
        ('Jaskr', 'Jaskrowate'),
        ('Jasno', 'Jasnotowate (Wargowe)'),
        ('Jezog', 'Jeżogłowkowate'),
        ('Kania', 'Kaniankowate'),
        ('Kapus', 'Kapustowate(Krzyżowe)'),
        ('Kaszt', 'Kasztanowcowate'),
        ('Klono', 'Klonowate'),
        ('Kloko', 'Kłokoczkowate'),
        ('Kokor', 'Kokornakowate'),
        ('Komos', 'Komosowate'),
        ('Konop', 'Konopiowate'),
        ('Kosac', 'Kosaćcowate'),
        ('Kozlk', 'Kozłkowate'),
        ('Krwaw', 'Krwawnicowate'),
        ('Krzyz', 'Krzyżowe(Kapustowate)'),
        ('Krzyp', 'Krzyżownicowate'),
        ('Leszc', 'Leszczynowate'),
        ('Lilio', 'Liliowate'),
        ('Lipow', 'Lipowate'),
        ('Lnowa', 'Lnowate'),
        ('Laczn', 'Łączniowate'),
        ('Makow', 'Makowate'),
        ('Marza', 'Marzanowate'),
        ('Motyl', 'Motylkowate(Bobowate)'),
        ('Nasie', 'Nasiężrzałowate'),
        ('Nieci', 'Niecierpkowate'),
        ('Obraz', 'Obrazkowate'),
        ('Ogore', 'Ogórecznikowate'),
        ('Oliwk', 'Oliwkowate'),
        ('Orlic', 'Orlicowate'),
        ('Tamar', 'Tamaryszkowate'),
        ('Toino', 'Toinowate'),
        ('Trawy', 'Trawy (Wiechlinowate)'),
        ('Tredo', 'Trędownikowate'),
        ('Troje', 'Trojeściowate'),
        ('Trzmi', 'Trzmielinowate'),
        ('Turzy', 'Turzycowate'),
        ('Wargo', 'Wargowe (Jasnotowate)'),
        ('Wawrz', 'Wawrzynkowate'),
        ('Werbe', 'Werbenowate'),
        ('Wiazo', 'Wiązowate'),
        ('Widli', 'Widliczkowate'),
        ('Widla', 'Widłakowate'),
        ('Wiech', 'Wiechlinowate (Trawy)'),
        ('Wielo', 'Wielosiłowate'),
        ('Wierz', 'Wierzbowate'),
        ('Wiesi', 'Wiesiołkowate'),
        ('Wietl', 'Wietlicowate'),
        ('Wilcz', 'Wilczomleczowate'),
        ('Winor', 'Winoroślowate'),
        ('Wodni', 'Wodnikowate'),
        ('Wrzos', 'Wrzosowate'),
        ('Zachy', 'Zachylnikowate'),
        ('Zanok', 'Zanokcicowate'),
        ('Zaraz', 'Zarazowate'),
        ('Zlozo', 'Złożone (Astrowate)'),
        ('Zabie', 'Żabieńcowate'),
        ('Zabis', 'Żabiściekowate'),
        ('Palko', 'Pałkowate'),
        ('Papro', 'Paprotkowate'),
        ('Papre', 'Paprotnikowate'),
        ('Pierw', 'Pierwiosnkowate'),
        ('Pizma', 'Piżmaczkowate'),
        ('Plywa', 'Pływaczowate'),
        ('Podrz', 'Podrzeniowate'),
        ('Pokrz', 'Pokrzywowate'),
        ('Poryb', 'Poryblinowate'),
        ('Poslo', 'Posłonkowate (Czystkowate)'),
        ('Powoj', 'Powojowate'),
        ('Przew', 'Przewiertniowate'),
        ('Przes', 'Przęstkowate'),
        ('Psian', 'Psiankowate'),
        ('Rdest', 'Rdestnicowate'),
        ('Rdest', 'Rdestowate'),
        ('Rezed', 'Rezedowate'),
        ('Rokit', 'Rokitnikowate'),
        ('Rosic', 'Rosiczkowate'),
        ('Rozow', 'Różowate'),
        ('Rzeso', 'Rzęsowate'),
        ('Rzesl', 'Rzęślowate'),
        ('Sanda', 'Sandałowcowate'),
        ('Seler', 'Selerowate (Baldaszkowe)'),
        ('Sitow', 'Sitowate'),
        ('Skaln', 'Skalnicowate'),
        ('Skrzy', 'Skrzypowate'),
        ('Sosno', 'Sosnowate'),
        ('Storc', 'Storczykowate'),
        ('Szakl', 'Szakłakowate'),
        ('Szarl', 'Szarłatowate'),
        ('Szcza', 'Szczawikowate'),
        ('Szcze', 'Szczeciowate'),
        ('Szors', 'Szorstkolistne'),
        ('Slazo', 'Ślazowate'),
        ('Swibk', 'Świbkowate'),
    )
    kategorie = (
        ('pap', 'Paprotniki'),
        ('drz', 'Drzewa Krzewy Krzewinki'),
        ('tra', 'Turzycowate Trawy'),
        ('bia', 'Zielne - Kwiaty białe'),
        ('zol', 'Zielne - Kwiaty żółte'),
        ('cze', 'Zielne - Kwiaty czerwone'),
    )
    pietra = (
        ('pog', 'Piętro pogórza'),
        ('dol', 'Piętro regla dolnego'),
        ('gor', 'Piętro regla górnego'),
        ('kos', 'Piętro kosodrzewiny'),
        ('hal', 'Piętro halne'),
        ('tur', 'Piętro turniowe'),
        ('pol', 'Piętro połonin (Bieszczady)'),
    )
    id_rosliny = models.AutoField(primary_key=True)
    nazwa_polska = models.CharField(max_length=256,unique=True)
    nazwa_lacinska = models.CharField(max_length=256)
    opis = models.TextField()
    wystepowanie = models.TextField(null=True,blank=True)
    kategoria = models.CharField(max_length=3,choices=kategorie,null=True,blank=True)
    rodzina = models.CharField(max_length=5,choices=rodziny,null=True,blank=True)
    kolor_kwiatow = models.CharField(max_length=2,choices=kolory,null=True,blank=True)
    chronione = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    endemity = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    czerwona_księga = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    lecznicze = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    trujace = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    pasozytnicze = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    owadozerne = models.CharField(max_length=1,choices=TAK_NIE,default='n',blank=True)
    pietro_roslinnosci = models.CharField(max_length=3,choices=pietra,null=True,blank=True)
    data = models.DateField()
    class Meta:
        verbose_name_plural = 'Rośliny'
    def __str__(self):
        return self.nazwa_polska
class Images(models.Model):
    TAK_NIE = (
        ('y', 'Tak'),
        ('n', 'Nie')
    )
    nazwa_polska = models.ForeignKey(Roslina, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(max_length=255, upload_to=generate_filename)
    zdjecie_glowne = models.CharField(max_length=1,choices=TAK_NIE,default='n')
    def __str__(self):
        return self.nazwa_polska.nazwa_polska
