from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, ModelFormMixin
from guardian.mixins import LoginRequiredMixin

from questions.models import Question

class QuestionMixin(object):
    model = Question
    def get_success_url(self):
        return reverse('question:detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

class QuestionIndex(LoginRequiredMixin, QuestionMixin, ListView):
    template_name = 'questions/index.html'

class QuestionDetail(LoginRequiredMixin, QuestionMixin, DetailView):
    template_name = 'questions/detail.html'

class QuestionCreate(LoginRequiredMixin, QuestionMixin, CreateView):
    template_name = 'questions/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class QuestionUpdate(LoginRequiredMixin, QuestionMixin, UpdateView):
    template_name = 'questions/update.html'

class QuestionDelete(LoginRequiredMixin, QuestionMixin, DeleteView):
    template_name = 'questions/confirm_delete.html'
    def get_success_url(self):
        return reverse('question:index')
