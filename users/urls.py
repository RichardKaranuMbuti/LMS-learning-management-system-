from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('', include('school.urls')),
]