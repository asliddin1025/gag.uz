from django.contrib import admin
from django.urls import path, include

app_name = 'client'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('client/', include('client.urls', namespace='client'))
]
