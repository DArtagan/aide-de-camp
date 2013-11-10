from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, ModelFormMixin
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from guardian.models import User
from guardian.mixins import LoginRequiredMixin

from companies.models import Company, Contact, Position

# Companies
class IndexMixin(object):
    model = Company

    # def get_queryset(self):
    #     trio = {'Company': Company.objects.filter(user=self.request.user), 'Contact': Contact.objects.filter(user=self.request.user), 'Position': Position.objects.filter(company__user=self.request.user),}
    #     return trio

class Index(LoginRequiredMixin, IndexMixin, ListView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexMixin, self).get_context_data(**kwargs)
        context['companies'] = Company.objects.filter(user=self.request.user)
        context['contacts'] = Contact.objects.filter(user=self.request.user)
        context['positions'] = Position.objects.filter(company__user=self.request.user)
        return context


