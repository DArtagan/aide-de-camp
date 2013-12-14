class QuestionMixin(object):
    model = Question
    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.object.pk})
    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

class QuestionIndex(LoginRequiredMixin, QuestionMixin, ListView):
    template_name = 'index.html'

class QuestionDetail(LoginRequiredMixin, QuestionMixin, DetailView):
    template_name = 'detail.html'

class QuestionCreate(LoginRequiredMixin, QuestionMixin, CreateView):
    template_name = 'create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

class QuestionUpdate(LoginRequiredMixin, QuestionMixin, UpdateView):
    template_name = 'update.html'

class QuestionDelete(LoginRequiredMixin, QuestionMixin, DeleteView):
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse('question_index')
