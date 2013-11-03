from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from companies.forms import LoginForm
import urlparse
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

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

class LoginView(FormView):
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'login.html'
    success_url = '/'
   
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
           
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(self.get_success_url())
        else:       
            return self.form_invalid()
   
    def form_invalid(self):
        return HttpResponseRedirect(reverse('company:login'))
   
    def get_success_url(self):
        if self.success_url:
            redirect_to = self.success_url
        else:
            redirect_to = self.request.REQUEST.get(self.redirect_field_name, '')

        netloc = urlparse.urlparse(redirect_to)[1]
        if not redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL
        return redirect_to
     
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:               
            return self.form_invalid()

# Companies
class CompanyMixin(object):
    model = Company
    def get_success_url(self):
        return reverse('company:company_index', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Company.objects.all()

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
        return reverse('company:contact:contact_index')
    def get_queryset(self):
        return Contact.objects.all()

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
        #return reverse('company:position:position_update', args=[self.pk])
        return reverse('company:position:position_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Position.objects.all()

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


