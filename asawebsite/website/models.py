import datetime

from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class Boardmember(models.Model):
    member_fname = models.CharField(max_length=200, default='', blank=True)
    member_lname = models.CharField(max_length=200, default='', blank=True)
    member_nName = models.CharField(max_length=200, default='', blank=True)
    major_minor = year = models.CharField(max_length=200,default='', blank=True)
    year = models.CharField(max_length=200,default='', blank=True)
    
    position = models.CharField(max_length=200,default='', blank=True)
    
    why_ASA = models.CharField(max_length=1000,default='', blank=True)
    fun_fact = models.CharField(max_length=1000,default='', blank=True)
    fave_mem = models.CharField(max_length=1000,default='', blank=True)
    
    fb_id = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return (self.member_fname + " " + self.member_lname)


# class Album(models.Model):
#     album_name = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __unicode__(self):              # __unicode__ on Python 2
#         return self.album_name
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'

# class Photo(models.Model):
#     parent_album = models.ForeignKey(Album)
#     image = models.ImageField(upload_to='photogallery')
#     def __unicode__(self):              # __unicode__ on Python 2
#         return self.image.name