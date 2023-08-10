from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    slug = models.SlugField(unique=True)



class Item(models.Model):
    name = models.SlugField(unique=True, default='window')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'items'
        verbose_name = 'item'
        ordering = ['-pub_date']
