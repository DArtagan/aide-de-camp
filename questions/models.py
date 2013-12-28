from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('question:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('question:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('question:delete', args=[self.pk])

    def __unicode__(self):
        return self.question

