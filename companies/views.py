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

class CompanyDetain(CompanyMixin, DetailView):
    template_name = 'company/detail.html'

class CompanyCreate(CompanyMixin, CreateView):
    template_name = 'company/form.html'

class CompanyUpdate(CompanyMixin, UpdateView):
    template_name = 'company/form.html'

class ComputerDelete(CompanyMixin, DeleteView):
    pass
