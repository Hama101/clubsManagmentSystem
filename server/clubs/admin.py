from django.contrib import admin
from .models import *


class ClubsAdmin(admin.ModelAdmin):
    list_display = ('name','logo_url' ,'nbMembers' ,
                    'description','created_at'   )

admin.site.register(Clubs,ClubsAdmin)


class MembersAdmin(admin.ModelAdmin):
    list_display = ('face_img' ,'facebook', 'github',
                    'name', 'surname' ,'email' ,
                    'role' ,'clubJoined',
                    'phone' , 'verfied' , '_class')

admin.site.register(Members,MembersAdmin)



class EventsAdmin(admin.ModelAdmin):
    list_display = ('title' , 'date' , 'description' , 'event_img')

admin.site.register(Events,EventsAdmin)

class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ('title' , 'date' , 'shortDescription' ,
                    'event_img','team','local','longDescription')

admin.site.register(EventDetails,EventDetailsAdmin)

class RewardsAdmin(admin.ModelAdmin):
    list_display = ('title' , 'pic_url')

admin.site.register(Rewards,RewardsAdmin)



