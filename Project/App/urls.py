from django.urls import path
from App import views

urlpatterns = [
path('',views.details),
path('father/',views.father),
path('mother/',views.mother),
path('children/',views.children),
]
