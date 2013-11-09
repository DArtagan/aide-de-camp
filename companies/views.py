from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ImproperlyConfigured
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
    # Mixin by Chris brack3t.com
    """
    View mixin which verifies that the user has authenticated.

    NOTE:
        This should be the left-most mixin of a view.
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class PermissionRequiredMixin(object):
    # Mixin by Chris at brack3t.com
    """
    View mixin which verifies that the logged in user has the specified
    permission.

    Class Settings
    `permission_required` - the permission to check for.
    `login_url` - the login url of site
    `redirect_field_name` - defaults to "next"
    `raise_exception` - defaults to False - raise 403 if set to True

    Example Usage

        class SomeView(PermissionRequiredMixin, ListView):
            ...
            > required
            permission_required = "app.permission"

            > optional
            login_url = "/signup/"
            redirect_field_name = "hollaback"
            raise_exception = True
            ...
    """
    # Define permission check test
    def user_check(user):
        return user == 
    
    login_url = '/accounts/login/'
    permission_required = None
    raise_exception = False
    redirect_field_name = '/'

    def dispatch(self, request, *args, **kwargs):
        # Verify class settings
        if self.permission_required == None or len(
            self.permission_required.split(".")) != 2:
            raise ImproperlyConfigured("'PermissionRequiredMixin' requires "
                "'permission_required' attribute to be set.")

        has_permission = request.user.has_perm(self.permission_required)

        if not has_permission:
            if self.raise_exception:
                return HttpResponseForbidden()
            else:
                path = urlquote(request.get_full_path())
                tup = self.login_url, self.redirect_field_name, path
                return HttpResponseRedirect("%s?%s=%s" % tup)

        return super(PermissionRequiredMixin, self).dispatch(
            request, *args, **kwargs)

# Companies
class CompanyMixin(object):
    model = Company
    def get_success_url(self):
        return reverse('company:company_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

class CompanyIndex(LoginRequiredMixin, PermissionRequiredMixin, CompanyMixin, ListView):
    template_name = 'company/index.html'

class CompanyDetail(LoginRequiredMixin, CompanyMixin, DetailView):
    template_name = 'company/detail.html'

class CompanyCreate(LoginRequiredMixin, CompanyMixin, CreateView):
    template_name = 'company/form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

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

