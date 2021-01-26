from django.urls import path
from apps.registration_profile.views.registration_views import \
    RegistrationView, \
    RegistrationValidationView

urlpatterns = [
    path('', RegistrationView.as_view()),
    path('validation/', RegistrationValidationView.as_view()),
]
