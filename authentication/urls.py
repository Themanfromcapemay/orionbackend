from django.urls import path
from .views import specify_username_rapid_view

urlpatterns = [
    path('specify-username-rapid/', specify_username_rapid_view, name='specify_username_rapid'),
]
