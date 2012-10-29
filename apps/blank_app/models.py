# -*- coding: utf-8 -*-

from django.db import models 

from django_extensions.db.fields import CreationDateTimeField
#from someapp import strings

#class Something(models.Model):
#    """
#    Here you explain what this model is about
#    """
#    title = models.CharField(strings.TITLE, max_length=128, unique=True)
#    description = models.TextField(strings.DESCRIPTION)
#    created_at = CreationDateTimeField(verbose_name=strings.CREATED_AT)
#
#    class Meta:
#        ordering = ('title','created_at', )
#        verbose_name = strings.SOMETHING
#        verbose_name_plural = strings.SOMETHING_PLURAL
#
#    def __unicode__(self):
#       return self.title
