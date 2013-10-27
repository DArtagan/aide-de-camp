from django.db import models
from django.core.urlresolvers import reverse

class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    notes = models.TextField()

    def get_absolute_url(self):
        return reverse('company:company_detail', args=[self.pk])

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    company = models.ManyToManyField(Company)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    notes = models.TextField()

    def __unicode__(self):
        return self.name

class Position(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    date_noted = models.DateField(auto_now_add=True)
    notes = models.TextField()

    def __unicode__(self):
        return self.name
