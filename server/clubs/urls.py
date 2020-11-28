from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home ),
    path('clubs/',v.clublist ),
    path('events/', v.events) ,
    path('members/', v.members),
    path('events/<str:title>', v.eventDetails)
    #path('new/',v.new)
]