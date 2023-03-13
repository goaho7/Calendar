from django.urls import path

from . import views

app_name = 'oneapp'

urlpatterns = [
    #path('', views.DayAddView.as_view(), name='index'),
    path('', views.index, name='index'),
    #path('create/', views.day_create, name='day_create'),
    #path('ajax/', views.ajax, name='ajax'),
]
