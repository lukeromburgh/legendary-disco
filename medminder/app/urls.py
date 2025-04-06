from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('', include ('website.urls')),
    path('login-page/', views.login_page, name='login-page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('accounts/login/', views.login_user, name='login'),
    path('go-to-website/', views.redirect_to_website, name='go-to-website'),
]