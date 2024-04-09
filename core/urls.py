# event_hub_backend/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for creating activities
    path('api/create-activity/', views.create_activity, name='create-activity'),

    # Endpoint for updating activities
    path('api/update-activity/<int:pk>/', views.update_activity, name='update-activity'),

    # Endpoint for user signup
    path('api/signup/', views.signup, name='signup'),

    # Endpoint for user login
    path('api/login/', views.login, name='login'),

    # Endpoint for testing token authentication
    path('api/test-token/', views.test_token, name='test-token'),
]
