from django.urls import path
from .views import RegisterView,LoginView,UpdateUserRoleView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('users/register/', RegisterView.as_view()),
    path('users/login/',LoginView.as_view()),
    path('users/<int:pk>/role/', UpdateUserRoleView.as_view()),
    
    # path('users/<int:pk>/', UserDetailView.as_view()),
]