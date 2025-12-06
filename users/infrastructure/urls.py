# Rutas de la API. Adaptan URLs a los controladores.
from django.urls import path
from users.infrastructure.views import (
    RegisterUserView, GetUserProfileView, UpdateUserView,
    DeleteUserView, ListUsersView, LoginView
)

urlpatterns = [
    path('users/', RegisterUserView.as_view(), name='register_user'),
    path('users/<int:user_id>/', GetUserProfileView.as_view(), name='get_user_profile'),
    path('users/<int:user_id>/update/', UpdateUserView.as_view(), name='update_user'),
    path('users/<int:user_id>/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('users/list/', ListUsersView.as_view(), name='list_users'),
    path('login/', LoginView.as_view(), name='login'),
]
