from django.urls import path
from djproject import views

# https://docs.djangoproject.com/en/3.1/topics/db/models/

urlpatterns = [
    path('', views.index, name='index'),
    path('/secondIndex', views.secondIndex)
]
