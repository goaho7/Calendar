from django.urls import path

from . import views

app_name = 'oneapp'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    #path('ajax/', views.ajax, name='ajax'),
]
