# coding=UTF-8
from django.db import models


STAN_DYWANU = (
 ('D','Dostępny'),
 ('S','Sprzedany'),
 ('K','W konserwacji'),
)

TYP_AKCJI = (
	('K','Kupno'),
	('S','Sprzedaż'),
	('K','Oddany do konserwacji'),
	('O','Odebrany z konserwacji'),	
)

# Create your models here.
class Dywan(models.Model):
	kod = models.CharField(max_length=25)
	wysokosc = models.IntegerField()
	szerokosc = models.IntegerField()
	nazwa = models.CharField(max_length=50)
	stan = models.CharField(max_length=1, choices=STAN_DYWANU)
	
	def __unicode__(self):
		return self.nazwa
	
class Zdjecie(models.Model):
	dywan = models.ForeignKey(Dywan)
	wysokosc = models.IntegerField()
	szerokosc = models.IntegerField()
	zdjecie = models.ImageField(upload_to='media') 
	
	# def __unicode__(self):
	# 	return self.zdjecie
	
class Kontrahent(models.Model):
	imie = models.CharField(max_length=255)
	nazwisko = models.CharField(max_length=255)
	
class Akcja(models.Model):
	data = models.DateTimeField()
	typ = models.CharField(max_length=1, choices=TYP_AKCJI)
	kontrahent = models.ForeignKey(Kontrahent)
	komentarz = models.CharField(max_length=512)
	
