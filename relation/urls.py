from django.urls import path
from relation.views import *
app_name='nothing'
urlpatterns=[
path('brother/',brother,name='brother'),


]