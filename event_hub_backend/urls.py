from django.urls import path, include
from rest_framework import routers
from activities import views
from rest_framework.authtoken.views import obtain_auth_token
from accounts import views as accounts_views 

router = routers.DefaultRouter()
router.register(r'activities', views.ActivityViewSet)

urlpatterns = [
    # ... other URLs
    path('api/register/', accounts_views.RegistrationAPIView.as_view()),
    path('api/login/', accounts_views.LoginAPIView.as_view()), 
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('api/', include(router.urls)),   
]

