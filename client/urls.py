from django.urls import path
from .views import ClientRegistrationForm


app_name = 'client'

urlpatterns = [
    path('registration/', ClientRegistrationForm.as_view(), name='registration')
]