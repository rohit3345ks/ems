from django.urls import path
from authapp import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout')
]
