from django.urls import path
from .views import RegisterView, LogoutView, CustomLoginView,CustomRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='custom_token_obtain_pair'),
    path('login/refresh/', CustomRefreshView.as_view(), name='custom_token_refresh'),
    path('logout/', LogoutView.as_view(), name="logout")
]

