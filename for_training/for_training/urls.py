from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('oneapp.urls', namespace='oneapp')),
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
]
