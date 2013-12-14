from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)
    user = models.ForeignKey(User, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('question_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('question_delete', args=[self.pk])

    def __unicode__(self):
        return self.name

