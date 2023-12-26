from django.db import models
from djangoflix.db.receivers import publish_state_pre_save,slugify_pre_save
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, blank=True,null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = GenericRelation(TaggedItem,related_query_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# pre_save.connect(publish_state_pre_save,sender=Category)
pre_save.connect(slugify_pre_save,sender=Category)