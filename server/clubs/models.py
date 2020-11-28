from django.db import models as m
from django.contrib.postgres.fields import ArrayField

"""
        **** Ya hama ****
don t forget when you change or add model here
or change somthing to change it on the admin.py script
        **** Okay?? ****
"""
# Create your models here.
class Clubs(m.Model):
    name = m.CharField(max_length=255)
    logo_url = m.CharField(max_length=2083)
    nbMembers = m.IntegerField()
    description = m.CharField(max_length=2083)
    created_at = m.DateTimeField(auto_now_add=True)
    #next_event_id = next event id from events Model

class Members(m.Model):
    face_img = m.CharField(max_length=2083)
    facebook = m.CharField(max_length=2083)
    github = m.CharField(max_length=2083)
    name = m.CharField(max_length=25)
    surname = m.CharField(max_length=25)
    email = m.EmailField()
    role = m.CharField(max_length=25)
    clubJoined = m.CharField(max_length=25)
    #i can use this as and id for club joined table
    phone = m.CharField(max_length=25)
    verfied = m.BooleanField()#5alis wala la ?? xD !
    _class = m.CharField(max_length=25)#class yaqra fih


class Events(m.Model):
    title = m.CharField(max_length=25)
    date =  m.DateTimeField()
    description = m.CharField(max_length=100)
    event_img = m.CharField(max_length=2083)


class EventDetails(m.Model):
    title = m.CharField(max_length=25)
    date =  m.DateTimeField()
    shortDescription = m.CharField(max_length=100)
    event_img = m.CharField(max_length=2083)
    team = ArrayField(m.CharField(max_length=25 , blank=True),
                        default=list)
    local = m.CharField(max_length=80)
    longDescription = m.CharField(max_length=2083)



class Rewards(m.Model):
    title = m.CharField(max_length=25)
    pic_url = m.CharField(max_length=2083)