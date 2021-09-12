from django.urls import path, include
from . import views

urlpatterns = [ #where all the pages are, you define them in views.py
   path('', views.homepage, name='homepage'),
   path('contact', views.contact, name='contact'),
   path('CV', views.CV, name='CV'),
   path('geesteswetenschapper', views.geesteswetenschapper, name='geesteswetenschapper'),
   path('informaticus', views.informaticus, name='informaticus'),
   path('onderzoeker', views.onderzoeker, name='onderzoeker')
]
