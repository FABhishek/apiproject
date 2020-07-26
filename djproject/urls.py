from django.urls import path
from djproject import views
urlpatterns = [
    path('', views.index, name='index'),
]