from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from companies.models import Company, Contact, Position

# Companies
class CompanyMixin(object):
    model = Company
    def get_success_url(self):
        return reverse_lazy('company:company_index')
    def get_queryset(self):
        return Company.objects.all()

class CompanyIndex(CompanyMixin, ListView):
    template_name = 'company/index.html'

class CompanyDetail(CompanyMixin, DetailView):
    template_name = 'company/detail.html'

class CompanyCreate(CompanyMixin, CreateView):
    template_name = 'company/form.html'

class CompanyUpdate(CompanyMixin, UpdateView):
    template_name = 'company/form.html'

class CompanyDelete(CompanyMixin, DeleteView):
    pass

# Contact
class ContactMixin(object):
    model = Contact
    def get_success_url(self):
        return reverse_lazy('contact:contact_index')
    def get_queryset(self):
        return Contact.objects.all()

class ContactIndex(ContactMixin, ListView):
    template_name = 'contact/index.html'

class ContactDetail(ContactMixin, DetailView):
    template_name = 'contact/detail.html'

class ContactCreate(ContactMixin, CreateView):
    template_name = 'contact/form.html'

class ContactUpdate(ContactMixin, UpdateView):
    template_name = 'contact/form.html'

class ContactDelete(ContactMixin, DeleteView):
    pass

# Position
class PositionMixin(object):
    model = Position
    def get_success_url(self):
        return reverse_lazy('position:position_index')
    def get_queryset(self):
        return Position.objects.all()

class PositionIndex(PositionMixin, ListView):
    template_name = 'position/index.html'

class PositionDetail(PositionMixin, DetailView):
    template_name = 'position/detail.html'

class PositionCreate(PositionMixin, CreateView):
    template_name = 'position/form.html'

class PositionUpdate(PositionMixin, UpdateView):
    template_name = 'position/form.html'

class PositionDelete(PositionMixin, DeleteView):
    pass


