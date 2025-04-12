from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('', include ('core.urls')),
    path('login-page/', views.login_page, name='login-page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('accounts/login/', views.login_user, name='login'),
    path('go-to-core/', views.redirect_to_core, name='go-to-core'),
]