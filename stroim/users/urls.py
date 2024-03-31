from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
app_name = 'users'

urlpatterns = [
    path(
      'logout/',
      # Прямо в описании обработчика укажем шаблон, 
      # который должен применяться для отображения возвращаемой страницы.
      # Да, во view-классах так можно! Как их не полюбить.
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
] 
