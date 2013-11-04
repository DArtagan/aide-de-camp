from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, ModelFormMixin
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from companies.models import Company, Contact, Position

class LoginRequiredMixin(object):
    """
    View mixin which verifies that the user has authenticated.

    NOTE:
        This should be the left-most mixin of a view.
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

def ExcludeForm(the_class, *args, **kwargs):
    class ExcludeUserForm(ModelForm):
        class Meta:
            model = the_class
            exclude = ('user')
    return ExcludeUserForm

# Companies
class CompanyMixin(object):
    model = Company
    form_class = ExcludeForm(Company)
    def get_success_url(self):
        return reverse('company:company_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class CompanyIndex(LoginRequiredMixin, CompanyMixin, ListView):
    template_name = 'company/index.html'

class CompanyDetail(LoginRequiredMixin, CompanyMixin, DetailView):
    template_name = 'company/detail.html'

class CompanyCreate(LoginRequiredMixin, CompanyMixin, CreateView):
    template_name = 'company/form.html'

class CompanyUpdate(LoginRequiredMixin, CompanyMixin, UpdateView):
    template_name = 'company/form.html'

class CompanyDelete(LoginRequiredMixin, CompanyMixin, DeleteView):
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('company:company:company_index')

# Contact
class ContactMixin(object):
    model = Contact
    def get_success_url(self):
        return reverse('company:contact:contact_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Contact.objects.filter(company__user=self.request.user)

class ContactIndex(LoginRequiredMixin, ContactMixin, ListView):
    template_name = 'contact/index.html'

class ContactDetail(LoginRequiredMixin, ContactMixin, DetailView):
    template_name = 'contact/detail.html'

class ContactCreate(LoginRequiredMixin, ContactMixin, CreateView):
    template_name = 'contact/form.html'

class ContactUpdate(LoginRequiredMixin, ContactMixin, UpdateView):
    template_name = 'contact/form.html'

class ContactDelete(LoginRequiredMixin, ContactMixin, DeleteView):
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('company:contact:contact_index')

# Position
class PositionMixin(object):
    model = Position
    def get_success_url(self):
        return reverse('company:position:position_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Position.objects.filter(company__user=self.request.user)

class PositionIndex(LoginRequiredMixin, PositionMixin, ListView):
    template_name = 'position/index.html'

class PositionDetail(LoginRequiredMixin, PositionMixin, DetailView):
    template_name = 'position/detail.html'

class PositionCreate(LoginRequiredMixin, PositionMixin, CreateView):
    template_name = 'position/form.html'

class PositionUpdate(LoginRequiredMixin, PositionMixin, UpdateView):
    template_name = 'position/form.html'

class PositionDelete(LoginRequiredMixin, PositionMixin, DeleteView):
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('company:position:position_index')

