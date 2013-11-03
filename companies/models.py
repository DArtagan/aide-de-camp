from django.db import models
from django.core.urlresolvers import reverse

class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('company:company_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('company:company_update', args=[self.pk])

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    company = models.ManyToManyField(Company, null=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('company:contact:contact_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('company:contact:contact_update', args=[self.pk])

    def __unicode__(self):
        return self.name

class ApplyStatus(models.Model):
    status = models.CharField(max_length=50)

    def __unicode__(self):
        return self.status

class Position(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True, null=True)
    date_noted = models.DateField(auto_now_add=True)
    apply_portal = models.CharField(max_length=500, blank=True)
    apply_deadline = models.DateField(blank=True, null=True)
    apply_status =  models.ForeignKey(ApplyStatus, null=True, blank=True)
    notes = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('company:position:position_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('company:position:position_update', args=[self.pk])

    def __unicode__(self):
        return self.name
